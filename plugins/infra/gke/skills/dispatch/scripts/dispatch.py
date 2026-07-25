#!/usr/bin/env python3
"""Dispatch a wave manifest to GKE. Handles idempotent replay, compute mode selection,
and K8s Job creation with sidecar log capture."""

import argparse
import json
import sys
import tempfile
import time
from pathlib import Path

from gcs_utils import gcs_read_json, gcs_write_json, run
from job_templates import build_job_yaml


def upload_inputs(manifest: dict, bucket: str) -> None:
    wave_id = manifest["wave_id"]
    for task in manifest["tasks"]:
        if task["status"] != "pending" or not task.get("inputs"):
            continue
        path = f"{bucket}/waves/{wave_id}/inputs/{task['id']}.json"
        gcs_write_json(path, task["inputs"])


def merge_with_existing(manifest: dict, bucket: str) -> dict:
    """Idempotent replay: merge with any existing manifest in GCS."""
    wave_id = manifest["wave_id"]
    existing_path = f"{bucket}/waves/{wave_id}/manifest.json"
    existing = gcs_read_json(existing_path)
    if not existing:
        return manifest

    existing_status = {t["id"]: t for t in existing["tasks"]}
    for task in manifest["tasks"]:
        prior = existing_status.get(task["id"])
        if prior and prior["status"] == "completed":
            task["status"] = "completed"
            task["result"] = prior["result"]
        elif prior and prior["status"] == "failed":
            task["status"] = "pending"

    completed = sum(1 for t in manifest["tasks"] if t["status"] == "completed")
    pending = sum(1 for t in manifest["tasks"] if t["status"] == "pending")
    manifest["metrics"]["completed"] = completed
    manifest["metrics"]["pending"] = pending
    print(f"Idempotent merge: {completed} already completed, {pending} to dispatch", file=sys.stderr)
    return manifest


def select_mode(manifest: dict) -> str:
    mode = manifest["config"].get("mode", "auto")
    if mode == "pod-pool":
        return "pod-pool"
    return "indexed-job"


def dispatch_indexed_job(manifest: dict) -> None:
    yaml_content = build_job_yaml(manifest)
    if not yaml_content:
        print("No pending tasks to dispatch", file=sys.stderr)
        return

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(yaml_content)
        yaml_path = f.name

    try:
        result = run(["kubectl", "apply", "-f", yaml_path])
        print(result.stdout, file=sys.stderr)
    finally:
        Path(yaml_path).unlink()


def main():
    parser = argparse.ArgumentParser(description="Dispatch wave to GKE")
    parser.add_argument("--manifest", required=True, help="Path to wave manifest JSON")
    parser.add_argument("--bucket", default=None, help="Override GCS bucket")
    parser.add_argument("--namespace", default=None, help="Override K8s namespace")
    parser.add_argument("--mode", default=None, help="Override compute mode")
    parser.add_argument("--dry-run", action="store_true", help="Print Job YAML without applying")
    args = parser.parse_args()

    with open(args.manifest) as f:
        manifest = json.load(f)

    if args.bucket:
        manifest["config"]["bucket"] = args.bucket
    if args.namespace:
        manifest["config"]["namespace"] = args.namespace
    if args.mode:
        manifest["config"]["mode"] = args.mode

    bucket = manifest["config"]["bucket"]

    manifest = merge_with_existing(manifest, bucket)

    pending = [t for t in manifest["tasks"] if t["status"] == "pending"]
    if not pending:
        print("All tasks already completed. Nothing to dispatch.", file=sys.stderr)
        sys.exit(0)

    manifest["status"] = "dispatching"
    gcs_write_json(f"{bucket}/waves/{manifest['wave_id']}/manifest.json", manifest)

    upload_inputs(manifest, bucket)

    mode = select_mode(manifest)
    print(f"Dispatching {len(pending)} tasks via {mode}", file=sys.stderr)

    if args.dry_run:
        if mode == "indexed-job":
            print(build_job_yaml(manifest))
        else:
            print("Pod pool dispatch (dry-run not supported for pool mode)", file=sys.stderr)
        sys.exit(0)

    if mode == "indexed-job":
        dispatch_indexed_job(manifest)
    else:
        print(f"Pod pool mode not yet implemented, falling back to indexed-job", file=sys.stderr)
        dispatch_indexed_job(manifest)

    manifest["status"] = "running"
    manifest["metrics"]["pending"] = len(pending)
    gcs_write_json(f"{bucket}/waves/{manifest['wave_id']}/manifest.json", manifest)

    with open(args.manifest, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Wave {manifest['wave_id']} dispatched: {len(pending)} tasks running", file=sys.stderr)


if __name__ == "__main__":
    main()
