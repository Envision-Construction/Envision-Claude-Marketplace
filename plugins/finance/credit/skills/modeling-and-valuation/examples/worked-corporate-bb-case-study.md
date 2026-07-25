---
last_updated: "2026-03-21"
---

## Worked Case Study: MedTech Holdings — Corporate BB Credit

### Company Profile
- **Issuer:** MedTech Holdings, Inc. (fictitious)
- **Sector:** Healthcare Services — Physician Staffing & Outsourced Services
- **Sponsor:** Summit Capital Partners (fictitious PE firm, Fund VI, 2023 vintage)
- **LTM Revenue:** $1,200M | **LTM EBITDA (Reported):** $270M | **LTM EBITDA (Adjusted):** $250M

### Step 1: EBITDA Normalization

| Line Item | Reported | Adjustment | Analyst EBITDA | Rationale |
|---|---|---|---|---|
| Revenue | $1,200M | — | $1,200M | Organic growth +3% YoY |
| COGS | ($780M) | — | ($780M) | 65% of revenue, stable |
| Gross Profit | $420M | — | $420M | 35% margin |
| SG&A | ($120M) | — | ($120M) | 10% of revenue |
| D&A | ($30M) | +$30M | — | Add back |
| EBITDA (Basic) | $270M | — | $270M | — |
| Stock-Based Comp | — | ($8M) | ($8M) | Real economic cost; recurring |
| Sponsor Mgmt Fee | — | ($4M) | ($4M) | Recurring annual fee |
| "Integration" Costs | — | ($8M) | ($8M) | 3rd consecutive year of "one-time" integration — treat as recurring |
| **Analyst EBITDA** | — | — | **$250M** | $20M haircut to reported EBITDA |

**Key Judgment Call:** Management adds back $20M in "non-recurring" costs — but $8M of integration costs have appeared in each of the last 3 years following tuck-in acquisitions. This is a serial acquirer; integration costs are a cost of doing business, not one-time items. Apply the skepticism principle from `references/ebitda-calculation-the-core-metric.md`.

### Step 2: Leverage & Coverage Ratios

| Metric | Calculation | Result | Rating Implication |
|---|---|---|---|
| Total Debt / EBITDA | $1,375M / $250M | 5.5x | B+ (per `references/rating-agency-thresholds.md`: BB = 3.0-4.5x, B = 4.5-6.5x) |
| Net Debt / EBITDA | ($1,375M - $75M) / $250M | 5.2x | B+ range |
| Secured Debt / EBITDA | $1,100M / $250M | 4.4x | Senior leverage within BB range |
| EBITDA / Interest | $250M / $90M | 2.8x | BB- (threshold: 2.5-3.5x for BB) |
| FCF / Total Debt | $85M / $1,375M | 6.2% | Adequate deleveraging capacity |

**Interpretation:** Headline leverage is B+/BB- territory. Coverage is tight at 2.8x — a 200bps SOFR increase would compress to ~2.2x (see macro sensitivity below). The credit sits at the BB/B boundary; analyst EBITDA (not management EBITDA) puts it firmly in B+ territory.

### Step 3: Scenario Analysis

| Metric | Base Case | Downside (-15% Rev) | Upside (+5% Rev) |
|---|---|---|---|
| Revenue | $1,200M | $1,020M | $1,260M |
| EBITDA | $250M | $190M | $270M |
| EBITDA Margin | 20.8% | 18.6% | 21.4% |
| Total Leverage | 5.5x | 7.2x | 5.1x |
| Interest Coverage | 2.8x | 2.1x | 3.0x |
| FCF | $85M | $25M | $105M |
| Liquidity (Cash + Revolver) | $175M | $115M | $195M |
| Covenant Headroom | 18% | -5% (BREACH) | 25% |

**Downside Scenario Drivers:** 15% revenue decline from: (a) loss of 2 major hospital system clients (top-5 = 35% of revenue), (b) reimbursement rate cuts in Medicaid-heavy states, (c) staffing supply constraints increasing labor costs 5%. Operating leverage is significant — 15% revenue decline produces 24% EBITDA decline due to fixed cost base.

**Key Insight:** The base case has only 18% covenant headroom on the 6.5x max leverage test. The downside case breaches within 2 quarters. This is a credit where the difference between management EBITDA ($270M, 5.1x leverage, 25% headroom) and analyst EBITDA ($250M, 5.5x, 18% headroom) is the difference between comfort and concern.

### Step 4: SOFR Sensitivity

| SOFR Level | Total Interest | Coverage | Covenant Headroom |
|---|---|---|---|
| 3.0% (current) | $90M | 2.8x | 18% |
| 4.0% (+100bps) | $101M | 2.5x | 12% |
| 5.0% (+200bps) | $112M | 2.2x | 5% |
| 6.0% (+300bps) | $123M | 2.0x | -2% (BREACH) |

**Conclusion:** Credit has ~200bps of rate cushion before covenant breach. No interest rate hedging in place. Flag this as a risk in the IC memo.
