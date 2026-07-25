# Wave Manifest Schema

The wave manifest is the single source of truth for a dispatch cycle. It is created by the
framework, uploaded to GCS, and updated by the dispatcher as tasks complete.

## Schema

```json
{
  "wave_id": "string (required, unique, idempotency key)",
  "created_at": "ISO8601 timestamp",
  "git_sha": "string (optional, pins reproducibility)",
  "source_framework": "string (gsd | ralph | bmad | taskmaster | custom)",
  "status": "pending | dispatching | running | completed | partial_failure | failed",
  "tasks": [
    {
      "id": "string (required, unique within wave)",
      "index": "integer (auto-assigned, maps to JOB_COMPLETION_INDEX)",
      "cmd": "string (required, shell command to execute)",
      "image": "string (required, container image reference)",
      "inputs": {
        "key": "value (arbitrary JSON, uploaded as /inputs/task_id.json)"
      },
      "outputs_pattern": "string (glob for files to collect from /outputs/)",
      "resource_profile": "light | standard | heavy | gpu",
      "timeout_seconds": "integer (default: 600)",
      "retries": "integer (default: 2, maps to backoffLimit)",
      "depends_on": ["task_id (optional, for intra-wave ordering)"],
      "status": "pending | running | completed | failed | skipped",
      "result": {
        "exit_code": "integer",
        "duration_seconds": "float",
        "output_path": "gs:// path to result.json",
        "stdout_path": "gs:// path to stdout.log",
        "stderr_path": "gs:// path to stderr.log",
        "artifacts": ["gs:// paths to collected artifacts"],
        "error": "string (if failed)"
      }
    }
  ],
  "config": {
    "mode": "indexed-job | pod-pool | auto",
    "parallelism_cap": "integer | null (null = cluster decides)",
    "bucket": "gs:// bucket path",
    "namespace": "string (default: gke-dispatch)",
    "cluster": "string (default: from kubeconfig current-context)",
    "node_pool": "string (optional, target specific node pool)",
    "service_account": "string (K8s SA for workload identity)"
  },
  "metrics": {
    "total_tasks": "integer",
    "completed": "integer",
    "failed": "integer",
    "pending": "integer",
    "wall_clock_seconds": "float",
    "total_cpu_seconds": "float"
  }
}
```

## Validation Rules

1. `wave_id` must be unique across all dispatches — use `{framework}-{phase}-{wave}-{timestamp}` format
2. `tasks[].id` must be unique within the wave
3. `tasks[].image` must be pullable from the cluster (gcr.io/claude-mcp-457317/* or public)
4. `tasks[].depends_on` references must resolve to other task IDs in the same wave
5. `tasks[].depends_on` must not create cycles
6. `config.bucket` must exist and be writable by the dispatch service account
7. `config.parallelism_cap` if set must be ≥ 1

## Idempotency Contract

The `wave_id` is the idempotency key. When `dispatch.py` receives a manifest with a `wave_id`
that already exists in GCS:

1. Download the existing manifest from `gs://{bucket}/waves/{wave_id}/manifest.json`
2. Merge: keep `completed` task statuses, reset `failed` to `pending` (for retry)
3. Dispatch only `pending` tasks
4. Update the merged manifest in GCS

This means calling `dispatch.py` multiple times with the same `wave_id` is always safe.

## Status Transitions

```
Task:  pending → running → completed
                        → failed (after retries exhausted)
                        → skipped (dependency failed, cascade)

Wave:  pending → dispatching → running → completed (all tasks completed)
                                       → partial_failure (some failed, some completed)
                                       → failed (all tasks failed)
```

## Framework-Specific wave_id Conventions

| Framework | wave_id format | Example |
|-----------|---------------|---------|
| GSD | `gsd-{phase}-{wave}-{timestamp}` | `gsd-p3-w2-1717900800` |
| Ralph | `ralph-{loop_id}-{iteration}-{timestamp}` | `ralph-abc123-i5-1717900800` |
| BMAD | `bmad-{task_group}-{timestamp}` | `bmad-refactor-1717900800` |
| Custom | `{framework}-{identifier}-{timestamp}` | `myfw-batch42-1717900800` |
