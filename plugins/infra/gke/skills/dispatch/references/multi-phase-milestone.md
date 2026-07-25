# Multi-Phase Milestone Pattern

When a milestone spans multiple phases that must run in order with verification gates between them, author a single roadmap JSON and dispatch with `scripts/run_roadmap.py`. The dispatcher runs phases sequentially and waves within each phase in parallel — one command runs the whole milestone.

## When to use this vs a single-wave manifest

| Use roadmap JSON | Use single-wave manifest |
|------------------|--------------------------|
| ≥2 phases with verification gates between them | One batch of independent tasks |
| Tasks share no state across phases | Tasks share intermediate artifacts |
| You want resume + dry-run for the whole milestone | One-shot dispatch |
| Plan files already split per-phase in `.planning/` | Ad-hoc task list |

## How phase ordering actually works

`run_roadmap.py` does NOT walk `phases[]` strictly in order. It partitions the phases into **sequential batches**, where phases within a batch run in parallel because their `files_modified` sets are disjoint (see `scripts/run_roadmap.py:372` `group_phases_into_batches`).

Algorithm, greedy from `phases[0]`:

1. Start a new batch. Add the next remaining phase to it; its files become the batch's claimed file set.
2. For each subsequent remaining phase, add it to the current batch if and only if its `files_modified` set is disjoint from the batch's claimed set.
3. Close the batch when no more phases fit. Start a new batch with the next remaining phase.
4. Batches run sequentially; the next batch waits for all phases in the prior batch to complete (and for any required `verification.cmd` to pass).

The practical implication: **`files_modified` is load-bearing for phase ordering.** If you forget to declare it, the grouper sees disjoint sets everywhere and collapses every phase into a single parallel batch — which is almost never what you want. Treat `files_modified` as required, not optional, for every task in a multi-phase manifest.

**Do NOT use `depends_on` to chain across phases.** `depends_on` is intra-wave only (see `manifest-schema.md` validation rule 4). References to task IDs in other waves or other phases will fail validation. If a downstream phase truly needs an artifact from an upstream one, the upstream phase's `verification.cmd` should write it to GCS or a known path, and the downstream task's `inputs` should reference it. Cross-phase ordering comes from `files_modified` overlap, not `depends_on`.

## Wave grouping within a phase

Each task in a phase carries an implicit wave assignment. There are two ways to express it:

1. **Explicit `waves: [[...], [...]]`** — author lists each wave's tasks as a sub-array. Best when wave structure is non-trivial.
2. **Derive from `files_modified` overlap** — pass a flat task list and let `normalize_wave.py` group by file overlap. Best for simple phases where overlap analysis matches intent.

The example below uses explicit waves because real plans usually carry a `wave:` field in their frontmatter that the JSON author should respect.

## Annotated mini-skeleton (3 phases)

```json
{
  "roadmap_id": "example-milestone",
  "phases": [
    {
      "id": "phase-A-bootstrap",
      "title": "Bootstrap shared infrastructure",
      "waves": [
        [
          {
            "id": "A-01",
            "cmd": "",
            "image": "avireddy0/claude-executor:latest",
            "resource_profile": "standard",
            "inputs": {
              "repo_url": "https://github.com/Envision-Construction/Envision-MCP.git",
              "repo_branch": "main",
              "plan_path": ".planning/phases/A/A-01-PLAN.md",
              "max_turns": "25"
            },
            "files_modified": ["repos/Envision-MCP/config/settings.py"]
          }
        ]
      ],
      "verification": {
        "cmd": "cd repos/Envision-MCP && pytest tests/config -q",
        "required": true
      }
    },

    {
      "id": "phase-B-parallel-refactor",
      "title": "Per-service refactors (parallel)",
      "waves": [
        [
          {"id": "B-01", "cmd": "", "image": "avireddy0/claude-executor:latest",
           "resource_profile": "standard",
           "inputs": {"plan_path": ".planning/phases/B/B-01-PLAN.md", "repo_url": "https://github.com/Envision-Construction/Envision-MCP.git", "repo_branch": "main"},
           "files_modified": ["repos/Envision-MCP/gateway/integrations/svc_a.py"]},
          {"id": "B-02", "cmd": "", "image": "avireddy0/claude-executor:latest",
           "resource_profile": "standard",
           "inputs": {"plan_path": ".planning/phases/B/B-02-PLAN.md", "repo_url": "https://github.com/Envision-Construction/Envision-MCP.git", "repo_branch": "main"},
           "files_modified": ["repos/Envision-MCP/gateway/integrations/svc_b.py"]}
        ],
        [
          {"id": "B-03", "cmd": "", "image": "avireddy0/claude-executor:latest",
           "resource_profile": "standard",
           "inputs": {"plan_path": ".planning/phases/B/B-03-PLAN.md", "repo_url": "https://github.com/Envision-Construction/Envision-MCP.git", "repo_branch": "main"},
           "depends_on": ["B-01", "B-02"],
           "files_modified": ["repos/Envision-MCP/gateway/routers/aggregated.py"]}
        ]
      ],
      "verification": {
        "cmd": "cd repos/Envision-MCP && pytest tests/integrations -q",
        "required": true
      }
    },

    {
      "id": "phase-C-ml-retrain",
      "title": "Retrain intent classifier on new schema",
      "waves": [
        [
          {"id": "C-01", "cmd": "python retrain.py --epochs 20",
           "image": "avireddy0/intent-trainer:latest",
           "resource_profile": "gpu",
           "timeout_seconds": 3600,
           "inputs": {"dataset_uri": "gs://gke-dispatch-claude-mcp-457317/datasets/intent-v3.parquet"}}
        ]
      ],
      "verification": {
        "cmd": "python verify_model.py --min-f1 0.85",
        "required": true
      }
    }
  ]
}
```

Notes on the skeleton:

- `phase-A` has 1 wave with 1 task — minimum viable phase
- `phase-B` shows intra-phase parallelism: wave 1 runs B-01 and B-02 in parallel; wave 2 runs B-03 after both complete via `depends_on: ["B-01", "B-02"]`. Cross-wave (intra-phase) `depends_on` is valid; cross-phase is not.
- `phase-C` shows `resource_profile: "gpu"` for an ML retrain step — only profile this where you actually need a GPU (verify quotas with `gcq <region>`; legacy `gcloud compute regions describe` does not show modern GPU SKUs).
- Each task uses `avireddy0/claude-executor:latest` for plan-driven work. The executor reads `inputs.plan_path` and runs Claude Code in headless mode against the named repo+branch.
- `verification.cmd` runs in the dispatcher's working directory after the phase's last wave completes. Set `required: false` on advisory checks; `true` blocks the next phase on failure.

## Invocation matrix

```bash
# Dry run — print phase/wave/task plan without dispatching
python3 scripts/run_roadmap.py --roadmap roadmap.json --dry-run

# Interactive — pause between phases, "n" to stop and save resume state
python3 scripts/run_roadmap.py --roadmap roadmap.json \
  --bucket gs://gke-dispatch-claude-mcp-457317

# Autonomous — no prompts, run to completion
python3 scripts/run_roadmap.py --roadmap roadmap.json --auto \
  --bucket gs://gke-dispatch-claude-mcp-457317

# Resume from saved state after interrupt or partial failure
python3 scripts/run_roadmap.py \
  --resume gs://gke-dispatch-claude-mcp-457317/roadmaps/<roadmap_id>/state.json
```

`--resume` re-uses each task's `wave_id` as its idempotency key, so completed tasks from prior runs skip automatically. Failed tasks reset to `pending` and re-dispatch.

## Real-world example

The v25.0 ADK-Native Architecture milestone is materialized as a roadmap JSON at:

`~/GitHub/central-command/.planning/milestones/v25.0-roadmap.json`

8 phases (124–131), 31 plans, 21 waves total. Phase 128 (OpenAPIToolset Migration) carries the bulk: 12 plans across 5 waves with non-trivial `depends_on` chains between waves. Phases 124 and 125 run their plans fully in parallel within a single wave. Phases 126, 127, 129, 130, 131 are strict serial wave-per-plan chains.

Phase parallelism (per `--dry-run`):
- **Batch 1 (parallel):** 124 (Envision-MCP requirements), 125 (slackwrapper), 126 (gateway/tool_registry.py + gateway/servers/) — disjoint file sets
- **Batches 2–6 (serial):** 127 → 128 → 129 → 130 → 131 — all touch overlapping `gateway/` files (agents, routers, integrations, mcp_bridge), so they cannot share a batch

Each task points at the corresponding `<phase>-<NN>-PLAN.md` file under `.planning/milestones/v25.0-phases/`, which the executor image reads to drive the actual work. Every task carries `files_modified` so the grouper can compute the overlap correctly — without that, all 8 phases would collapse into a single parallel batch.

## Anti-patterns

- **Cross-phase `depends_on`** — does not validate. Use `files_modified` overlap (or the phase batching it produces) and `verification.cmd` instead.
- **Tasks without `files_modified`** — the grouper treats them as touching nothing, so every phase becomes parallel-eligible regardless of actual conflicts. Always declare `files_modified` on every task in a multi-phase manifest.
- **One giant wave with all tasks** — loses the verification gate between logical units. Split into phases.
- **`verification.required: false` everywhere** — the gate becomes ornamental. Either run the check or remove it.
- **`gpu` profile on every task** — ties up GPU node capacity for non-GPU work. Audit which plans actually need it.
- **Hard-coded image tags in tasks** — pin to `latest` only when you mean it; otherwise use a sha256 digest for reproducibility.
