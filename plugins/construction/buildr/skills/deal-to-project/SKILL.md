---
name: Deal to Project
description: Convert a won Buildr deal into a Buildr project record — the standard BD-to-ops handoff. Use this skill when the user has just won a deal (or references a won deal) and needs the operational project set up in Buildr, when the user explicitly asks to convert or promote a deal into a project, or when the user says "kick off the project" after a contract close. Triggers on "we won X, set up the project", "convert [deal] to a project", "kick off the [Company] project from Buildr", "promote the won deal to a project", "create the project record for [Y]", "handoff [deal] to ops".
---

# Buildr — Deal → Project Handoff

Standardize the won-deal-to-operational-project transition so nothing falls through.

## Standard sequence

1. **Find the deal.** If the user names it, resolve via `mcp__envision-mcp__buildr_read(resource="deals", action="list")`. Verify the deal is closed-won (`status == "won"`). If it's still open, ask before promoting — some teams create the project at signature, others at contract notice. User's call.

2. **Pull the deal record** for fields to carry over:
   `buildr_read(resource="deals", action="get", item_id=deal_id)`

3. **Check for an existing project** on the same company to avoid duplicates:
   `buildr_read(resource="projects", action="list", params={"company_id": deal.company_id})`
   Surface any matches and confirm before creating a new record.

4. **Build the project create params** (`extra="forbid"` write schema — `name` required, `description` and `company_id` optional but strongly recommended):
   ```
   {
     "name": "Marina Vista — Hillsboro Shores GC",
     "description": "From won deal <deal_id>: <deal.name>",
     "company_id": "<from deal>"
   }
   ```
   Mapping conventions:
   - `deal.name` → project name (typically with site or scope qualifier appended)
   - `deal.company_id` → project `company_id`
   - `deal.value` → carried as a reference in the description (the write schema only accepts `name` / `description` / `company_id`)
   - `deal.expected_close_date` → optional follow-up `projects.update` for start_date if the gateway has been extended

5. **Confirm with the user before writing.** Won deals tend to have a real-money number behind them; misnaming the project propagates downstream into accounting, scheduling, and reporting.

6. **Write:** `buildr_write(resource="projects", action="create", params=...)`

7. **Link backward (best practice).** Drop a note on the originating deal pointing at the new project id:
   ```
   buildr_write(
     resource="activities", action="add_note",
     params={
       "entity_id": deal_id, "entity_type": "deal",
       "note": "Promoted to project <project_id>: <project_name>"
     }
   )
   ```

8. **Surface the new project_id** to the user with a hint about the next operational step (Procore project creation, Sage opening, Buildr task setup — depends on Envision's runbook for the project type).

## Don't auto-create if

- The deal is still open. Ask first.
- A project for the same company already exists. List existing projects for the company and verify there isn't a duplicate before creating.

## Gotchas

- `projects.create` accepts a narrow set of fields per the write schema (`name`, `description`, `company_id`). For extra fields (project_type, start/end dates, value), check whether the gateway schema has been extended; if not, create with the allowed fields first, then follow with `projects.update` for the rest.
- Won deal value may differ from project budget. Don't assume they're the same — ask if the user wants `deal.value` carried as the project value, or if a fresh budget is being established.
- The handoff often spawns operational tasks (open Procore, set up Sage job, create Buildr tasks for kickoff). After the project is created, offer the user a checklist or follow with `buildr:activity-logging` to seed the project record with a kickoff note.

## Related

- `buildr:crm` — surface map
- `buildr:deal-lifecycle` — the `deals.win` call that typically precedes this
- `buildr:account-360` — verify there isn't already a project on this account
- `buildr:activity-logging` — log the handoff kickoff
