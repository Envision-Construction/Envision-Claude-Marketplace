---
name: Rabbet
description: Rabbet construction lending platform — MCP integration (projects, draws, vendors, funding sources), draw management, budget tracking, retainage calculations, pay applications, browser automation, and Firecrawl integration patterns
triggers:
  - rabbet
  - update rabbet
  - enter in rabbet
  - draw management
  - budget adjustment
  - construction draw
---

<!-- Tool surface last verified: 2026-05-09. If a `mcp__firecrawl__*` call returns "unknown tool", "unknown parameter", or similar shape errors, treat as SKILL STALENESS — surface that to the user, do NOT silently fall back. -->

# Rabbet — Construction Lending Platform

> **IMPORTANT: Rabbet has a full MCP integration via Envision MCP.**
> DO NOT use GraphQL, Firecrawl, or browser automation for standard operations.
> Use the Envision MCP `rabbet()` STRAP tool below. The GraphQL/browser section
> at the bottom is ONLY for advanced mutations not covered by the REST API
> (e.g., `adjustRequestedAmountForLineItem`, `unfreezeDraw`).

## MCP Integration (Primary — Use This First)

**Rabbet is available as a STRAP deferred domain on Envision MCP.** Use this for ALL standard read/write operations (projects, draws, vendors, funding sources, stakeholders, reference data).

### How to Access

Via Envision MCP CodeMode meta-tools:

```
search("rabbet")           → discovers the rabbet() tool
get_schemas("rabbet")      → shows parameter schema
execute("rabbet(resource='projects', action='list')")
```

Or call the tool directly if already discovered:

```
rabbet(resource="projects", action="list")
```

### Available Operations (22 total)

| Resource | Actions | Notes |
|----------|---------|-------|
| **projects** | list, get, get_by_custom_id, upsert | Use project_id or item_id for get |
| **draws** | list, get | list needs project_id; get returns line items, reviews, assessment |
| **vendors** | list, get, get_by_custom_id, upsert | 1500+ vendors in org |
| **funding_sources** | list, list_for_project, set | Paginated; set needs project_id |
| **stakeholders** | list, set | Both need project_id |
| **templates** | list | Project templates with custom field definitions |
| **teams** | list | Organization teams |
| **product_types** | list | Multifamily, Office, Industrial, etc. |
| **regions** | list | Northeast, Midwest, Southeast |

### Examples

```python
# List all projects
rabbet(resource="projects", action="list")

# Get a specific project
rabbet(resource="projects", action="get", item_id="d290f1ee-...")

# List draws for a project
rabbet(resource="draws", action="list", project_id="d290f1ee-...")

# Get draw details (includes line items, reviews, assessment)
rabbet(resource="draws", action="get", item_id="b308e77f-...")

# Create a vendor
rabbet(resource="vendors", action="upsert", params={"data": {"name": "Acme Corp", "type": "CONTRACTOR"}})

# Set funding source on a project
rabbet(resource="funding_sources", action="set", project_id="d290f1ee-...",
       params={"data": {"vendorId": "...", "amount": "$1,000,000", "label": "Construction Loan", "type": "LOAN"}})
```

### Auth

API key auth (token header). Key stored in GCP Secret Manager as `envision-mcp-rabbet-api-key`.
Base URL: `https://dozer.prod.rabbet.com/api`

---

## Browser Automation (Firecrawl CLI) — Advanced Operations

**Use this section ONLY for operations NOT available via the MCP API above** (e.g., editing draw line item amounts, budget adjustments, GraphQL mutations).

For standard reads (projects, draws, vendors, funding sources, stakeholders, reference data), always use the MCP integration above.

### Authentication

Rabbet uses Auth0. Firecrawl `--profile` does NOT persist Auth0 httpOnly cookies across sessions. Each new session requires user login via the interactive live view.

```bash
firecrawl browser launch-session --profile rabbet --ttl 3600
firecrawl browser execute "open https://lift.rabbet.com"
# User must log in via the Interactive Live View URL
```

### What Works (Fully Automatable)

| Action | Method | Notes |
|--------|--------|-------|
| **Text fields** (vendor name, contract #, description, notes) | `fill @ref 'value'` | Works perfectly |
| **Dropdown selections** (vendor picker, line item picker) | `fill @ref 'search'` then `click @option_ref` | Works perfectly |
| **Agreement creation** (text + dropdown fields only) | Full workflow via fill/click | Amount fields show $0 on save |
| **Budget adjustment amounts** | `fill @ref 'amount'` | **WORKS** — key discovery |
| **Budget adjustment line item selection** | `fill` + `click` on option | Works perfectly |
| **Vendor creation** (GraphQL) | `addOrganization` mutation | Works via API |
| **GraphQL read queries** | Bearer token from localStorage | All queries work |
| **Draw line item amounts** (GraphQL) | `adjustRequestedAmountForLineItem` mutation | **WORKS** — but is **incremental** (adds delta), not set. See Draw Amount Entry below. |
| **Unfreeze funded draws** (GraphQL) | `unfreezeDraw(drawId, projectId)` mutation | Works — required to edit a draw marked FUNDED |
| **Create draws** (GraphQL) | `addDraw(name, projectId, submittedDate, ...)` | Works |

### What Does NOT Work

| Action | Why |
|--------|-----|
| **Edit Original Budget** dollar amounts | Formik internal state ignores all programmatic input |
| **Agreement dollar amounts** (creation form) | Same Formik issue — fill changes DOM but not state |
| **Some GraphQL queries** | `project.draw(id) { lineItems }` and similar nested queries return HTTP 500 — use top-level `project { draws } { ... }` instead |
| **Firecrawl profile auth persistence** | Auth0 httpOnly cookies don't save to profiles |
| **Project-level `lineItem(id)` for per-draw amounts** | Returns `$0` even when draw amounts are set; per-draw amounts stored separately |

### Draw Amount Entry — `adjustRequestedAmountForLineItem`

Use this mutation to enter draw line-item amounts (the path that actually works for production data entry):

```graphql
mutation {
  adjustRequestedAmountForLineItem(
    drawId: "<draw_id>",
    lineItemId: "<line_item_id>",
    grossRequestedAmount: 448758.37,    # Currency value
    retainageAmount: 0,
    retainagePercentage: 0,
    setManually: true,
    memo: "Optional free-text memo"
  ) { id grossRequestedAmount }
}
```

**CRITICAL GOTCHA — the mutation INCREMENTS, not SETS.** Each call adds `grossRequestedAmount` to the existing value. To correct an over-allocation, send a **negative delta**:

```graphql
# If a line item is currently $897,516 and target is $448,758:
# Send -448758.37 to subtract the excess.
adjustRequestedAmountForLineItem(... grossRequestedAmount: -448758.37 ...)
```

Recommended pattern: query the line item's current `grossRequestedAmount` first; pass `target - current` as the delta. Or only call once per line item per draw to avoid stacking.

### Funded Draw Editing

Draws marked FUNDED have `isFrozen: true` and reject all edit mutations with:
```
"Target is frozen and cannot be edited" (draw_frozen: true)
```

Unfreeze via GraphQL before editing:
```graphql
mutation { unfreezeDraw(drawId: "<id>", projectId: "<id>") { id state isFrozen } }
```

This returns the draw to `state: STARTED` and `isFrozen: false`. After edits, the draw can be marked funded again with `markDrawComplete` or `fundDraw`.

### Critical: Budget Adjustment Popup

When creating budget adjustments, clicking "Create Adjustment" triggers a **confirmation popup**:

> "Changing the budget may affect your Projection. Would you like to save your changes?"

**You MUST click "Yes" on this popup.** Without it, the adjustment is silently discarded. The full flow:

```bash
# 1. Navigate to draw > Budget tab > Budget Adjustments > Create Adjustment
firecrawl browser execute "fill @description 'description text'"

# 2. For each line item:
firecrawl browser execute "fill @select 'line item search'"
firecrawl browser execute "click @option_ref"          # select from dropdown
firecrawl browser execute "fill @amount_ref '-12345'"   # set amount (negative for source)
firecrawl browser execute "click @addLineItem"          # add next row

# 3. After all line items added:
firecrawl browser execute "click @createAdjustment"
# Wait for popup...
firecrawl browser execute "snapshot -i -c"  # find "Yes" button
firecrawl browser execute "click @yesButton"
```

### Budget Modifications Strategy

**Never edit original budget amounts.** Instead, use budget adjustments within draws:

1. **Budget-neutral reallocations** (scope consolidation, line item moves): Sources sum = Destinations sum, Total change = $0
2. **CO-driven changes** (non-neutral): Creates a positive or negative total, requires funding source update
3. Each adjustment should map to a specific Procore event (CO, budget mod) for audit trail

### GraphQL Read Queries

```bash
# Get auth token from browser
firecrawl browser execute --python '
auth_key = "@@auth0spajs@@::82JeJTVlQrP8wRxhid7UR27vSzF9Gt5k::https://dozer-prod.contractsimply.com/::openid profile email"
raw = await page.evaluate(f"localStorage.getItem(\'{auth_key}\')")
import json; data = json.loads(raw)
print(data["body"]["access_token"])
'

# Query project
curl -s 'https://dozer.prod.rabbet.com/graphql' \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"query":"{ project(id: \"PROJECT_ID\") { id name amount divisions { name lineItems { name budgetAmount } } } }"}'
```

### Key IDs

- GraphQL: `https://dozer.prod.rabbet.com/graphql`
- Auth token key: `@@auth0spajs@@::82JeJTVlQrP8wRxhid7UR27vSzF9Gt5k::https://dozer-prod.contractsimply.com/::openid profile email`
- Org (Prometheus Ventures): `8e3e9f7f-d353-4417-a635-870a7aad00b3`
- Vendor creation: `addOrganization(name, sourceOrganizationId, type: VENDOR)`

---

## Platform Reference

**Login:** https://lift.rabbet.com/ | **Support:** help@rabbet.com

### User Roles
Admin, Organization, Project, Budget, Draw, Document, Reporting permissions. Project roles: Document Reviewer, Draw Reviewer, Signatory (max 1).

### Project Setup
3 budget methods: Excel template upload (new projects only), manual Budget Builder, copy from previous. Budget template: 9 columns (Division Name, Line Item Number, Line Item Name, Summary Line Item, Original Budget Amount, Line Item Type, Line Item Category, Expected Retainage, Master Format Division).

### Draw Lifecycle
Active → Paused → Withdrawn → Rejected → Funded. Workflow: Create → Documents → Draw Summary → Review → Line Items → Budget Adjustments → Funding Sources → Rules → Approvals → Package → Fund.

### Document Types That Affect Draw Amounts
Invoice, Payment Application, Budget (Draw Summary), Retainage Release, 2448, 92464.

### Retainage Formula
`Current Payment Due = Work Completed + Stored Materials - Total Retainage to Date + Previous Period Retainage`

### Budget Adjustments
All adjustments within a draw. Reallocate (neutral, $0 net) or Change Total (non-neutral, update funding sources). Contingency tracked via Line Item Settings.

### Agreements
Types: Addendum, Contract, Work Authorization, Change Orders. Hierarchy: Exposures → PCOs → ECOs. Track costs to agreements (premium).

### Funding Sources
Types: Debt, Equity, Cash, Letter of Credit, Working Capital. Auto Allocate with Move To (priority), Pari Passu (proportional), Uses of Funds (restrict sources).

**Per-draw funding allocation**: Each draw has a Funding Sources tab. Three modes:
1. **Manual entry** — type values into each source's "Requested" field; sum must equal draw total to reduce the difference to $0.
2. **Auto Allocate Funds** (toggle ON) — Rabbet calculates per source based on Project Settings ordering (Move To / Pari Passu).
3. **Uses of Funds** (toggle ON in Project Settings) — restrict which sources can fund which line items. Restricted fields gray out.

Manual edits override auto-allocation. Click **Submit** before navigating away — changes don't auto-save.

**Validation rule**: Total funding source amounts must equal total budget to save the funding source CONFIGURATION (use placeholder source for unknown balances). Per-draw allocation does not require this match.

**GraphQL mutation for per-draw allocation**: `bulkUpdateFundingSources(drawId, fundingSources, projectId)` (bulk update); `disburseFunds(drawId, disbursements, ...)` (actual disbursement event); `upsertFundingSource(...)` for project-level config.

### Loan Paydowns / Repayments (Equity buyback, principal payment)

Rabbet has no separate "loan repayment draw" type. Repayments are tracked via the **"Confirm Outstanding Balances" modal** on each draw's Funding Sources tab:

- **Paid Down to Date**: cumulative repayments to this source so far
- **Paydown This Draw**: amount repaid in the current draw
- **Outstanding Balance**: auto-updates based on the two above

Paydowns appear in the **Ledger sub-tab** with timestamp, user, draw reference, and the source affected. To structure a "repayment draw" (e.g., "Rob Repayment $1.5M from Viva $750K + EMD $750K"):

1. Create the draw shell (`addDraw`)
2. On the draw's Funding Sources tab, click **Adjust Funding Sources**
3. Allocate the SOURCE rows (Viva, EMD) — these contribute funds INTO the draw
4. On the source being repaid (Preferred Equity): enter the "Paydown This Draw" value
5. Confirm Outstanding Balances modal records the repayment in the ledger

The line item allocations for a paydown-only draw can be `$0` across the board, OR they can map to a "Loan Repayment" / "Financing Costs" line item (create via `createLineItem` mutation if one doesn't exist).

### Key Formulas
- Net Requested = Gross - Retainage
- Cost Estimate = MAX(Budget, Gross Requested, Commitments + PCOs + Exposures)
- Balance to Fund = Current Budget - Net Requested
- Total Uncommitted = Current Budget - Total Commitments

### Common Pitfalls
1. **Cannot delete line items with draw or disbursement history** — Rabbet has NO `deleteLineItem` mutation. The UI Edit Original Budget trash icon is disabled when `hasDisbursements: true` or `hasAdjustments: true`. Even setting requested amounts back to $0 does NOT clear the audit trail. Once a line item has been touched by `adjustRequestedAmountForLineItem` or `disburseFunds`, it's permanent. Use `addLineItemComment` to add an audit memo if the line must remain. To truly remove, contact Rabbet support for database-level deletion.
2. Cannot replace PDFs — remove and re-upload
3. Only newest draw can be deleted
4. Retainage % fields are reference only — don't change amounts
5. Multiple pay apps in one draw — retainage doesn't auto-carry
6. Funded draws must be set Active before editing
7. **`disburseFunds` is SET behavior** — replaces existing per-draw funding source allocation. To go from $X to $Y, send $Y as the value (not the delta).
8. **`adjustRequestedAmountForLineItem` is INCREMENTAL** — adds delta. To go from $X to $Y on a line item, send `(Y - X)` as the delta. Re-running with the same `grossRequestedAmount` will DOUBLE the value.
9. **`createBalanceConfirmation` paydown is per-draw delta** — `pendingPaydownAmount` = amount paid down IN THIS DRAW (not cumulative). Multiple confirmations on the same draw are additive.
10. **Paydown cannot exceed disbursed** — if Source has $X disbursed, paydown attempts > $X return HTTP 500.
