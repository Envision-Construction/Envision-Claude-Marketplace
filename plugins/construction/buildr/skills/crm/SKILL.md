---
name: Buildr CRM
description: Envision Construction's Buildr CRM — the system of record for BD pipeline, deals/opportunities, accounts, contacts, activities, and won-project handoffs. Use this skill whenever the user mentions Buildr, the BD pipeline, opportunities, deals, accounts or companies in our CRM, contact records, sales activity tracking, or wants any CRM data. Also trigger on adjacent phrasing — "pipeline", "opportunities", "leads", "prospects", "accounts", "CRM", "financials", "project documents", "workforce", "bidding packages" — even when Buildr isn't named explicitly, since Buildr is Envision's only CRM. Routes through the existing Envision-MCP gateway tools (buildr_read / buildr_write); do NOT build new HTTP clients.
---

# Buildr CRM (via Envision-MCP gateway)

Buildr is the CRM in Envision Construction's stack — the system of record for business development (deals/opportunities, accounts, contacts, BD activities, and the handoff to operational projects).

## Access path

Sessions reach Buildr through the Envision-MCP gateway, which holds the OAuth2 client-credentials grant and refreshes the token automatically (2hr TTL). You never see the API key.

Three tools are registered on the gateway:

- `mcp__envision-mcp__buildr_read(resource, action, params)` — read-only
- `mcp__envision-mcp__buildr_write(resource, action, params)` — mutating
- `mcp__envision-mcp__buildr` — legacy unified dispatcher (deprecation window; prefer the split tools)

If `mcp__envision-mcp__*` tools aren't loaded in the current session, fetch their schemas first with ToolSearch: `select:mcp__envision-mcp__buildr_read,mcp__envision-mcp__buildr_write`.

## Surface map

### Typed resources (12) — hand-written adapters with non-CRUD verbs

| Resource | Read actions | Write actions |
|----------|--------------|---------------|
| deals | list, get | create, update, move_stage, win, lose |
| pipeline | get, get_metrics | — |
| companies | list, get | create, update |
| contacts | list, get | create, update |
| projects | list, get | create, update |
| activities | list | create, log_call, log_meeting, add_note |
| tasks | list | create, update, complete |
| tags | list | create, add_to_entity |
| users | list, get | — |
| custom_fields | list | — |
| reports | get_sales, get_activity, get_crm_summary | — |
| connection | test | — |

### Generic resources (37) — registry-driven CRUD dispatcher (PR #722 / post-deploy)

Default verbs: `list`, `get`, `create`, `update`, `delete`. Resources marked **list only**, **list, get only**, or **list, update only** are restricted by the registry `supports` tuple — `buildr_write` will reject unsupported verbs with `INVALID_OPERATION`. Resources marked "see footgun list below" have non-obvious required fields documented in the section after Write schemas.

| Resource | Notes |
|----------|-------|
| bidding_packages | `project_id`, `name`, `cost_code_id` required on create |
| calls | `call_outcome_id`, `company_id`, `contact_id`, `recorded_at` required on create — see footgun list below |
| call_outcomes | **list only** — reference data |
| comments | `commentable_type` (Literal enum, CamelCase), `commentable_id`, `html` required on create — see footgun list below |
| company_roles | **list, update only** — no create/delete |
| contract_types | reference data |
| custom_field_groups | |
| delivery_methods | reference data |
| divisions | **list only** — reference data |
| document_categories | |
| emails | `subject`, `from` required on create; `body_html` and `body_text` are mutually exclusive — see footgun list below |
| financials_billing_periods | **list only**; `project_id` required |
| financials_change_orders | `project_id` required; amounts in cents |
| financials_closed_periods | `project_id` required |
| financials_forecast_periods | **list only**; `project_id` required |
| financials_prime_contracts | `project_id` required; amounts in cents — see footgun list below |
| gng_features | **list, get only** |
| gng_lead_answers | `project_id` + `gng_lead_survey_id` required |
| gng_lead_surveys | |
| gng_project_answers | `project_id` + `gng_project_survey_id` required |
| gng_project_surveys | |
| gng_survey_template_questions | `gng_survey_template_id` required |
| gng_survey_templates | **list, get only** |
| industries | reference data |
| lead_sources | reference data |
| loss_reasons | reference data |
| market_sectors | **list only** — reference data |
| meetings | `title`, `meeting_at`, `recorded_at`, `company_id` required on create — see footgun list below |
| project_changesets | **list only**; `project_id` required |
| project_directory_contacts | `project_id` required |
| project_directory_memberships | `project_id` required |
| project_document_folders | `project_id` required |
| project_documents | `project_id`, `document_category_id`, `attachment` required on create |
| project_photos | `project_id` required |
| project_stages | reference data |
| project_team_memberships | `project_id` required |
| project_team_roles | reference data |
| tender_types | reference data |
| trades | **list only** — reference data |
| webhook_messages | **list, get only** |
| webhooks | |
| work_scopes | reference data |
| workforce_assignments | `project_id`, `role_id`, `project_phase` (`"construction"` or `"precon"`), `start_date`, `end_date`, `utilization` (0–100) required; `workforce_id` via `item_id` |

## Call patterns

**Typed resources:**
```
mcp__envision-mcp__buildr_read(resource="deals", action="list")
mcp__envision-mcp__buildr_read(resource="companies", action="get", item_id="<company_id>")
mcp__envision-mcp__buildr_read(resource="pipeline", action="get_metrics")
mcp__envision-mcp__buildr_read(resource="reports", action="get_crm_summary")

mcp__envision-mcp__buildr_write(
  resource="deals", action="create",
  params={"name": "Marina Vista GC", "value": "158200000", "company_id": "..."}
)
mcp__envision-mcp__buildr_write(
  resource="deals", action="move_stage",
  params={"deal_id": "...", "stage": "negotiation"}
)
mcp__envision-mcp__buildr_write(
  resource="activities", action="log_call",
  params={"contact_id": "...", "notes": "Discussed schedule changes", "duration": 30}
)
```

**Generic resources (all five CRUD verbs work the same way):**
```
mcp__envision-mcp__buildr_read(resource="project_documents", action="list",
  params={"project_id": "..."})

mcp__envision-mcp__buildr_read(resource="financials_billing_periods", action="get",
  item_id="<period_id>")

mcp__envision-mcp__buildr_write(resource="bidding_packages", action="create",
  params={"project_id": "...", "name": "Earthwork", "cost_code_id": "...", "due_date": "2026-06-30"})

mcp__envision-mcp__buildr_write(resource="project_documents", action="delete",
  item_id="<doc_id>")
```

`item_id` can substitute for the per-resource id field in params for get/update/delete operations.

## Write schemas (extra="forbid")

Write actions validate params via pydantic with `extra="forbid"` — unknown keys are rejected with `VALIDATION_ERROR`. Common required fields:

- `deals.create`: `name` required; optional `value` (string), `company_id`, `stage`
- `deals.move_stage`: `stage` required; `deal_id` from item_id or params
- `companies.create`: `name` required
- `contacts.create`: `name` required; optional `email`, `phone`, `company_id`
- `activities.log_call` / `log_meeting`: `contact_id` required
- `activities.add_note`: `entity_id`, `entity_type` ("deal" / "contact" / "company"), `note` all required
- `tasks.create`: `title` required; optional `assignee_id`, `due_date` (YYYY-MM-DD)
- `tags.add_to_entity`: `tag_id`, `entity_id`, `entity_type` all required

## Required fields — generic resources (footgun list)

**Financial amounts**: ALL Buildr financial fields use `_in_cents` integers. `amount_in_cents: 1500000` = $15,000. Never pass decimal dollars.

**bidding_packages.create**: `project_id`, `name`, `cost_code_id` required

**calls.create**: `call_outcome_id`, `company_id`, `contact_id`, `recorded_at` (ISO 8601) required
— different from `activities.log_call` which only needs `contact_id`

**meetings.create**: `title`, `meeting_at`, `recorded_at`, `company_id` required
— different from `activities.log_meeting` which only needs `contact_id`

**comments.create**: `commentable_type` (CamelCase Literal, NOT snake_case), `commentable_id` (str), `html` (str)
Valid `commentable_type` values: `"Budgets::ChangeRequest"` | `"Budgets::Alternate"` | `"Company"` | `"Contact"` | `"Lead"` | `"Project"`

**emails.create**: `subject`, `from` required; `body_html` and `body_text` are mutually exclusive (send one, not both)

**financials_change_orders.create**: `project_id`, `amount_in_cents` (int), `approval_date` (YYYY-MM-DD) required

**financials_prime_contracts.create**: `project_id` (int), `initial_contract_value_in_cents` (int), `initial_construction_cost_in_cents` (int) required

**workforce_assignments.create**: `project_id` (int), `role_id`, `project_phase` (`"construction"` or `"precon"`), `start_date` (YYYY-MM-DD), `end_date` (YYYY-MM-DD), `utilization` (int 0–100) required; `workforce_id` goes in `item_id`

**project_documents.create**: `document_category_id`, `attachment` (Dict with `filename`, `content_type`, and either `url` or `base64_data`) required

## Pagination

The gateway paginates internally (per_page=100, walks all pages) before returning. List actions return the full result set in a single response, not a cursor. For very large reads (1000+ records), expect 5-15s of latency — surface that to the user when visible.

## Common errors

- `INVALID_OPERATION` — unknown resource.action, or `buildr_read` was called on a write action. The response carries `available_operations` grouped by resource.
- `VALIDATION_ERROR` — params failed pydantic validation. Check field names (snake_case) and the `extra="forbid"` rule above.
- `DISPATCH_ERROR` — upstream Buildr API or OAuth failure. The gateway retries 3× with backoff for 429/5xx; if you still see this, the upstream is degraded or the BUILDR_API_KEY / BUILDR_API_SECRET in Secret Manager need rotation.

## Sibling skills (workflow-specific)

- `buildr:pipeline-review` — pipeline health, stuck deals, forecasting
- `buildr:account-360` — full picture of one account
- `buildr:activity-logging` — log call/meeting/note with correct entity linking
- `buildr:deal-lifecycle` — create / move stage / win / lose
- `buildr:deal-to-project` — convert won deal into a Buildr project

## Public API documentation

Captured 2026-05-23 (login-gated) and bundled at `references/public-docs.md` inside this skill. Read it when you need:
- Rate-limit numbers (burst 20/10s, hourly 2k, daily 48k) for budgeting heavy reads
- Response envelope shapes (`{item}` for create/get, `{items}` for list)
- The full 52-resource surface documented by Buildr (Envision-MCP exposes all of them via the typed + generic surface above as of PR #726, with the bare `workforce` parent resource — distinct from `workforce_assignments` — the only documented category not yet wired)
- The integration↔docs base-URL discrepancy (`/v1` vs `/api/beta/`) — important if a real endpoint 404s

## Code references (for the curious)

- Integration client: `~/GitHub/Envision-MCP/integrations/buildr.py`
- Resource registry (52 entries): `~/GitHub/Envision-MCP/gateway/strap/buildr_resources.py` (PR #722)
- Pydantic write schemas: `~/GitHub/Envision-MCP/gateway/strap/buildr_schemas.py` (PR #722)
- STRAP dispatch table: `~/GitHub/Envision-MCP/gateway/strap/buildr.py`
- Gateway server composition: `~/GitHub/Envision-MCP/gateway/servers/buildr_server.py`
- Settings (secret names): `~/GitHub/Envision-MCP/config/buildr_settings.py`
- Public API docs (login-gated): https://docs.buildr.com/api-guide/getting-started
