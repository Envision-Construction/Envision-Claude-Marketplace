---
title: "Worked Example: CLO Equity Case Study"
last_updated: "2026-03-21"
update_cadence: annually
next_review: "2027-03-21"
type: worked-example
---

# Worked Case Study: Summit CLO IV — CLO Equity Investment Analysis

## Deal Summary

This is a **synthetic teaching example** intended to illustrate CLO equity underwriting workflow, not to provide current market levels or live manager data. Refresh any spread, default, recovery, valuation, or relative-value assumptions against root `references/market-benchmarks.md` and any current deal materials before using this framework in live work.

**Manager:** Ridgeline Credit Management — $8B AUM, 12 CLOs managed across 2015-2025 vintages. Boutique platform with dedicated 18-person credit team and sector-specialist analysts covering healthcare, TMT, and industrials.

**Deal Parameters:**

| Parameter | Detail |
|---|---|
| Deal Name | Summit CLO IV |
| Manager | Ridgeline Credit Management |
| Closing Date | Q3 2025 |
| Reinvestment Period End | Q3 2029 (4 years) |
| Non-Call Period End | Q3 2027 (2 years) |
| Final Stated Maturity | Q3 2037 (12 years) |
| Total Portfolio Par | $400M |
| Collateral Type | Broadly syndicated first lien leveraged loans |
| Warehouse Ramp | 80% ramped at close; full ramp within 90 days |

## Tranche Structure

| Tranche | Rating | Size ($M) | % of Deal | Spread/Coupon | Attachment | Detachment |
|---|---|---|---|---|---|---|
| Class A | Aaa/AAA | $256M | 64.0% | SOFR+135 | 36.0% | 100.0% |
| Class B | Aa2/AA | $40M | 10.0% | SOFR+185 | 26.0% | 36.0% |
| Class C | A2/A | $24M | 6.0% | SOFR+235 | 20.0% | 26.0% |
| Class D | Baa3/BBB- | $20M | 5.0% | SOFR+340 | 15.0% | 20.0% |
| Class E | Ba3/BB- | $16M | 4.0% | SOFR+620 | 11.0% | 15.0% |
| Sub Notes (Equity) | NR | $36M | 9.0% | Residual | 0.0% | 11.0% |
| Income Notes | NR | $8M | 2.0% | Residual | — | — |
| **Total** | | **$400M** | **100%** | | | |

**Key Structural Observations:**

- **Subordination below Class A:** 36.0% — consistent with a senior-first CLO stack where most loss protection sits below the top tranche (see `references/clo-structure-and-economics.md`)
- **Equity cushion (Sub Notes + Income Notes):** 11.0% of deal — provides first-loss protection for rated tranches
- **Blended liability cost:** Weighted average spread on rated tranches = approximately SOFR+195 bps
- **Arbitrage at close:** WAS (SOFR+385) minus blended liability cost (SOFR+195) = 190 bps net interest margin on $400M pool, levered approximately 9x on $44M equity base

## OC/IC Test Calculations

Coverage tests are the guardrails that determine equity's access to cash flow (see `references/clo-structure-and-economics.md`). When tests pass, residual cash flows go to equity. When tests fail, cash is diverted to amortize senior tranches until compliance is restored.

**Current Coverage Test Dashboard:**

| Test | Current Level | Trigger | Cushion | Trend |
|---|---|---|---|---|
| Sr OC (Class A) | 134.2% | 120.0% | +1,420 bps | Stable |
| Sr IC (Class A) | 412.0% | 120.0% | Ample | Stable |
| Mezz OC (Class D) | 115.8% | 108.0% | +780 bps | Slightly declining |
| Mezz IC (Class D) | 285.0% | 105.0% | Ample | Stable |
| Jr OC (Class E) | 111.2% | 104.5% | +670 bps | Slightly declining |

**OC Test Interpretation:**

- Senior OC cushion of +1,420 bps is robust — would require approximately $57M in additional par losses (14.2% of pool) before Class A OC test fails
- Mezzanine OC cushion of +780 bps is adequate but bears monitoring — approximately $31M in incremental par losses would breach the Class D trigger
- Junior OC test at +670 bps is the binding constraint — approximately $27M in additional par losses would trigger cash flow diversion away from equity
- Slight decline in mezzanine and junior OC reflects the two existing defaults ($4.8M par lost) — expected trajectory given early deal seasoning

**Current Pool Metrics:**

| Metric | Current Value | Test/Limit | Cushion |
|---|---|---|---|
| WARF | 2,850 | 3,100 (max) | 250 points |
| WAS | SOFR+385 bps | — | — |
| WAL | 4.2 years | 5.0 years (max) | 0.8 years |
| Diversity Score | 72 | 60 (min) | +12 |
| CCC Bucket | 6.8% | 7.5% (max) | 70 bps |
| Defaults (par) | 1.2% ($4.8M) | — | — |
| Number of Defaults | 2 names | — | — |
| Average Loan Price | 96.5 | — | — |

**Pool Quality Assessment:**

- WARF of 2,850 sits at the BB/B boundary — consistent with broadly syndicated leveraged loan pools (see `references/clo-structure-and-economics.md`)
- CCC bucket at 6.8% is close to the 7.5% limit (70 bps cushion); if additional downgrades occur, excess CCC par is haircut at market value rather than par in OC test calculations, which would accelerate cushion erosion
- Diversity score of 72 indicates a well-diversified portfolio with limited single-name concentration
- Two defaults ($4.8M) represent early-stage seasoning losses; both names are in retail sector (industry-specific stress)

## Manager Evaluation Scorecard

Manager assessment follows the framework in `references/clo-manager-evaluation.md`, evaluating Ridgeline Credit Management across six dimensions.

| Dimension | Assessment | Score |
|---|---|---|
| Default Rate (cumulative) | 2.8% across 12 CLOs vs. 3.5% peer median — below-average defaults indicating strong credit selection | 4/5 |
| Recovery Performance | 68% average recovery vs. 62% market — selective workout approach with dedicated distressed team | 4/5 |
| Par Build Track Record | +0.8% annualized par build vs. +0.5% peer median — consistent value creation through disciplined discount purchasing | 4/5 |
| WARF Management | Conservative positioning — maintains WARF 200-300 points below test limits across all deals; proactive sell discipline on deteriorating credits | 4/5 |
| OC/IC Consistency | Never failed a coverage test across 12 deals and 8 years of managing CLOs — demonstrates strong portfolio quality discipline | 5/5 |
| Equity IRR by Vintage | 2019 vintage: 14.2%, 2021: 16.8%, 2023: 13.5% (early). Returns are solid but slightly below top-performing peers who take more concentrated bets | 3/5 |
| **Overall** | **Top-quartile manager with strong credit selection and exceptional OC/IC track record; slightly below-average equity returns reflect conservative positioning that sacrifices upside for consistency** | **4.0/5** |

**Manager Detail Notes:**

- **AUM & Platform:** $8B AUM across 12 CLOs places Ridgeline in the boutique tier (<$10B). While smaller platforms may have less market access than top-tier managers ($50B+), Ridgeline compensates with focused coverage and consistent execution
- **Investment Process:** Dedicated sector analysts cover healthcare, TMT, and industrials; portfolio turnover of approximately 15% annually (moderate, consistent with par-build strategy)
- **Alignment of Interest:** Ridgeline co-invests 15% of equity in each deal — moderate alignment; subordinated management fee of 20 bps with 12% IRR hurdle provides incentive alignment with equity holders
- **Sell Discipline:** Proactive — Ridgeline historically exits deteriorating credits at 90-95 cents (taking small realized losses) rather than holding through distress. This discipline supports the low cumulative default rate but limits opportunistic recovery upside

## Equity Cash Flow Waterfall

The equity cash flow waterfall follows the strict priority of payments outlined in `references/clo-structure-and-economics.md`.

### Base Case (Annual)

| Waterfall Step | Calculation | Amount |
|---|---|---|
| **Total Pool Interest Income** | $400M x (3.00% SOFR + 3.85% WAS) = $400M x 6.85% | $27.4M |
| Less: Senior Management Fee | $400M x 0.20% | ($0.8M) |
| Less: Trustee/Admin Fees | Fixed | ($0.3M) |
| Less: Class A Interest | $256M x (3.00% + 1.35%) = $256M x 4.35% | ($11.1M) |
| Less: Class B Interest | $40M x (3.00% + 1.85%) = $40M x 4.85% | ($1.9M) |
| Less: Class C Interest | $24M x (3.00% + 2.35%) = $24M x 5.35% | ($1.3M) |
| Less: Class D Interest | $20M x (3.00% + 3.40%) = $20M x 6.40% | ($1.3M) |
| Less: Class E Interest | $16M x (3.00% + 6.20%) = $16M x 9.20% | ($1.5M) |
| Less: Subordinate Management Fee | $400M x 0.20% | ($0.8M) |
| **= Residual to Equity** | $27.4M - $18.7M (rounded) | **$8.7M** |
| **Equity Cash Yield** | $8.7M / $36M Sub Notes | **24.2%** |

**Base Case Observations:**

- 24.2% cash yield is above the reference framework range of 12-18% target IRR because cash yield measures current distributions only, not total return (which incorporates NAV change and terminal value)
- Annualized IRR will be lower than cash yield if NAV declines over time due to defaults
- The 190 bps net arbitrage (WAS minus liability cost) indicates a meaningful asset-liability spread cushion at entry (see `references/clo-structure-and-economics.md`)

### Stress Case (CDR 4%, Recovery 60%)

| Component | Calculation | Impact |
|---|---|---|
| Annual defaults | $400M x 4% CDR | $16.0M par defaulting |
| Loss after recovery | $16.0M x (1 - 60%) | ($6.4M) net loss |
| Reduced performing pool (Year 1) | $400M - $16.0M + $9.6M recovery | ~$384M performing par |
| Reduced interest income | $384M x 6.55% (WAS compression to 355 bps) | $25.2M |
| Total liability costs (unchanged) | Senior mgmt + admin + rated tranche interest + sub mgmt | ~$18.7M |
| **Stressed Residual to Equity** | $25.2M - $18.7M | **~$6.5M** |
| **Stressed Equity Yield** | $6.5M / $36M | **~15.5%** (before OC diversion) |

**OC Test Impact Under Stress:**

- At 4% CDR with 60% recovery, par erodes approximately $6.4M annually
- After Year 1: Jr OC cushion narrows from +670 bps to approximately +450 bps — still passing
- After Year 2: Jr OC cushion narrows to approximately +230 bps — approaching trigger
- After Year 3: Jr OC test likely fails — equity distributions suspended, cash diverted to amortize Class E until par is rebuilt
- **If Mezz OC fails:** Equity distributions fully suspended until par rebuilt — yield drops to 0% until cured. This is the primary downside scenario for CLO equity investors

## IRR Sensitivity Table

IRR projections modeled over the full deal life assuming 4-year reinvestment period, call at Year 5, and entry at 80% of par ($28.8M investment for $36M par equity position).

| CDR | Recovery 55% | Recovery 60% | Recovery 65% | Recovery 70% |
|---|---|---|---|---|
| 2% | 14.8% | 15.5% | 16.2% | 16.8% |
| 3% | 12.1% | 13.2% | 14.1% | 15.0% |
| 4% | 9.2% | 10.8% | 12.0% | 13.1% |
| 6% | 3.5% | 5.8% | 7.8% | 9.5% |
| 8% | -2.1% | 0.8% | 3.2% | 5.4% |

**Sensitivity Interpretation:**

- **Base Case IRR:** 15.5% (2% CDR, 60% recovery) — consistent with a constructive equity case built on healthy arbitrage and preserved test cushion (see `references/clo-structure-and-economics.md`)
- **Break-even scenario:** Approximately 7-8% CDR with 60% recovery yields near-zero IRR — this corresponds to a severe credit cycle (comparable to 2008-2009 stress levels)
- **CDR sensitivity dominates:** Each 1% increase in CDR reduces IRR by approximately 250-350 bps — consistent with high sensitivity noted in the equity CLO framework (300-400 bps per 1% CDR increase)
- **Recovery sensitivity is secondary:** Each 5% improvement in recovery adds approximately 80-120 bps to IRR
- **Stress resilience:** Even at 4% CDR (moderate stress), IRR remains positive across all recovery scenarios — reflecting the favorable entry arbitrage (WAS of 385 bps) and below-par entry price

## NAV Analysis

NAV is calculated per the framework in `references/clo-structure-and-economics.md`: Market Value of Loan Portfolio minus Outstanding Rated Tranches at Par, divided by Equity Investment Amount.

### Current NAV Snapshot

| Component | Par ($M) | Mark | Value ($M) |
|---|---|---|---|
| Performing Loans | $395.2M | 96.5% | $381.4M |
| Defaulted (2 names) | $4.8M | 35.0% | $1.7M |
| **Total Assets** | **$400.0M** | | **$383.1M** |
| Less: Rated Debt at Par | | | ($356.0M) |
| **NAV** | | | **$27.1M** |
| **NAV / Par Equity** | | | **75.3%** |

**NAV Decomposition:**

- Par NAV (all loans at par): ($400.0M - $356.0M) / $36M = 122.2% — portfolio par still exceeds rated liabilities by a healthy margin
- Market NAV: 75.3% reflects the mark-to-market discount on performing loans (avg price 96.5) and the two defaulted names marked at 35 cents
- The gap between par NAV (122%) and market NAV (75%) is driven primarily by the 3.5-point average discount on performing loans — in a par recovery scenario, NAV would accrete meaningfully

### NAV Sensitivity to Default Scenarios

| CDR Scenario | Cumulative Defaults (4yr) | NAV / Par Equity | Implied Equity Multiple |
|---|---|---|---|
| 2% (base) | $32M | ~75% | 8-10x cash flow |
| 4% (moderate stress) | $64M | ~55-60% | 5-7x cash flow |
| 6% (severe stress) | $96M | ~35-40% | 2-4x cash flow |
| 8% (crisis) | $128M | ~15-20% | <2x cash flow |

**Trading Implications:**

- At current NAV of 75.3%, equity trades at approximately 8-10x annualized base case cash flow ($8.7M)
- Entry at 80% of par ($28.8M for $36M par) represents a slight premium to market NAV ($27.1M) — paying 106% of NAV for the cash flow stream
- Under moderate stress (4% CDR), NAV compresses to 55-60% of par, implying potential mark-to-market losses of 15-20 points from current levels

## Vintage Positioning

### 2025 Vintage Context

Summit CLO IV enters a market environment with mixed signals for CLO equity investors:

**Favorable Factors:**

- **Current WAS (385 bps) supports the equity case:** The wider loan spread provides a strong arbitrage cushion at entry, which matters because equity depends on preserving excess spread through the reinvestment period (see `references/clo-structure-and-economics.md`)
- **Liability costs have compressed:** AAA spreads at SOFR+135 are tighter than 2023-2024 levels (SOFR+155-165), improving the net interest margin for new-issue CLOs
- **Manager quality:** Ridgeline's conservative positioning and strong OC track record provide a cushion against late-cycle deterioration

**Unfavorable Factors:**

- **Default rates expected to normalize:** Market consensus projects default rates rising from historically low levels (~1.5% in 2024) to 2-3% through 2026-2027. The 4-year reinvestment period (2025-2029) may coincide with a period of rising defaults
- **Late-cycle positioning:** Economic expansion is mature; if recession occurs during the reinvestment period, the manager will be buying loans from deteriorating credits at potentially distressed prices
- **CCC bucket near limit:** At 6.8% vs. 7.5% limit, further downgrades could trigger CCC excess haircuts in OC tests, amplifying cushion erosion

**Key Risk — Credit Cycle During Reinvestment:**

- If the credit cycle turns during 2025-2029, Ridgeline will be deploying portfolio proceeds into a weaker credit environment
- **Manager mitigation:** Ridgeline's conservative WARF positioning (200-300 points below test limits) provides buffer. Their proactive sell discipline means they will likely exit deteriorating names early, reducing default exposure but potentially booking trading losses
- **Historical analog:** 2018 vintage CLOs faced a similar late-cycle entry and delivered 8-12% IRR — below target but positive. Ridgeline's 2019 vintage (14.2% IRR) outperformed through COVID stress, suggesting resilience

## Relative Value vs. Comparable CLO Equity

| CLO | Manager Tier | Vintage | WAS | Equity Size | Cash Yield | NAV/Par | Entry Price |
|---|---|---|---|---|---|---|---|
| Summit IV | Top Quartile | 2025 | 385 bps | $36M | 24.2% | 75.3% | 80% of par |
| Crestline CLO VII | Top Quartile | 2024 | 375 bps | $32M | 22.5% | 78.1% | 82% of par |
| Harbor Bridge CLO III | 2nd Quartile | 2025 | 395 bps | $28M | 26.0% | 71.2% | 75% of par |
| Oakmont CLO V | 2nd Quartile | 2023 | 355 bps | $40M | 19.8% | 82.5% | 88% of par |

**Relative Value Assessment:**

- **Summit IV vs. Crestline VII:** Both top-quartile managers. Summit IV offers 170 bps higher cash yield (24.2% vs. 22.5%) at a 2-point cheaper entry (80% vs. 82% of par). The wider WAS on Summit IV (+10 bps) and newer vintage (2025 vs. 2024) explain the yield advantage. Summit IV is the better entry point for comparable manager quality
- **Summit IV vs. Harbor Bridge III:** Harbor Bridge offers the highest cash yield (26.0%) and cheapest entry (75% of par), but the 2nd-quartile manager introduces higher dispersion risk. With a weaker manager, the probability of OC test failure and cash flow diversion is meaningfully higher. The 180 bps yield pick-up does not adequately compensate for the manager quality gap (200-400 bps IRR difference between top-quartile and below-average performers, per `references/clo-manager-evaluation.md`)
- **Summit IV vs. Oakmont V:** Oakmont's 2023 vintage has more seasoning and higher NAV (82.5%), but the tighter WAS (355 bps) and higher entry price (88% of par) result in a 440 bps lower cash yield. Oakmont is a safer, lower-return position suitable for conservative allocations
- **Verdict:** Summit IV offers competitive yield (24.2%) with top-quartile manager quality at a fair entry point (80% of par). It represents the preferred position for quality-adjusted returns — delivering near-peer yield to cheaper but riskier alternatives while maintaining the downside protection of a proven manager

## Investment Recommendation Summary

| Factor | Assessment |
|---|---|
| Arbitrage Quality | Favorable — 190 bps net spread at entry, 60th-70th percentile historically |
| Manager Quality | Top quartile — strong credit selection, zero OC test failures, conservative WARF management |
| Entry Valuation | Fair — 80% of par (106% of market NAV); slight premium to NAV justified by cash flow quality |
| Downside Protection | Adequate — Jr OC cushion of +670 bps; break-even at approximately 7-8% CDR |
| Key Risk | Credit cycle turning during reinvestment period (2025-2029); CCC bucket proximity to limit |
| Base Case IRR | 15.5% (2% CDR, 60% recovery) |
| Stress Case IRR | 10.8% (4% CDR, 60% recovery) |
| Relative Value | Preferred vs. comparable CLO equity — best quality-adjusted return in comp set |
