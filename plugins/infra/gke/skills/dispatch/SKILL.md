---
name: GKE Dispatch
description: >
  Dispatch parallel task waves to GKE (claude-mcp-457317). Idempotent, checkpoint-based.
  Use when 2+ independent tasks need parallel execution on GKE — from any framework.
---

# GKE Dispatch

Dispatch parallel work units to GKE with zero-drop guarantees and idempotent replay.

## Architecture

```
Framework (GSD/Ralph/any)
  │
  ├─ normalize_wave() ─→ Wave Manifest (JSON)
  │
  ├─ dispatch_wave() ──→ GKE cluster (claude-mcp-457317)
  │   ├─ Upload inputs to GCS
  │   ├─ Check prior completions (idempotent guard)
  │   ├─ Create K8s Indexed Job (or dispatch to pod pool)
  │   └─ Sidecar log-shipper captures stdout/stderr to GCS
  │
  ├─ poll_wave() ─────→ Watch for task completions
  │   ├─ GCS result.json per task index
  │   └─ Manifest status updates (completed/failed/pending)
  │
  └─ collect_results() → Aggregated results + artifacts back to framework
```

## Lossless Guarantees

| Guarantee | Mechanism |
|-----------|-----------|
| No dropped tasks | Manifest tracks every task; orphan detector flags any task without a terminal state |
| Full output capture | Sidecar ships stdout/stderr/artifacts to GCS; Cloud Logging as backup |
| Idempotent replay | Each task checks `result.json` before executing; completed tasks skip automatically |
| Atomic results | Write to `.tmp` then `gsutil mv` — no partial result files |
| Crash recovery | Manifest persists in GCS; re-run `dispatch_wave()` with same `wave_id` resumes from checkpoint |

## Quick Start

### 1. Normalize the wave

Convert framework-specific task lists into the universal wave manifest:

```bash
python3 scripts/normalize_wave.py \
  --wave-id "phase-3-wave-2" \
  --tasks '[{"id": "task-0", "cmd": "python analyze.py --input data.csv", "image": "gcr.io/claude-mcp-457317/analyst:latest"}]' \
  --output /tmp/wave-manifest.json
```

Or build programmatically — see [references/manifest-schema.md](references/manifest-schema.md).

### 2. Dispatch

```bash
python3 scripts/dispatch.py \
  --manifest /tmp/wave-manifest.json \
  --bucket gs://gke-dispatch-claude-mcp-457317 \
  --namespace gke-dispatch \
  --mode auto
```

`--mode auto` selects K8s Indexed Job (default) or pod pool (if wave frequency > 1/min).

### 3. Poll and collect

```bash
python3 scripts/collect.py \
  --manifest /tmp/wave-manifest.json \
  --bucket gs://gke-dispatch-claude-mcp-457317 \
  --timeout 900
```

Returns aggregated JSON with per-task status, outputs, logs, and artifact paths.

## Framework Integration

### Automatic detection

Any framework that produces a wave manifest can use this as its dispatch backend.

### GSD integration

GSD's `execute-phase` groups plans into waves by `files_modified` overlap analysis.
Map each independent plan to a wave task:

```python
for plan in wave.independent_plans:
    tasks.append({
        "id": plan.name,
        "cmd": f"claude-code --plan {plan.path} --worktree {plan.branch}",
        "image": "avireddy0/claude-executor:latest",
        "inputs": {"plan_path": plan.path, "git_sha": current_sha},
        "resource_profile": "standard"
    })
```

### Generic framework interface

```python
manifest = {
    "wave_id": "unique-wave-identifier",
    "git_sha": "abc123",
    "tasks": [
        {
            "id": "task-0",
            "cmd": "your-command --args",
            "image": "your-image:tag",
            "inputs": {},
            "outputs_pattern": "**/*.json",
            "resource_profile": "standard",
            "timeout_seconds": 600,
            "retries": 2
        }
    ],
    "config": {
        "mode": "auto",
        "parallelism_cap": null,
        "bucket": "gs://gke-dispatch-claude-mcp-457317"
    }
}
```

## Compute Modes

| Mode | Best for | Cold start | Mechanism |
|------|----------|------------|-----------|
| `indexed-job` | < 50 tasks, > 30s each, infrequent | 3-8s (warm node) | K8s Indexed Job, `completionMode: Indexed` |
| `pod-pool` | > 1 wave/min, < 30s tasks | 0s (pre-warmed) | Deployment + HPA, Redis/Pub/Sub queue |
| `auto` | Mixed workloads | Adaptive | Tracks wave frequency, promotes after 3 consecutive waves within 5min |

## Resource Profiles

| Profile | CPU | Memory | GPU | Use case |
|---------|-----|--------|-----|----------|
| `light` | 0.5 | 512Mi | — | Linting, formatting, simple analysis |
| `standard` | 2 | 4Gi | — | Code generation, test execution, builds |
| `heavy` | 8 | 16Gi | — | Large refactors, full test suites, compilation |
| `gpu` | 4 | 16Gi | 1×T4 | ML inference, embedding generation |

## GCS Layout

```
gs://gke-dispatch-claude-mcp-457317/
  waves/{wave_id}/
    manifest.json
    inputs/{task_id}.json
    outputs/{task_id}/
      result.json
      stdout.log
      stderr.log
      artifacts/
```

## Failure Handling

| Failure | Response |
|---------|----------|
| Task OOM | Pod restarts (backoffLimit: 2), escalates resource_profile on retry |
| Task timeout | Killed, marked `failed`, included in retry set |
| Node preemption | Pod rescheduled automatically |
| Partial wave failure | Re-run `dispatch.py` with same manifest — retries only failed/pending |
| GCS write failure | Sidecar retries 3x with backoff; Cloud Logging backup |
| Cluster unreachable | Clear error exit; manifest stays `pending` for retry |

## Envision-MCP Integration

Before raw kubectl, check for MCP dispatch tools via `search("gke dispatch batch")`.
Prefer MCP `execute()` over kubectl when available. Fallback: scripts use kubectl directly.

## Full Roadmap Execution

Phases run sequentially (gated on verification); waves within each phase run in parallel on GKE.

### From a GSD .planning/ directory

```bash
python3 scripts/run_roadmap.py \
  --planning-dir .planning \
  --bucket gs://gke-dispatch-claude-mcp-457317
```

Groups plans into waves by `files_modified` overlap and executes phases sequentially.

### From a roadmap JSON

```bash
python3 scripts/run_roadmap.py \
  --roadmap roadmap.json \
  --bucket gs://gke-dispatch-claude-mcp-457317
```

### Checkpoint resume

```bash
python3 scripts/run_roadmap.py \
  --resume gs://gke-dispatch-claude-mcp-457317/roadmaps/my-roadmap/state.json
```

Completed waves and phases skip automatically.

### Autonomous mode

Run without confirmation prompts between phases:

```bash
python3 scripts/run_roadmap.py --planning-dir .planning --auto \
  --bucket gs://gke-dispatch-claude-mcp-457317
```

Without `--auto`, pauses after each phase. `n` or Ctrl+C saves state for `--resume`.

### Dry run

Preview the execution plan without dispatching:

```bash
python3 scripts/run_roadmap.py --planning-dir .planning --dry-run
```

### Roadmap JSON format

```json
{
  "roadmap_id": "my-project-v2",
  "phases": [
    {
      "id": "phase-1",
      "title": "Foundation",
      "waves": [
        [
          {"id": "auth", "cmd": "...", "image": "...", "files_modified": ["src/auth.ts"]},
          {"id": "db", "cmd": "...", "image": "...", "files_modified": ["src/db.ts"]}
        ],
        [
          {"id": "api", "cmd": "...", "image": "...", "files_modified": ["src/auth.ts", "src/db.ts"]}
        ]
      ],
      "verification": {
        "cmd": "npm test",
        "required": true
      }
    }
  ]
}
```

Tasks with no `files_modified` overlap run in the same wave. Verification gates before the next phase.

## LLM Executor Image

Image: `avireddy0/claude-executor:latest`

- Claude Code CLI in `-p` (headless) mode
- `CLAUDE_CODE_OAUTH_TOKEN` auth via Secret Manager CSI
- GitHub App token generation (app 3604031) for multi-repo push
- Entrypoint handles clone, plan execution, GCS upload, and git push

### Build and push

```bash
cd ${CLAUDE_PLUGIN_ROOT}/skills/dispatch/docker
docker build -t avireddy0/claude-executor:latest .
docker push avireddy0/claude-executor:latest
```

### Secrets setup

Apply the SecretProviderClass (one-time):

```bash
kubectl apply -f docker/k8s-secrets.yaml
```

Requires two secrets in Secret Manager (`claude-mcp-457317`):
- `gsd-claude-oauth-token` — from `claude setup-token` on a workstation
- `gsd-github-app-private-key` — GitHub App 3604031 private key PEM

### Task definition for LLM execution

```python
tasks.append({
    "id": "refactor-auth",
    "cmd": "",  # entrypoint resolves from PLAN_PATH
    "image": "avireddy0/claude-executor:latest",
    "resource_profile": "standard",
    "inputs": {
        "repo_url": "https://github.com/Envision-Construction/Envision-MCP.git",
        "repo_branch": "main",
        "plan_path": ".planning/phase-3/PLAN-auth.md",
        "max_turns": "25",
    },
})
```

`dispatch.py` auto-detects `claude-executor` images and generates per-task Jobs with Secret Manager CSI mounts.

## References

- [references/manifest-schema.md](references/manifest-schema.md) — Full JSON schema with validation rules and idempotency contract
- [references/multi-phase-milestone.md](references/multi-phase-milestone.md) — Authoring a roadmap JSON for a multi-phase milestone; phase ordering, verification gates, and the depends_on cross-phase anti-pattern
- [references/cluster-setup.md](references/cluster-setup.md) — Error-driven remediation reference (consult only when something fails)
- [references/envision-mcp-integration.md](references/envision-mcp-integration.md) — MCP tool discovery and fallback pattern
