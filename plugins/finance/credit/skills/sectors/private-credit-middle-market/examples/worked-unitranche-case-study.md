---
last_updated: "2026-03-21"
---

# Worked Case Study: CloudServ Solutions — Unitranche FOLO Analysis

All company names and figures in this example are illustrative. Use the case study for underwriting mechanics, not as a source of current market benchmarks.

## 1. Company Profile & Borrower Assessment

### Business Overview

| Item | Detail |
|---|---|
| Company | CloudServ Solutions |
| Sector | B2B Cloud Infrastructure Management (SaaS) |
| Description | Provides cloud infrastructure monitoring, optimization, and cost-management tools to mid-market and enterprise IT departments |
| Revenue (LTM) | $120M |
| Recurring Revenue | 85% of total ($102M ARR) |
| Net Revenue Retention (NRR) | 112% |
| Gross Margin | ~72% |
| Customers | ~650 accounts; top 10 = 18% of ARR |
| Sponsor | Midpoint Capital Partners, Fund III (2024 vintage) |
| Transaction | LBO / Growth Recapitalization |

### EBITDA Bridge & Analyst Adjustments

| Line Item | Amount ($M) | Notes |
|---|---|---|
| Reported EBITDA | $48.0 | Per management / sponsor model |
| Less: Stock-Based Compensation | ($5.0) | Real, recurring economic cost; ~4% of revenue. Treated as operating expense per analyst convention |
| Less: Capitalized Development Costs | ($3.0) | $3M of development spend capitalized on balance sheet; reclassified to operating expense for analytical consistency |
| **Analyst-Adjusted EBITDA** | **$40.0** | Conservative base for credit underwriting |

**Key adjustment rationale:**

- **SBC ($5M):** CloudServ grants equity-based compensation to engineering and senior staff. Unlike one-time transaction bonuses, SBC is a recurring retention cost that directly substitutes for cash compensation. Excluding it overstates true cash earnings capacity. At 4% of revenue, this is moderate for a SaaS business but material to credit metrics.
- **Capitalized development costs ($3M):** Management capitalizes a portion of R&D on the balance sheet and amortizes over 3 years. For credit analysis, these costs are recurring and necessary to maintain the product platform. Reclassifying them to operating expense provides a more conservative (and realistic) EBITDA that reflects ongoing investment requirements.

The $8M gap between Reported EBITDA ($48M) and Analyst EBITDA ($40M) represents a 17% difference — meaningful for leverage calculations (5.0x analyst vs. 4.2x reported). This reinforces the importance of independent EBITDA scrubbing in private credit underwriting.

---

## 2. Unitranche Structure

### Capital Structure Summary

| Tranche | Amount ($M) | Rate | Leverage (Analyst EBITDA) | Maturity |
|---|---|---|---|---|
| Revolving Credit Facility | $25.0 | SOFR + 400 bps | 0.6x (if fully drawn) | 5 years |
| Unitranche — First-Out | $120.0 | SOFR + 425 bps | 3.0x | 7 years |
| Unitranche — Last-Out | $80.0 | SOFR + 800 bps | 5.0x (total through last-out) | 7 years |
| **Total Unitranche** | **$200.0** | **SOFR + 575 bps (blended)** | **5.0x** | **7 years** |
| Sponsor Equity (at cost) | $165.0 | — | — | — |
| **Total Capitalization** | **$365.0** | | | |

### Equity Contribution

- Sponsor equity: $165M (45% of total capitalization)
- Debt-to-total-capitalization: 55%
- Equity cushion beneath debt: $165M, or 0.83x EBITDA coverage per turn of leverage

### FOLO Structure — Agreement Among Lenders (AAL) Key Terms

| AAL Provision | Terms |
|---|---|
| Payment Priority | First-out receives all scheduled interest and principal before last-out in a default/enforcement scenario |
| Voting & Amendments | First-out has consent right over amendments to pricing, maturity, amortization, and collateral release. Last-out can block changes to subordination waterfall |
| Buy-Out Rights | Last-out may purchase first-out position at par + accrued after an event of default, within 30-day window |
| Enforcement | First-out controls remedies for first 180 days post-EOD. Last-out may direct enforcement thereafter if first-out has not acted |
| Adequate Protection | First-out entitled to adequate protection payments in bankruptcy before last-out |

### Blended Spread Verification

Blended coupon = (60% x 425 bps) + (40% x 800 bps) = 255 + 320 = **575 bps**

With SOFR at 3.00%, all-in blended coupon = **8.75%**

---

## 3. Covenant Package Analysis

### Financial Covenants

| Covenant | Threshold | Current | Headroom | Test Frequency |
|---|---|---|---|---|
| Maximum Total Leverage | 6.0x | 5.0x | 17% ($8M EBITDA decline before breach) | Quarterly |
| Minimum Fixed Charge Coverage Ratio | 1.10x | 1.35x | 19% | Quarterly |
| EBITDA Addback Cap | 15% of EBITDA | ~10% utilized | 5 percentage points | Per calculation |

### Leverage Headroom Calculation

- Current EBITDA: $40.0M
- Maximum EBITDA decline before covenant breach: $40.0M - ($200M / 6.0x) = $40.0M - $33.3M = **$6.7M (16.7% decline)**
- This provides roughly 2-3 quarters of deterioration runway assuming gradual decline

### Covenant Package Assessment vs. Market

| Feature | CloudServ Deal | BSL Market Typical | Assessment |
|---|---|---|---|
| Maintenance covenants | Yes (leverage + FCCR) | Rare (cov-lite) | Stronger — provides early warning |
| EBITDA addback cap | 15% | 25-30% (or uncapped) | Tighter — limits creative adjustments |
| Financial reporting | Quarterly + monthly revenue flash | Quarterly only | Better visibility |
| Board observer rights | Yes (first-out lender) | No | Enhanced governance |
| Restricted payments | Blocked until <4.0x leverage | Typically permitted baskets | More protective |
| Equity cure rights | 2 cures over life, max $5M each | Varies | Standard for private credit |

### Information Rights & Monitoring

- **Monthly:** Revenue flash report (ARR, NRR, churn, new bookings)
- **Quarterly:** Full financial statements (within 45 days), compliance certificate, management discussion
- **Annually:** Audited financials (within 90 days), annual budget/operating plan, insurance certificates
- **Ad hoc:** Material contract changes, management departures, litigation updates
- **Board observer:** First-out lender representative attends board meetings (observer, non-voting)

---

## 4. Performing Waterfall

### Annual Interest Allocation (Performing Scenario)

Assumes SOFR = 3.00%, no default, revolver undrawn.

| Step | Description | Amount ($M) |
|---|---|---|
| 1 | Gross interest — First-Out: $120M x (3.00% + 4.25%) = $120M x 7.25% | $8.70 |
| 2 | Gross interest — Last-Out: $80M x (3.00% + 8.00%) = $80M x 11.00% | $8.80 |
| 3 | **Total unitranche interest** | **$17.50** |
| 4 | Administrative agent fee (0.025% of total commitments) | $0.06 |
| 5 | Unused revolver commitment fee: $25M x 0.50% | $0.13 |
| 6 | **Total annual debt service (interest only, no amortization)** | **$17.69** |

### Quarterly Cash Flow Waterfall (Performing)

| Priority | Payment | Quarterly Amount ($M) |
|---|---|---|
| 1 | Administrative agent fees | $0.01 |
| 2 | Revolver interest (if drawn) | $0.00 |
| 3 | Revolver commitment fee | $0.03 |
| 4 | First-Out interest | $2.18 |
| 5 | Last-Out interest | $2.20 |
| 6 | Mandatory amortization (1.0% annual of unitranche) | $0.50 |
| 7 | Excess cash flow sweep (50% of ECF if leverage >4.5x) | Variable |
| | **Total quarterly debt service** | **$4.92 + ECF sweep** |

### Interest Coverage & Debt Service

| Metric | Value |
|---|---|
| EBITDA / Total Interest | $40.0M / $17.5M = **2.29x** |
| EBITDA / Total Debt Service (incl. 1% amort) | $40.0M / $19.5M = **2.05x** |
| Free Cash Flow (pre-sweep) estimate | $40.0M - $17.7M debt service - $5.0M capex - $3.5M taxes = **$13.8M** |
| ECF sweep (50% if leverage >4.5x) | ~$6.9M applied to principal |

---

## 5. Stress Waterfall (Recovery Scenario)

### Scenario Assumptions

| Assumption | Value | Rationale |
|---|---|---|
| Stress EBITDA | $24.0M (40% decline) | Severe customer churn + competitive displacement |
| Stress EV Multiple | 6.25x (vs. 9.1x at entry) | Multiple compression in distressed SaaS environment |
| Gross Enterprise Value | $150.0M | $24M x 6.25x |
| Restructuring / Transaction Costs | ($5.0M) | Legal, advisory, DIP fees |
| Net Distributable Value | $145.0M | |
| Revolver (drawn in stress) | $10.0M | Partial draw to fund operating shortfall |

### Recovery Waterfall

| Priority | Claim ($M) | Available ($M) | Recovery ($M) | Recovery Rate |
|---|---|---|---|---|
| 1. Administrative & Priority Claims | $5.0 | $150.0 | $5.0 | 100.0% |
| 2. Revolver | $10.0 | $145.0 | $10.0 | 100.0% |
| 3. Unitranche — First-Out | $120.0 | $135.0 | $120.0 | **100.0%** |
| 4. Unitranche — Last-Out | $80.0 | $15.0 | $15.0 | **18.75%** |
| 5. Sponsor Equity | $165.0 | $0.0 | $0.0 | 0.0% |
| **Total** | **$380.0** | | **$150.0** | |

### Recovery Analysis

The stress scenario reveals the fundamental risk asymmetry in FOLO structures:

- **First-out ($120M):** Full recovery (100%). The 3.0x attachment point and payment priority provide substantial protection. Even in a severe stress (40% EBITDA decline + multiple compression), first-out recovers in full.
- **Last-out ($80M):** Recovery of only $15M (18.75%). The last-out absorbs nearly all loss after equity is eliminated. Despite earning SOFR+800 (375 bps premium over first-out), the last-out bears dramatically disproportionate downside.
- **Loss severity differential:** First-out LGD = 0%; Last-out LGD = 81.25%. This 81-point gap in loss severity underscores why last-out pricing must reflect subordination risk, not just credit risk.

### Sensitivity: Recovery Under Varying Enterprise Values

| Stress EV ($M) | First-Out Recovery | Last-Out Recovery | Last-Out $ Recovery |
|---|---|---|---|
| $200 (no decline) | 100% | 81.25% | $65.0M |
| $175 | 100% | 50.0% | $40.0M |
| $150 (base stress) | 100% | 18.75% | $15.0M |
| $135 | 100% | 0.0% | $0.0M |
| $120 | 91.7% | 0.0% | $0.0M |

**Breakeven EV for last-out full recovery:** ~$215M (requires no material value destruction)

**Breakeven EV for first-out impairment:** $135M (requires ~63% value decline from entry EV of $365M)

---

## 6. Sponsor Assessment Scorecard

### Midpoint Capital Partners — Fund III

| Dimension | Assessment | Score (1-5) |
|---|---|---|
| Track Record | Fund I: 2.1x MOIC, Fund II: 1.8x (early); 2 exits from 8 portfolio companies | 3 |
| Equity Contribution | 45% equity / 55% debt; $165M sponsor equity at cost | 4 |
| Operating Model | Operational value-add focus; dedicated operating partners for SaaS portfolio companies | 4 |
| Behavioral Patterns | No dividend recaps to date; moderate add-on pace (1-2 per year); constructive amendment history | 4 |
| Alignment | Management rollover 8% of equity; earn-out tied to EBITDA targets | 3 |
| **Overall** | **Supportive sponsor with adequate track record; mid-market fund size limits follow-on capacity** | **3.6** |

### Detailed Dimension Commentary

**Track Record (3/5):**
Fund I returned 2.1x gross MOIC — solid but not top-quartile for vintage. Fund II is early (1.8x, partially realized). Only 2 full exits from 8 investments limits statistical significance. No realized losses to date, but portfolio is young. The firm has invested in technology-enabled services for 3 funds, demonstrating sector familiarity.

**Equity Contribution (4/5):**
At 45% equity, the sponsor has meaningful skin in the game. The $165M equity check (from a $500M fund) represents a ~33% fund concentration, signaling high conviction but also limiting follow-on capacity. Day-one equity cushion of $165M beneath $200M of debt is adequate for a 5.0x deal.

**Operating Model (4/5):**
Midpoint employs 3 dedicated operating partners across its portfolio, including one with SaaS operations background (former COO of a mid-market SaaS platform). Post-acquisition playbook includes sales optimization, customer success buildout, and pricing strategy — all relevant to CloudServ. Track record of improving margins by 200-400 bps in prior SaaS investments.

**Behavioral Patterns (4/5):**
No dividend recapitalizations across any fund — a positive signal for lenders. Add-on acquisition pace is measured (1-2 per year per platform), with demonstrated willingness to contribute incremental equity for acquisitions (50/50 debt-equity mix on tuck-ins). During a prior covenant pressure situation (Fund I, 2020), Midpoint proactively engaged lenders and contributed a $5M equity cure — constructive behavior.

**Alignment (3/5):**
Management rollover at 8% of equity is below the 10-15% range preferred by lenders. Earn-out tied to EBITDA targets partially mitigates this. CEO and CFO have 3-year employment agreements with non-competes. Key-man risk is moderate: CTO is a co-founder with deep product knowledge but no equity rollover.

### Sponsor Risk Factors

- **Fund concentration:** CloudServ is ~33% of Fund III. If the investment underperforms, the sponsor may lack capacity for follow-on equity support without cross-fund considerations.
- **Limited exit track record:** Only 2 realized exits across all funds. Ability to execute a successful exit (and thereby protect credit) is less proven than established firms.
- **Fund life:** Fund III is 2024 vintage with typical 5+1+1 structure. Hold period pressure could emerge by 2029-2030, potentially accelerating exit timeline and influencing operating decisions.

---

## 7. Post-Close Monitoring Framework

### Thesis-Kill Triggers Mapped to Escalation Tiers

| Tier | Trigger | Threshold | Action |
|---|---|---|---|
| **Tier 1: Analyst Watch** | NRR decline | NRR drops below 105% (vs. 112% at close) | Add to internal watchlist; increase monitoring frequency to bi-weekly; prepare updated sensitivity analysis |
| **Tier 1: Analyst Watch** | Revenue growth deceleration | Revenue growth <5% YoY (vs. ~15% at close) | Review customer concentration; assess competitive dynamics; update revenue model |
| **Tier 2: Team Review** | EBITDA decline vs. model | EBITDA decline >10% vs. underwriting case | Formal team discussion; re-run covenant compliance projections; engage sponsor for management call |
| **Tier 2: Team Review** | Leverage deterioration | Total leverage exceeds 5.5x (approaching 6.0x covenant) | Prepare amendment/waiver analysis; assess cure options; review AAL buy-out mechanics |
| **Tier 2: Team Review** | Amendment request | Sponsor/borrower requests covenant relief | Assess request merit; model concession scenarios; coordinate first-out / last-out response per AAL |
| **Tier 3: IC Notification** | Severe EBITDA decline | EBITDA decline >20% vs. underwriting case | Formal IC notification memo; updated recovery analysis; engage legal counsel for documentation review |
| **Tier 3: IC Notification** | Liquidity stress | Liquidity runway <6 months (cash + revolver availability) | Assess DIP financing options; review first-out adequate protection rights; model liquidation scenarios |
| **Tier 3: IC Notification** | Key management departure | CEO or CFO departure | Assess succession plan; evaluate sponsor's ability to recruit replacement; review key-man provisions |
| **Tier 4: Emergency IC** | Covenant breach | Actual or anticipated covenant violation | Activate enforcement rights (180-day first-out control period per AAL); evaluate forbearance vs. acceleration |
| **Tier 4: Emergency IC** | Payment default | Missed interest or principal payment | Immediately assess last-out buy-out election; coordinate legal strategy; model recovery scenarios |
| **Tier 4: Emergency IC** | Sponsor distress | Sponsor fund enters wind-down or GP faces fundraising failure | Assess impact on portfolio company support; evaluate co-investor or secondary sale options |

### Monitoring Cadence

| Frequency | Deliverable | Key Metrics Tracked |
|---|---|---|
| Monthly | Revenue flash review | ARR, NRR, logo churn, gross bookings, pipeline |
| Quarterly | Full credit review | EBITDA vs. model, leverage, coverage, liquidity, covenant compliance |
| Quarterly | Covenant compliance certificate review | Verify calculations, addback utilization, restricted payment capacity |
| Semi-Annually | Sponsor / management call | Strategic update, competitive landscape, M&A pipeline, capital allocation plans |
| Annually | Thesis re-validation | Reassess original investment thesis; update base/downside/upside scenarios; review sponsor fund lifecycle |
| Ad Hoc | Event-driven review | Material contract loss, acquisition announcement, management change, market dislocation |

### SaaS-Specific Monitoring Metrics

Given CloudServ's SaaS business model, standard credit metrics should be supplemented with software-specific KPIs:

| Metric | At Close | Watch Level | Concern Level |
|---|---|---|---|
| Net Revenue Retention | 112% | <105% | <95% |
| Gross Revenue Retention | 92% | <88% | <82% |
| Logo Churn (annual) | 8% | >12% | >18% |
| LTV/CAC Ratio | 4.5x | <3.0x | <2.0x |
| Rule of 40 (growth + margin) | 48 | <35 | <25 |
| ARR per Employee | $185K | <$150K | <$120K |

### Cross-Skill References

- For escalation governance procedures and watchlist management, reference the `surveillance-monitoring` skill
- For covenant amendment and waiver analysis frameworks, reference the `debt-structure-covenants` skill
- For updated recovery modeling in stress scenarios, reference the `modeling-and-valuation` skill
- For sponsor behavioral assessment updates, reference `references/sponsor-vs-non-sponsor-underwriting.md`
