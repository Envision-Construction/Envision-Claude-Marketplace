---
name: Deal Lifecycle
description: Create, advance, or close out deals and opportunities in Buildr — new opportunity intake, stage transitions, mark won/lost with attribution, update value or owner or probability. Use this skill whenever the user wants to act on a deal record. Triggers on "create a new deal", "new opportunity", "we won the [X] deal", "we lost [Y]", "move [deal] to [stage]", "advance the [X] opportunity", "update the value on [deal]", "reassign [deal] to [user]", "change the probability on [X]", "new lead came in", "we got the [X] contract", "kill the [Y] deal".
---

# Buildr — Deal Lifecycle

Manage the full deal arc: create → move stage → win or lose.

## Pick the right action

| User intent | Action | Required |
|-------------|--------|----------|
| New opportunity | `deals.create` | `name`; optional `value`, `company_id`, `stage` |
| Update fields | `deals.update` | `deal_id` (via `item_id` or `params`); any field |
| Move to next stage | `deals.move_stage` | `deal_id`, `stage` |
| Closed-won | `deals.win` | `deal_id`; optional `won_value` |
| Closed-lost | `deals.lose` | `deal_id`; optional `reason` |

## Standard sequence

### Creating a deal

1. **Resolve company_id** — required for meaningful pipeline analytics. If the user names a company, look it up (`companies.list` + match). If the company isn't in Buildr yet, offer to create it first via `companies.create`.
2. **Build params:**
   ```
   {
     "name": "Marina Vista — GC bid",
     "value": "158200000",       # string per write schema
     "company_id": "...",
     "stage": "qualifying"        # must match an existing pipeline stage exactly
   }
   ```
3. **Write:** `mcp__envision-mcp__buildr_write(resource="deals", action="create", params=...)`
4. **Surface the new deal_id.**

### Moving a stage

- Get the current stage list first via `buildr_read(resource="pipeline", action="get")` so you propose a real stage name, not an invented one.
- `buildr_write(resource="deals", action="move_stage", params={"deal_id": "...", "stage": "negotiation"})`

### Winning / losing

- **Win:** `buildr_write(resource="deals", action="win", params={"deal_id": "..."})`. If the user mentions a final number that differs from the deal's tracked value, pass `won_value` so reports track the true close number.
- **Lose:** `buildr_write(resource="deals", action="lose", params={"deal_id": "...", "reason": "..."})`. Always capture the reason if the user gave one — that feeds win/loss analysis.

## Confirm before terminal writes

`win` and `lose` are terminal — they flip `status` from open to won/lost and remove the deal from open-pipeline rollups. Always echo deal name + value + (for losses) reason back to the user and confirm before calling, unless the user has clearly already authorized ("yes, mark Marina Vista won").

## Required-context patterns

- "We won the X deal" → resolve deal by name, confirm value, call `deals.win`.
- "New lead from [Company]" → company exists? → `deals.create`. Not yet? → `companies.create` first, then `deals.create` with the new `company_id`.
- "Bump probability on X to 80%" → `deals.update` with `{"deal_id": "...", "probability": 80}`.
- "Move X to negotiation" → look up stage names; `deals.move_stage`.
- "Reassign X to [user]" → resolve user via `users.list`, then `deals.update` with `{"deal_id": "...", "owner_id": "..."}`.

## Gotchas

- `value` is a string in the write schema (`extra="forbid"`). Cast numbers before sending: `"158200000"`, not `158200000`.
- `stage` must match an existing pipeline stage exactly — don't invent. Pull the stage list first if you're unsure.
- After `deals.win`, the natural next step is `buildr:deal-to-project` to spin up the project record. Offer it.
- `probability` is an integer 0–100; pydantic will reject floats or strings.
- `win` and `lose` are typed-only verbs — no equivalent exists in the generic dispatcher. You cannot transition a deal to won/lost via `deals.update`.

## Related

- `buildr:crm` — full surface map
- `buildr:pipeline-review` — find the stuck deal you're now advancing
- `buildr:deal-to-project` — the natural follow-up after `deals.win`
- `buildr:activity-logging` — log the conversation that drove the stage change
