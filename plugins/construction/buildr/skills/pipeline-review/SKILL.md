---
name: Pipeline Review
description: Pull and analyze the Buildr deal pipeline — open opportunities by stage, weighted forecast, stuck deals, win rate, recent stage moves. Use this skill whenever the user asks about pipeline health, forecast, opportunity backlog, deal-by-stage breakdowns, or sales rollups. Triggers on "what's in our pipeline", "weighted forecast", "stuck deals", "deals in [stage]", "pipeline this quarter", "open opportunities", "sales backlog", "BD report" — even when "Buildr" isn't named, since Buildr is Envision's only pipeline.
---

# Buildr — Pipeline Review

Pull the pipeline and produce a clean rollup the user can act on.

## Standard sequence

1. **Hit the pre-baked summary first.** `mcp__envision-mcp__buildr_read(resource="reports", action="get_crm_summary")` returns companies count, contacts count, open deals count, pipeline metrics, recent activities, and pending tasks in one call. If the user's question is satisfied here, stop. The summary is one round-trip vs. four.

2. **For per-stage detail:** `buildr_read(resource="pipeline", action="get_metrics")` returns the aggregate per-stage breakdown.

3. **For per-deal detail:** `buildr_read(resource="deals", action="list")`, then bucket by `stage` in memory and compute:
   - Count and total `value` per stage (value is a string — cast to number)
   - Weighted forecast = Σ (value × probability / 100), treating null probability as 0
   - Stuck deals = open deals where `updated_at` is older than ~30 days
   - Average days-in-stage when stage-transition history is available

4. **For sales report time-series:** `buildr_read(resource="reports", action="get_sales")` with optional `start_date`, `end_date`, `group_by` (defaults to "month").

## Output format

Default to a Markdown table grouped by stage with a totals row, followed by a short paragraph calling out:

- Largest deal by value
- Stuck deals (>30 days idle) with deal name + last activity timestamp
- Stage transitions in the window if `get_sales` was called
- A weighted vs. unweighted forecast number side by side

Skip charts unless the user explicitly asks — Buildr returns structured data, not viz.

## Worked example

User: "Run me a pipeline review for the construction BD team."

```
1. buildr_read(resource="reports", action="get_crm_summary")     # one-call summary
2. buildr_read(resource="pipeline", action="get_metrics")         # per-stage aggregate
3. buildr_read(resource="deals", action="list")                   # per-deal detail
4. Bucket deals by stage; compute weighted forecast and stuck list
5. Render markdown table + callouts
```

## Gotchas

- The pipeline endpoint has known fallback behavior in the integration — `/pipeline/stages` is tried first, then `/pipeline`. If both fail the gateway returns an empty list (error is logged, not raised). Surface "pipeline stages unavailable" to the user rather than fabricating stage names.
- `deals.list` paginates through every page (per_page=100). For large pipelines this takes time; warn the user on visible delay.
- `value` is a string in API responses. Cast before arithmetic.
- `probability` may be null on early-stage deals — treat null as 0 for the weighted forecast, but also report the unweighted total separately so the user sees both views.

## Related

- `buildr:crm` — full surface map and auth model
- `buildr:deal-lifecycle` — when the user wants to act on a stuck deal you surfaced
- `buildr:account-360` — drill into one account's deals
