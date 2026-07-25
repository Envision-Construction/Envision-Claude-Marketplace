---
last_updated: "2026-03-22"
---

# Worked Example: Position Sizing — Apex Industrial Services

This worked example is illustrative. Recalculate all live limits, cushions, and benchmark inputs from the root reference files before using the workflow in a real portfolio decision.

## Credit Summary

| Field | Detail |
|---|---|
| Issuer | Apex Industrial Services, Inc. |
| Instrument | First Lien Term Loan B |
| Rating | B+ / B1 (S&P / Moody's) |
| Spread | SOFR + 400 bps |
| Leverage | 4.8x Total / 4.8x Senior Secured |
| EBITDA | $95M LTM |
| Revenue | $680M LTM |
| Sector | Industrials — Environmental & Facility Services |
| Sponsor | Ridgeline Partners (Fund III, 2023 vintage) |
| Maturity | March 2031 |
| Current Price | 99.25 |

Apex provides environmental remediation and industrial maintenance services to petrochemical and manufacturing clients. Revenue is ~65% recurring (multi-year MSAs), with moderate cyclicality tied to industrial production volumes.

## Fund Context

| Parameter | Value |
|---|---|
| Fund Vehicle | $2.0B CLO (Ridgeview CLO 2024-I) |
| Reinvestment Period End | June 2029 |
| Current NAV | $2.0B par |
| Current CCC Bucket | 5.2% ($104M) vs. 7.5% limit ($150M) |
| Current WAL | 4.3 years vs. 8.0 year max |
| Weighted Average Spread | SOFR + 385 bps vs. SOFR + 350 bps floor |

## Base Position Sizing

**Conviction Level**: Medium — Solid recurring revenue base with manageable leverage, but sector cyclicality and untested sponsor limit conviction.

| Sizing Input | Calculation |
|---|---|
| Target allocation (medium conviction) | 1.0%–1.5% of AUM |
| Maximum notional at 1.5% | $30M |
| Proposed notional | $25M (1.25% of AUM) |

Starting point: $25M based on medium conviction and B+ rating.

## Fund Vehicle Constraints Check

### CLO OC Test Impact

| Test | Current Level | Post-Trade Level | Trigger | Cushion |
|---|---|---|---|---|
| Senior OC (AAA) | 128.5% | 128.4% | 120.0% | 8.4% — Pass |
| Mezzanine OC (BBB) | 112.3% | 112.2% | 108.0% | 4.2% — Pass |
| Junior OC (BB) | 106.8% | 106.7% | 104.5% | 2.2% — Pass |

$25M B+ asset has minimal OC test impact. No haircut applied (B+ is above CCC threshold).

### CCC Bucket Check

| Metric | Value |
|---|---|
| Current CCC-rated par | $104M (5.2%) |
| CCC limit | $150M (7.5%) |
| Apex rating | B+ (not CCC) |
| Headroom | $46M — no CCC constraint |

If Apex were downgraded to CCC+, the $25M position would bring the CCC bucket to $129M (6.5%), still within the 7.5% limit. Downgrade buffer is adequate.

### Single-Obligor Test

| Metric | Value |
|---|---|
| Single-obligor limit | 2.0% of par = $40M |
| Proposed position | $25M (1.25%) — Pass |

### WAL Test Impact

Adding a March 2031 maturity ($25M) increases portfolio WAL from 4.30 to approximately 4.33 years, well within the 8.0-year maximum.

## Concentration Analysis

| Concentration Dimension | Current | Post-Trade | Limit | Status |
|---|---|---|---|---|
| Industrial sector | 11.5% ($230M) | 12.8% ($255M) | 15.0% soft cap | Pass (2.2% headroom) |
| Single-name (Apex) | 0.0% | 1.25% ($25M) | 2.0% hard cap | Pass (0.75% headroom) |
| B-rated bucket | 27.5% ($550M) | 28.8% ($575M) | 35.0% limit | Pass (6.2% headroom) |
| Sponsor (Ridgeline) | 1.0% ($20M) | 2.3% ($45M) | 5.0% soft cap | Pass (2.7% headroom) |
| Top 10 exposure | 14.2% | 15.5% | 20.0% guideline | Pass |

No concentration limit is binding. Industrial sector approaching soft cap warrants monitoring.

## Correlation Assessment

### Existing Overlapping Exposures

| Position | Overlap Type | Size |
|---|---|---|
| CleanTech Environmental ($20M) | Same sub-sector (environmental services) | Direct sector |
| Atlas Facility Mgmt ($15M) | Adjacent sub-sector (facility services) | Indirect sector |
| ProServ Industrial ($18M) | Adjacent sub-sector (industrial maintenance) | Indirect sector |
| Ridgeline Portfolio Co ($20M) | Same PE sponsor (Ridgeline Fund III) | Sponsor overlap |

### Correlation Adjustment Calculation

| Factor | Weight | Overlap | Contribution |
|---|---|---|---|
| Sector overlap (3 names, 15% of sector) | 0.50 | 0.15 | 0.075 |
| Sponsor overlap (1 name, 5% overlap) | 0.30 | 0.05 | 0.015 |
| Geographic overlap | 0.20 | 0.00 | 0.000 |
| **Total correlation adjustment** | | | **0.090** |

**Adjusted position size**: $25M x (1 - 0.09) = $22.75M, rounded to **$23M**

Rationale: Three existing industrial services/environmental names create moderate sector correlation. Single sponsor overlap adds marginal concentration risk. Reducing by $2M (to $23M) appropriately compensates for correlated downside.

## Stress Test Analysis

### Position-Level Stress

| Scenario | EBITDA Shock | Spread Widening | Price Impact | Position Loss |
|---|---|---|---|---|
| Base case | — | — | 99.25 | — |
| Moderate stress | -15% | +350 bps | 91.0 | -$1.9M (8.3%) |
| Severe stress | -25% | +700 bps | 79.0 | -$4.7M (20.3%) |
| Sector recession | -30% | +900 bps | 72.0 | -$6.3M (27.3%) |

### Portfolio-Level Stress Impact

| Metric | Pre-Trade | Post-Trade (Severe) | Limit |
|---|---|---|---|
| Portfolio loss under severe stress | $78M (3.9%) | $82.7M (4.1%) | 8.0% max |
| Spread duration impact (+100bps) | $12.4M | $12.9M | Informational |
| Expected loss (1-year) | $8.2M (0.41%) | $8.5M (0.43%) | 1.5% max |

Portfolio-level stress test passes all limits. Apex contribution to portfolio severe stress loss is $4.7M, representing 5.7% of total portfolio stress loss — proportionate to position size.

## Liquidity Assessment

| Dimension | Assessment |
|---|---|
| Asset type | First lien term loan |
| Liquidity tier | Tier 1 (3–5 business day exit) |
| Estimated bid-ask | 0.50–0.75 points |
| Market depth | 3–4 active dealers, $5M+ daily volume |
| Portfolio Tier 1 allocation | 22% ($440M) |
| Tier 1 target | >20% — Pass |

No liquidity constraint. First lien loans from B+ rated mid-cap issuers trade with adequate dealer liquidity.

## Final Recommendation

| Parameter | Value |
|---|---|
| **Recommended position size** | **$23M (1.15% of AUM)** |
| Original proposal | $25M (1.25%) |
| Adjustment | -$2M correlation adjustment |
| Conviction | Medium |
| All fund vehicle tests | Pass |
| All concentration limits | Pass |
| Stress test | Pass (4.1% portfolio loss vs. 8.0% limit) |
| Liquidity | Tier 1, no constraint |

### Conditions for Execution
1. Confirm bid-side levels at 99.00 or better (entry yield SOFR + 410 bps or wider)
2. Verify no pending rating action from S&P or Moody's
3. Set up surveillance monitoring with thesis-kill triggers per surveillance-monitoring handoff

### Thesis-Kill Triggers for Monitoring Handoff
- Leverage exceeds 6.0x (>1.2x increase from current)
- Loss of top-3 customer representing >15% of revenue
- EBITDA margin compression >300bps from entry level
- Sponsor dividend recap within 18 months of acquisition
- Rating downgrade to CCC+ or below

*Position sizing methodology references: `references/risk-appetite-and-limit-framework.md`, `references/fund-mandate-compliance.md`, `references/correlation-adjusted-position-sizing.md`, `references/portfolio-risk-parameters.md`, and `skills/private-credit-middle-market/references/bdc-regulatory.md` when the position is intended for a BDC.*
