#!/usr/bin/env python3
"""Tests for job_templates.py — YAML generation for K8s Jobs."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import yaml
from job_templates import (
    build_executor_jobs_yaml,
    build_indexed_job_yaml,
    build_job_yaml,
    _job_name,
    _resources,
)


def _manifest(tasks, image="alpine:latest", **config_overrides):
    config = {
        "bucket": "gs://test-bucket",
        "namespace": "test-ns",
        "service_account": "test-sa",
        "parallelism_cap": None,
    }
    config.update(config_overrides)
    return {
        "wave_id": "test-wave-1",
        "tasks": [
            {
                "id": t["id"],
                "cmd": t.get("cmd", "echo hi"),
                "image": t.get("image", image),
                "status": t.get("status", "pending"),
                "resource_profile": t.get("resource_profile", "standard"),
                "timeout_seconds": t.get("timeout_seconds", 600),
                "retries": t.get("retries", 2),
                "inputs": t.get("inputs", {}),
            }
            for t in tasks
        ],
        "config": config,
    }


class TestJobName:
    def test_basic(self):
        assert _job_name("wave-1") == "gke-dispatch-wave-1"

    def test_underscores_replaced(self):
        assert _job_name("my_wave") == "gke-dispatch-my-wave"

    def test_truncated_to_63(self):
        name = _job_name("a" * 100)
        assert len(name) <= 63

    def test_with_suffix(self):
        name = _job_name("wave-1", "task-0")
        assert name == "gke-dispatch-wave-1-task-0"


class TestResources:
    def test_known_profiles(self):
        for profile in ("light", "standard", "heavy", "gpu"):
            r = _resources(profile)
            assert "cpu" in r
            assert "memory" in r

    def test_unknown_falls_back_to_standard(self):
        assert _resources("nonexistent") == _resources("standard")

    def test_gpu_has_gpu_key(self):
        r = _resources("gpu")
        assert "gpu" in r


class TestBuildIndexedJobYaml:
    def test_empty_when_no_pending(self):
        m = _manifest([{"id": "t1", "status": "completed"}])
        assert build_indexed_job_yaml(m) == ""

    def test_generates_valid_yaml(self):
        m = _manifest([{"id": "t1"}, {"id": "t2"}])
        result = build_indexed_job_yaml(m)
        doc = yaml.safe_load(result)
        assert doc["kind"] == "Job"
        assert doc["spec"]["completionMode"] == "Indexed"
        assert doc["spec"]["completions"] == 2

    def test_namespace_from_config(self):
        m = _manifest([{"id": "t1"}], namespace="custom-ns")
        result = build_indexed_job_yaml(m)
        doc = yaml.safe_load(result)
        assert doc["metadata"]["namespace"] == "custom-ns"

    def test_resources_from_profile(self):
        m = _manifest([{"id": "t1", "resource_profile": "heavy"}])
        result = build_indexed_job_yaml(m)
        doc = yaml.safe_load(result)
        containers = doc["spec"]["template"]["spec"]["containers"]
        task_container = next(c for c in containers if c["name"] == "task")
        assert task_container["resources"]["requests"]["cpu"] == "8"
        assert task_container["resources"]["requests"]["memory"] == "16Gi"

    def test_has_log_shipper_sidecar(self):
        m = _manifest([{"id": "t1"}])
        result = build_indexed_job_yaml(m)
        doc = yaml.safe_load(result)
        containers = doc["spec"]["template"]["spec"]["containers"]
        names = [c["name"] for c in containers]
        assert "log-shipper" in names

    def test_has_idempotent_check_init(self):
        m = _manifest([{"id": "t1"}])
        result = build_indexed_job_yaml(m)
        doc = yaml.safe_load(result)
        inits = doc["spec"]["template"]["spec"]["initContainers"]
        assert inits[0]["name"] == "idempotent-check"

    def test_skips_completed_tasks(self):
        m = _manifest([
            {"id": "t1", "status": "completed"},
            {"id": "t2", "status": "pending"},
        ])
        result = build_indexed_job_yaml(m)
        doc = yaml.safe_load(result)
        assert doc["spec"]["completions"] == 1


class TestBuildExecutorJobsYaml:
    def test_empty_when_no_pending(self):
        m = _manifest([{"id": "t1", "status": "completed", "image": "avireddy0/claude-executor:latest"}])
        assert build_executor_jobs_yaml(m) == ""

    def test_per_task_jobs(self):
        m = _manifest([
            {"id": "t1", "image": "avireddy0/claude-executor:latest"},
            {"id": "t2", "image": "avireddy0/claude-executor:latest"},
        ])
        result = build_executor_jobs_yaml(m)
        docs = list(yaml.safe_load_all(result))
        assert len(docs) == 2
        assert all(d["kind"] == "Job" for d in docs)

    def test_has_secrets_init(self):
        m = _manifest([{"id": "t1", "image": "avireddy0/claude-executor:latest"}])
        result = build_executor_jobs_yaml(m)
        doc = yaml.safe_load(result)
        inits = doc["spec"]["template"]["spec"]["initContainers"]
        assert inits[0]["name"] == "fetch-secrets"

    def test_env_vars_set(self):
        m = _manifest([{
            "id": "t1",
            "image": "avireddy0/claude-executor:latest",
            "inputs": {"repo_url": "https://github.com/test/repo.git", "plan_path": ".planning/PLAN.md"},
        }])
        result = build_executor_jobs_yaml(m)
        doc = yaml.safe_load(result)
        containers = doc["spec"]["template"]["spec"]["containers"]
        executor = next(c for c in containers if c["name"] == "executor")
        env_map = {e["name"]: e["value"] for e in executor["env"]}
        assert env_map["REPO_URL"] == "https://github.com/test/repo.git"
        assert env_map["PLAN_PATH"] == ".planning/PLAN.md"
        assert env_map["GITHUB_APP_ID"] == "3604031"


class TestBuildJobYamlRouter:
    def test_routes_to_executor(self):
        m = _manifest([{"id": "t1", "image": "avireddy0/claude-executor:latest"}])
        result = build_job_yaml(m)
        docs = list(yaml.safe_load_all(result))
        assert docs[0]["spec"]["template"]["spec"]["initContainers"][0]["name"] == "fetch-secrets"

    def test_routes_to_indexed(self):
        m = _manifest([{"id": "t1", "image": "alpine:latest"}])
        result = build_job_yaml(m)
        doc = yaml.safe_load(result)
        assert doc["spec"]["completionMode"] == "Indexed"

    def test_empty_when_all_done(self):
        m = _manifest([{"id": "t1", "status": "completed"}])
        assert build_job_yaml(m) == ""
