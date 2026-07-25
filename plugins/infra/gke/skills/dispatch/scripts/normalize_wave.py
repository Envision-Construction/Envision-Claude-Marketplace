#!/usr/bin/env python3
"""Normalize framework-specific task lists into a universal wave manifest."""

import argparse
import json
import sys
from datetime import datetime, timezone

from gcs_utils import DEFAULT_CONFIG, RESOURCE_PROFILES


def validate_task(task: dict, index: int) -> list[str]:
    errors = []
    if "id" not in task:
        errors.append(f"Task {index}: missing 'id'")
    if "cmd" not in task:
        errors.append(f"Task {index}: missing 'cmd'")
    if "image" not in task:
        errors.append(f"Task {index}: missing 'image'")
    profile = task.get("resource_profile", "standard")
    if profile not in RESOURCE_PROFILES:
        errors.append(f"Task {index}: invalid resource_profile '{profile}', must be one of {list(RESOURCE_PROFILES)}")
    timeout = task.get("timeout_seconds", 600)
    if not isinstance(timeout, int) or timeout < 1:
        errors.append(f"Task {index}: timeout_seconds must be a positive integer")
    retries = task.get("retries", 2)
    if not isinstance(retries, int) or retries < 0:
        errors.append(f"Task {index}: retries must be a non-negative integer")
    return errors


def check_dependency_cycles(tasks: list[dict]) -> list[str]:
    task_ids = {t["id"] for t in tasks}
    errors = []
    graph: dict[str, list[str]] = {t["id"]: t.get("depends_on", []) for t in tasks}
    for tid, deps in graph.items():
        for dep in deps:
            if dep not in task_ids:
                errors.append(f"Task '{tid}' depends on unknown task '{dep}'")
    visited: set[str] = set()
    rec_stack: set[str] = set()

    def has_cycle(node: str) -> bool:
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.discard(node)
        return False

    for tid in task_ids:
        if tid not in visited:
            if has_cycle(tid):
                errors.append(f"Dependency cycle detected involving task '{tid}'")
                break
    return errors


def normalize(wave_id: str, tasks: list[dict], git_sha: str | None = None,
              framework: str = "custom", config_overrides: dict | None = None) -> dict:
    all_errors = []
    seen_ids: set[str] = set()
    for i, task in enumerate(tasks):
        errs = validate_task(task, i)
        all_errors.extend(errs)
        tid = task.get("id")
        if tid and tid in seen_ids:
            all_errors.append(f"Duplicate task id: '{tid}'")
        if tid:
            seen_ids.add(tid)

    dep_errors = check_dependency_cycles(tasks)
    all_errors.extend(dep_errors)

    if all_errors:
        print("Validation errors:", file=sys.stderr)
        for e in all_errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    normalized_tasks = []
    for i, task in enumerate(tasks):
        normalized_tasks.append({
            "id": task["id"],
            "index": i,
            "cmd": task["cmd"],
            "image": task["image"],
            "inputs": task.get("inputs", {}),
            "outputs_pattern": task.get("outputs_pattern", "**/*"),
            "resource_profile": task.get("resource_profile", "standard"),
            "timeout_seconds": task.get("timeout_seconds", 600),
            "retries": task.get("retries", 2),
            "depends_on": task.get("depends_on", []),
            "status": "pending",
            "result": None,
        })

    config = dict(DEFAULT_CONFIG)
    if config_overrides:
        config.update(config_overrides)

    return {
        "wave_id": wave_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "git_sha": git_sha,
        "source_framework": framework,
        "status": "pending",
        "tasks": normalized_tasks,
        "config": config,
        "metrics": {
            "total_tasks": len(normalized_tasks),
            "completed": 0,
            "failed": 0,
            "pending": len(normalized_tasks),
            "wall_clock_seconds": None,
            "total_cpu_seconds": None,
        },
    }


def main():
    parser = argparse.ArgumentParser(description="Normalize tasks into a wave manifest")
    parser.add_argument("--wave-id", required=True, help="Unique wave identifier")
    parser.add_argument("--tasks", required=True, help="JSON array of task objects")
    parser.add_argument("--git-sha", default=None, help="Git SHA to pin reproducibility")
    parser.add_argument("--framework", default="custom", help="Source framework name")
    parser.add_argument("--config", default=None, help="JSON config overrides")
    parser.add_argument("--output", default="-", help="Output file path (- for stdout)")
    args = parser.parse_args()

    tasks = json.loads(args.tasks)
    config_overrides = json.loads(args.config) if args.config else None
    manifest = normalize(args.wave_id, tasks, args.git_sha, args.framework, config_overrides)

    output = json.dumps(manifest, indent=2)
    if args.output == "-":
        print(output)
    else:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Manifest written to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
