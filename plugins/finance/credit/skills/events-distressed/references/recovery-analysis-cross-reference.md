---
last_updated: "2026-03-22"
---

# Recovery Analysis Cross-Reference

A routing guide for recovery analysis across the plugin. Use this document to identify the correct primary skill and broad methodology before running a bottoms-up recovery case.

---

## 1. Identify the Underlying Asset Class

| Underlying Credit | Primary Skill | Core Method |
|---|---|---|
| Corporate borrower | `events-distressed` | Enterprise value or liquidation waterfall through the capital structure |
| Commercial real estate | `cre-analysis-underwriting` | Property or collateral liquidation waterfall |
| Structured finance | `securitization-and-clos` | Tranche-level cash flow waterfall under collateral stress |
| Project finance / infrastructure | `specialized-asset-finance` | Asset and contracted-cash-flow recovery analysis |
| Asset-backed / equipment / aircraft / shipping | `specialized-asset-finance` | Collateral-value and remarketing analysis |

## 2. Corporate Recovery Analysis

**Primary skill:** `events-distressed`

**Use when:**
- The borrower is an operating company
- Recovery depends on enterprise value, legal priority, or restructuring path
- The question involves DIP impact, fulcrum analysis, LMEs, or bankruptcy outcomes

**Primary references:**
- `skills/events-distressed/references/valuation-and-recovery-waterfall.md`
- `skills/events-distressed/references/practical-checklist-for-distressed-credit-analysis.md`
- `references/default-recovery-rates.md`

## 3. CRE Recovery Analysis

**Primary skill:** `cre-analysis-underwriting`

**Use when:**
- Recovery depends on property value and sale or workout mechanics
- Collateral quality, lease rollover, or market liquidity drives the downside
- The instrument is a mortgage, mezzanine loan, or other property-backed exposure

**Primary references:**
- `skills/cre-analysis-underwriting/references/income-capitalization-approach.md`
- `skills/cre-analysis-underwriting/references/sensitivity-analysis-for-cre.md`
- `skills/cre-analysis-underwriting/references/loan-sizing-three-simultaneous-constraints.md`
- `skills/cre-analysis-underwriting/references/property-risk-assessment.md`
- `references/default-recovery-rates.md`

## 4. Structured Finance Recovery Analysis

**Primary skill:** `securitization-and-clos`

**Use when:**
- The question is about a tranche rather than a single borrower
- Cash flow diversion, subordination, or collateral pool behavior determines recovery
- The structure includes waterfalls, coverage tests, or enhancement layers

**Primary references:**
- `skills/securitization-and-clos/references/cash-flow-metrics-and-prepayment.md`
- `skills/securitization-and-clos/references/practical-deal-evaluation-checklist.md`
- `references/default-recovery-rates.md`

## 5. Project Finance Recovery Analysis

**Primary skill:** `specialized-asset-finance`

**Use when:**
- Recovery depends on concession, contracted cash flow, or step-in rights
- The borrower is a project SPV or infrastructure asset
- Asset operation and contract durability matter more than corporate enterprise value

**Primary references:**
- `skills/specialized-asset-finance/references/project-finance-credit-metrics.md`
- `skills/specialized-asset-finance/references/summary-asset-finance-lending-fundamentals.md`
- `references/default-recovery-rates.md`

## 6. Asset Finance Recovery Analysis

**Primary skill:** `specialized-asset-finance`

**Use when:**
- Recovery depends primarily on the resale or redeployment value of movable collateral
- The instrument is secured by equipment, aircraft, vessels, railcars, or similar assets
- Secondary market depth and repossession mechanics drive downside

**Primary references:**
- `skills/specialized-asset-finance/references/summary-asset-finance-lending-fundamentals.md`
- `references/default-recovery-rates.md`

## 7. Shared Guidance

- Use `references/default-recovery-rates.md` for historical benchmark calibration only
- Build a bottoms-up recovery case before comparing to historical medians
- Match the valuation method to the asset and likely resolution path
- Escalate to documentation review whenever legal priority, collateral definition, or guarantees may change the result

## 8. Common Recovery Analysis Mistakes

### Overestimating Recovery

| Mistake | Why It Happens | How to Avoid It |
|---|---|---|
| Using peak earnings or optimistic collateral values | Anchoring to best-case outcomes rather than realizable downside | Use sustainable, downside, or liquidation-consistent assumptions |
| Ignoring estate-level costs and senior claims | Administrative items are easy to overlook early | Deduct fees, priority claims, and process drag before allocating value to funded debt |
| Assuming labels guarantee recovery | "Senior" and "secured" are treated as shortcuts rather than legal analysis | Confirm liens, collateral, guarantees, and structural seniority |
| Applying going-concern multiples to a liquidation scenario | Not all distressed companies can be sold as going concerns | Assess whether a going-concern sale is realistic; if not, use orderly liquidation values |
| Ignoring time value of recovery | Delayed value is treated as equivalent to immediate value | Discount for time, illiquidity, and process uncertainty |
| Forgetting structural subordination | HoldCo debt is structurally subordinated to OpCo debt | Map the legal entity structure before allocating value |

### Underestimating Recovery

| Mistake | Why It Happens | How to Avoid It |
|---|---|---|
| Ignoring post-petition value creation | Assumes today's depressed value persists through resolution | Consider whether a reorganization or sale process can restore earnings power |
| Applying excessive liquidation discounts | Being overly conservative without evidence | Compare the discount to likely sale format, market depth, and collateral quality |
| Ignoring strategic value | Focus remains only on financial buyers or current market conditions | Test whether strategic buyers, sponsors, or incumbent operators could pay more |
| Ignoring guarantees or credit enhancement | Secondary support is overlooked | Review guarantees, reserves, wraps, and insurance before finalizing recovery |

### Process Mistakes

| Mistake | Description |
|---|---|
| Single-point recovery estimate | Always present a range rather than false precision |
| Not stress-testing the key valuation assumption | The main driver may be EV, liquidation discount, timing, or collateral condition; test it explicitly |
| Failure to update recovery estimates as events unfold | Recovery analysis is dynamic and should change with new facts |
| Confusing trading price with recovery value | Secondary market prices embed liquidity and positioning, not just ultimate payout |
| Not coordinating with legal on documentation analysis | Recovery depends on legal rights, not just analytical intuition |

---
