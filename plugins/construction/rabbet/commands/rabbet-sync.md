---
name: rabbet-sync
description: Automated Procore→Rabbet synchronization — pulls budget, commitments, and pay apps from Procore via Envision-MCP, diffs against current Rabbet state, and executes updates via browser automation
triggers:
  - sync procore to rabbet
  - rabbet sync
  - procore rabbet sync
  - update rabbet from procore
  - sync rabbet
---

Synchronize Procore project data into Rabbet for project: $ARGUMENTS

**Requires**: Procore project ID (numeric, e.g. `598134326184785`). If a project name is given instead, resolve it first via `procore_get_projects`.

**Read the wiring spec first**: `docs/specs/procore-to-rabbet-wiring.md` — this defines the authoritative field mapping. If the file does not exist yet, reference the mapping tables in `.planning/plans/sweetwater-rabbet-budget-wiring.md`.

---

## Phase 0 — Resolve Project IDs

1. If input is a project name (not numeric), call `procore_get_projects` and extract the numeric project ID.
2. Query Rabbet GraphQL for the matching project UUID:

```bash
curl -s 'https://dozer.prod.rabbet.com/graphql' \
  -H "Authorization: Bearer $RABBET_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"query":"{ projects { id name } }"}'
```

Match by project name (fuzzy). Store as `PROCORE_ID` and `RABBET_PROJECT_ID`.

---

## Phase 1 — Pull Procore State

Run these three MCP calls in parallel (they are independent):

```
procore_get_budget(project_id: PROCORE_ID)
procore_get_commitments(project_id: PROCORE_ID)
procore_get_pay_applications(project_id: PROCORE_ID)
```

**MCP tool notes:**
- `procore_get_budget` → returns line items with `wbs_code`, `original_amount`, `revised_amount`, `cost_type`
- `procore_get_commitments` → returns subcontracts with `number`, `vendor`, `status`, `approved_amount`, `change_order_packages`
- `procore_get_pay_applications` → returns pay apps with `number`, `period_amount`, `status`

Organize results into three dictionaries keyed by cost code / contract number / pay app number.

---

## Phase 2 — Pull Rabbet State (GraphQL)

**Auth token**: Retrieve from browser localStorage after user logs in (see Phase 3 for login flow). Alternatively, if a session is already open, extract the token:

```bash
firecrawl browser execute --python '
auth_key = "@@auth0spajs@@::82JeJTVlQrP8wRxhid7UR27vSzF9Gt5k::https://dozer-prod.contractsimply.com/::openid profile email"
raw = await page.evaluate(f"localStorage.getItem(\'{auth_key}\')")
import json; data = json.loads(raw)
print(data["body"]["access_token"])
'
```

**GraphQL query — full project snapshot:**

```graphql
{
  project(id: "RABBET_PROJECT_ID") {
    id
    name
    amount
    originalAmount
    divisions {
      id
      name
      lineItems {
        id
        name
        budgetAmount
        originalAmount
        committedAmount
      }
    }
    agreements {
      id
      number
      vendor { name }
      contractAmount
      status
    }
    draws {
      id
      name
      status
      budgetAdjustments {
        id
        description
        amount
        lineItems { lineItemId amount }
      }
    }
  }
}
```

Store snapshot as `rabbet_state`.

---

## Phase 3 — Browser Authentication (Required Each Session)

**CRITICAL: Auth0 httpOnly cookies do NOT persist in Firecrawl profiles. User login is required every session.**

```bash
firecrawl browser launch-session --profile rabbet --ttl 3600
firecrawl browser execute "open https://lift.rabbet.com"
```

Provide the user with the Interactive Live View URL and say:
> "Please log into Rabbet in the Interactive Live View. Press Enter here when the dashboard is visible."

Wait for user confirmation before proceeding.

After login, extract the auth token (see Phase 2 above) and store as `RABBET_TOKEN` for all subsequent GraphQL calls.

---

## Phase 4 — Generate Diff

Apply the wiring spec field mappings to produce three diff lists:

### 4a. Budget Line Item Diff

For each Procore cost code, map to the Rabbet division + line item using the wiring spec. Key name mappings (from `.planning/plans/sweetwater-rabbet-budget-wiring.md`):

| Procore Cost Code | Procore Name | Rabbet Division | Rabbet Line Item |
|---|---|---|---|
| 31-20-01.SUB | Earth Moving | 31 - Earthwork | Sitework Subcontractor |
| 50-*.OTH | Construction Fees | 50 - Fees | Profit / Fee.Other |
| All 01-* | By name | 01 - General Conditions | Match by name |

For each line item where `procore.revised_amount != rabbet.budgetAmount`:
- Flag as `BUDGET_DRIFT` with delta amount
- Note: budget amounts are NOT directly editable (Formik blocks). Drift requires a **budget adjustment** in a draw.

### 4b. Agreement Diff

For each Procore commitment, find the matching Rabbet agreement by number (`SC-001`, `SC-002`, etc.):

- `procore.approved_amount != rabbet.contractAmount` → flag as `AGREEMENT_AMOUNT_DRIFT`
- Missing in Rabbet → flag as `AGREEMENT_MISSING`
- `procore.change_order_packages` not reflected → flag as `CO_MISSING`

### 4c. Pay Application Diff

For each Procore pay app, check if a corresponding draw document exists in Rabbet:
- Not found → flag as `PAY_APP_NOT_UPLOADED`
- Found but amounts differ → flag as `PAY_APP_AMOUNT_DRIFT`

**Print the full diff summary before executing any writes.** Ask for user confirmation if any single change exceeds $50,000.

---

## Phase 5 — Execute Updates (Browser Automation)

**All writes go through Firecrawl browser automation. GraphQL mutations are blocked (HTTP 500).**

### 5a. Fix Agreement Amounts (Changes Column)

For each `AGREEMENT_AMOUNT_DRIFT`:

```bash
# Navigate to agreement
firecrawl browser execute "open https://lift.rabbet.com/projects/RABBET_PROJECT_ID/agreements"
firecrawl browser execute "snapshot -i -c"
# Find and click the agreement row
firecrawl browser execute "click @agreement_SC00X"

# Click the Changes column cell for the relevant line item
firecrawl browser execute "snapshot -i -c"
firecrawl browser execute "click @changes_cell_ref"

# Fill the amount (Changes column accepts programmatic fill)
firecrawl browser execute "fill @amount_input 'AMOUNT'"
firecrawl browser execute "press Tab"

# Save
firecrawl browser execute "click @save_button"
firecrawl browser execute "snapshot -i -c"  # verify saved
```

Verify after each agreement: re-query GraphQL and confirm `contractAmount` matches Procore.

### 5b. Create Budget Adjustments for Drift

For each `BUDGET_DRIFT`, create a budget adjustment within the active draw:

```bash
# Navigate to the draw's Budget tab
firecrawl browser execute "open https://lift.rabbet.com/projects/RABBET_PROJECT_ID/draws/DRAW_ID/budget"
firecrawl browser execute "snapshot -i -c"
firecrawl browser execute "click @budget_adjustments_tab"
firecrawl browser execute "click @create_adjustment_button"

# Fill description
firecrawl browser execute "fill @description_input 'Procore sync: [cost_code] delta as of [date]'"

# Add line item (may repeat for multi-line adjustments)
firecrawl browser execute "fill @line_item_select '[search term]'"
firecrawl browser execute "click @line_item_option"
firecrawl browser execute "fill @amount_input '[delta_amount]'"

# Submit
firecrawl browser execute "click @create_adjustment"

# CRITICAL: Handle confirmation popup
firecrawl browser execute "snapshot -i -c"
# Find "Yes" button in popup "Changing the budget may affect your Projection..."
firecrawl browser execute "click @yes_button"
```

**Budget adjustment rules:**
- Reallocations (no net change to total): sources are negative, destinations are positive, must sum to zero
- CO-driven additions (non-neutral): update funding sources after to balance
- Use Procore event as description for audit trail (e.g., "PCO-001: Meredith Extended GC +$307,425")

### 5c. Upload Pay Applications

For each `PAY_APP_NOT_UPLOADED`:

```
Notify user: "Pay app [number] from Procore is not in Rabbet. Please upload the PDF manually via:
  Rabbet > Project > Draws > [draw name] > Documents > Upload > Payment Application
  Then map to line item: [line_item_name]"
```

Pay app uploads are not automatable without the PDF — flag for manual follow-up.

---

## Phase 6 — Verification

Run a post-sync GraphQL query (same as Phase 2 query) and compare against expected values:

```bash
curl -s 'https://dozer.prod.rabbet.com/graphql' \
  -H "Authorization: Bearer $RABBET_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"query":"{ project(id: \"RABBET_PROJECT_ID\") { amount originalAmount agreements { number contractAmount } } }"}'
```

Print a verification table:

```
SYNC VERIFICATION — [Project Name] — [Date]
─────────────────────────────────────────────────────────────────
AGREEMENTS
  SC-001  Expected: $X,XXX,XXX  Actual: $X,XXX,XXX  [OK / DRIFT]
  SC-002  Expected: $XX,XXX     Actual: $XX,XXX     [OK / DRIFT]
  ...

BUDGET ADJUSTMENTS CREATED: [N]
  [description] → [line_item]: $[amount]

PAY APPS PENDING MANUAL UPLOAD: [N]
  [number] — [period] — $[amount]

REMAINING DRIFT:
  [any items not yet resolved]
─────────────────────────────────────────────────────────────────
STATUS: [CLEAN / PARTIAL / FAILED]
```

If any `DRIFT` remains, re-run Phase 5 for those items only (up to 2 retries). After 2 failed retries on the same item, stop and report the issue with the raw GraphQL response.

---

## Error Handling

| Error | Action |
|---|---|
| Procore MCP returns empty budget | Verify project ID and Procore connection. Try `procore_get_projects` to confirm access. |
| Rabbet GraphQL 401 | Token expired — repeat Phase 3 login flow |
| Rabbet GraphQL 500 on mutation | Expected — all writes must go through browser UI, not GraphQL mutations |
| Firecrawl browser session expired | Re-launch session: `firecrawl browser launch-session --profile rabbet --ttl 3600` |
| Agreement amount won't save (Formik revert) | Use Changes column (NOT the contract amount field directly). Changes column bypasses Formik. |
| Budget adjustment popup not found | Take a snapshot first; the popup title contains "Changing the budget" — click "Yes" |
| Line item not found in Rabbet | Check wiring spec for name aliases (e.g., "Earth Moving" → "Sitework Subcontractor") |

---

## Constraints and Known Limitations

- **Rabbet auth**: Auth0 httpOnly cookies do not persist in Firecrawl profiles. User must log in interactively each session.
- **GraphQL mutations**: All return HTTP 500. Every write goes through browser UI automation.
- **Original budget**: Not editable via automation (Formik state). Use budget adjustments within draws to reconcile deltas.
- **Agreement amounts**: The contract amount field is blocked. Use the **Changes column** — it accepts `fill()` and persists correctly.
- **Pay applications**: Cannot be uploaded without the PDF file. Flag for manual upload.
- **Funding sources**: Not present in Procore. Rabbet-only. Do not overwrite funding source data.
- **Divisions not in Procore**: Land Acquisition, Development Costs, 26-Electrical — skip during budget diff, do not zero these out.

---

## Reference

- Wiring spec: `docs/specs/procore-to-rabbet-wiring.md`
- Plan with full mapping tables: `.planning/plans/sweetwater-rabbet-budget-wiring.md`
- Rabbet skill (browser automation patterns): `/rabbet`
- GraphQL endpoint: `https://dozer.prod.rabbet.com/graphql`
- Auth token localStorage key: `@@auth0spajs@@::82JeJTVlQrP8wRxhid7UR27vSzF9Gt5k::https://dozer-prod.contractsimply.com/::openid profile email`
- Org ID (Prometheus Ventures): `8e3e9f7f-d353-4417-a635-870a7aad00b3`
