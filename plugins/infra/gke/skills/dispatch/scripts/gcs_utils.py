#!/usr/bin/env python3
"""Shared GCS utilities and constants for gke-dispatch scripts."""

import json
import subprocess
import tempfile
from pathlib import Path


RESOURCE_PROFILES = {
    "light": {"cpu": "500m", "memory": "512Mi", "cpu_limit": "1", "memory_limit": "1Gi"},
    "standard": {"cpu": "2", "memory": "4Gi", "cpu_limit": "4", "memory_limit": "8Gi"},
    "heavy": {"cpu": "8", "memory": "16Gi", "cpu_limit": "16", "memory_limit": "32Gi"},
    "gpu": {"cpu": "4", "memory": "16Gi", "cpu_limit": "8", "memory_limit": "32Gi", "gpu": "1"},
    "gpu_high": {
        "cpu": "8", "memory": "64Gi", "cpu_limit": "16", "memory_limit": "128Gi",
        "gpu": "1", "accelerator": "nvidia-h100-80gb",
    },
    "gpu_a100": {
        "cpu": "8", "memory": "64Gi", "cpu_limit": "16", "memory_limit": "128Gi",
        "gpu": "1", "accelerator": "nvidia-a100-80gb",
    },
}

DEFAULT_CONFIG = {
    "mode": "auto",
    "parallelism_cap": None,
    "bucket": "gs://gke-dispatch-claude-mcp-457317",
    "namespace": "gke-dispatch",
    "cluster": None,
    "node_pool": None,
    "service_account": "gke-dispatch-worker",
}


def run(cmd: list[str], check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=check, capture_output=capture, text=True)


def gcs_exists(path: str) -> bool:
    return run(["gsutil", "ls", path], check=False).returncode == 0


def gcs_read_json(path: str) -> dict | None:
    result = run(["gsutil", "cat", path], check=False)
    if result.returncode != 0:
        return None
    return json.loads(result.stdout)


def gcs_write_json(path: str, data: dict) -> None:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f, indent=2)
        tmp = f.name
    run(["gsutil", "cp", tmp, path])
    Path(tmp).unlink()


def gcs_list(prefix: str) -> list[str]:
    result = run(["gsutil", "ls", prefix], check=False)
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]
