---
title: "Worked Example: New-Issue CLO Analysis"
last_updated: "2026-03-22"
update_cadence: annually
next_review: "2027-03-22"
type: worked-example
---

# Worked Example: New-Issue CLO Analysis

## 1. Deal Summary

This is a **synthetic teaching example** of a $500M broadly syndicated loan (BSL) CLO managed by a mid-tier manager. It is meant to show how to organize a new-issue review, not to provide current market levels. Refresh any spread, enhancement, and comp assumptions against root `references/market-benchmarks.md` before using this example in live work.

**Key Deal Terms:**

| Parameter | Detail |
|---|---|
| Closing Date | March 2026 |
| Manager | Ridgeline Capital Management |
| Target Portfolio | $500M BSL first lien loans |
| Reinvestment Period | 5 years (March 2031) |
| Non-Call Period | 2 years (March 2028) |
| Legal Final Maturity | March 2035 (9 years) |
| Warehouse | $250M (JPMorgan), ~60% ramped at close |
| Arranger | JPMorgan Securities |
| Trustee | US Bank |

### Capital Structure

| Tranche | Rating | Size ($M) | % of Capital | Spread (bps) | Attachment | Detachment | CE % |
|---|---|---|---|---|---|---|---|
| Class A-1 | AAA/Aaa | 310.0 | 62.0% | SOFR+130 | 38.0% | 100.0% | 38.0% |
| Class A-2 | AA/Aa2 | 40.0 | 8.0% | SOFR+185 | 30.0% | 38.0% | 30.0% |
| Class B | A/A2 | 30.0 | 6.0% | SOFR+250 | 24.0% | 30.0% | 24.0% |
| Class C | BBB-/Baa3 | 30.0 | 6.0% | SOFR+390 | 18.0% | 24.0% | 18.0% |
| Class D | BB-/Ba3 | 22.5 | 4.5% | SOFR+625 | 13.5% | 18.0% | 13.5% |
| Class E | B-/B3 | 12.5 | 2.5% | SOFR+950 | 11.0% | 13.5% | 11.0% |
| Equity | NR | 55.0 | 11.0% | — | 0.0% | 11.0% | — |
| **Total** | | **500.0** | **100.0%** | | | | |

**Structural Commentary:** The 38.0% AAA credit enhancement is in line with recent BSL CLO issuance (typical range 36-40%). The 11.0% equity tranche is standard for a $500M deal. The Class E (B-rated) tranche at 2.5% of capital reflects current market appetite for CLO mezzanine risk; this tranche was placed with two specialized mezzanine CLO funds. Total debt-to-equity leverage is approximately 8.1x.

---

## 2. Coverage Test Dashboard

Coverage tests are the structural guardrails governing cash flow distribution. The following table presents OC and IC levels at pricing alongside indenture triggers and resulting cushion.

### Overcollateralization (OC) Tests

| Test | Par Coverage at Pricing | Trigger Level | Cushion (pts) | Cushion (%) |
|---|---|---|---|---|
| Class A OC | 131.6% | 125.0% | 6.6 pts | 5.3% |
| Class B OC | 122.8% | 118.0% | 4.8 pts | 4.1% |
| Class C OC | 115.2% | 111.5% | 3.7 pts | 3.3% |
| Class D OC | 110.5% | 107.5% | 3.0 pts | 2.8% |
| Class E OC | 108.1% | 105.5% | 2.6 pts | 2.5% |

### Interest Coverage (IC) Tests

| Test | IC Ratio at Pricing | Trigger Level | Cushion |
|---|---|---|---|
| Class A IC | 8.2x | 2.0x | 6.2x |
| Class B IC | 5.1x | 2.0x | 3.1x |
| Class C IC | 3.4x | 1.5x | 1.9x |
| Class D IC | 2.6x | 1.3x | 1.3x |
| Class E IC | 2.2x | 1.1x | 1.1x |

**Cushion Commentary:** OC cushions are adequate at pricing but require monitoring. The Class E OC cushion of 2.6 pts implies the portfolio can absorb approximately $13M of par loss (at 0% recovery) before the junior OC test is breached and equity distributions are halted. Under typical recovery assumptions (65%), this equates to roughly $37M of defaults, or approximately 7.4% of the portfolio. IC tests provide substantial headroom at current SOFR levels given the floating-rate nature of both assets and liabilities.

---

## 3. Collateral Quality Metrics

The initial portfolio (approximately 60% ramped from warehouse, 40% to be acquired during the ramp-up period) exhibits the following quality metrics relative to indenture limits.

| Metric | Current Level | Indenture Limit | Cushion | Commentary |
|---|---|---|---|---|
| WARF | 2,850 | 3,200 (max) | 350 | Weighted toward single-B; no outsized CCC exposure |
| Diversity Score (Moody's) | 65 | 55 (min) | +10 | Well-diversified across 180+ obligors, 25+ industries |
| Weighted Avg Life (WAL) | 4.2 years | 5.5 years (max) | 1.3 yrs | Conservative positioning; room to extend during reinvestment |
| Weighted Avg Spread (WAS) | SOFR+378 bps | SOFR+340 bps (min) | +38 bps | Supports arbitrage; target maintenance above +360 during RP |
| CCC Bucket (Caa1 and below) | 4.5% | 7.5% (max) | 3.0% | Below threshold; excess CCC haircut not triggered |
| Current Defaults (D-rated) | 0.8% ($4.0M) | Haircut at market value | — | One defaulted position (media sector); recovery in process |
| Second Lien Exposure | 0.0% | 5.0% (max) | 5.0% | No second lien positions; first lien only |
| Covenant-Lite % | 87% | N/A | — | Consistent with current BSL market (~85-90% cov-lite) |
| Fixed-Rate Bucket | 3.2% | 10.0% (max) | 6.8% | Minimal basis risk between assets and liabilities |
| Single Obligor Concentration | 1.8% (max) | 2.5% (max) | 0.7% | Largest position is a BB-rated healthcare services credit |

**Portfolio Composition by Rating:**

| Rating | % of Portfolio |
|---|---|
| BB+/BB/BB- | 18.5% |
| B+/B | 56.2% |
| B- | 20.8% |
| CCC+/CCC | 4.5% |
| Defaulted | 0.8% (par-weighted, market-value haircut applied) |

**Industry Concentration (Top 5):**

| Industry | % of Portfolio |
|---|---|
| Healthcare & Pharmaceuticals | 12.8% |
| Software & Technology | 11.4% |
| Business Services | 9.6% |
| Insurance | 7.2% |
| Chemicals, Plastics & Rubber | 6.1% |

---

## 4. Manager Assessment

### Ridgeline Capital Management — Firm Overview

| Metric | Detail |
|---|---|
| Total CLO AUM | $8.0B across 12 active deals |
| Manager Tier | Tier 2 (established mid-size; not top-10 by AUM) |
| Platform Founded | 2015 |
| Investment Team | 18 professionals (8 portfolio managers/analysts) |
| Portfolio Turnover | ~25% annualized (moderate; credit-picker style) |
| Default Rate (Cumulative, All Vintages) | 1.8% (vs. 2.4% market average) |
| Style Classification | Credit picker; fundamental bottom-up; moderate trading activity |

### Vintage Performance Summary

The following table summarizes Ridgeline's CLO equity performance by vintage. Seasoned vintages (2018-2022) provide meaningful track record data; recent vintages (2024-2025) remain unseasoned and are presented for completeness but should not be weighted heavily in the assessment.

| Vintage | Deal | Size ($M) | Equity IRR | Equity MOIC | Annualized Default Rate | Status |
|---|---|---|---|---|---|---|
| 2018 | Ridgeline CLO I | 400 | 16.2% | 1.68x | 1.5% | Called (2023) |
| 2019 | Ridgeline CLO I-R | 425 | 14.8% | 1.55x | 2.1% | Called (2024) |
| 2020 | Ridgeline CLO II | 450 | 18.5% | 1.72x | 1.2% | Amortizing |
| 2021 | Ridgeline CLO II-R | 475 | 15.1% | 1.48x | 1.6% | In RP |
| 2022 | Ridgeline CLO III | 500 | 13.4% | 1.32x | 2.3% | In RP |
| 2024 | Ridgeline CLO III-R | 500 | 14.7%* | 1.12x* | 0.9%* | In RP (unseasoned) |
| 2025 | Ridgeline CLO IV Warehouse | 250 | N/A | N/A | 0.0% | Ramping |

*Unseasoned; based on distributions to date and current NAV. Actual realized returns will differ.*

**Performance Commentary:** Ridgeline's track record is solid for a Tier 2 manager. The 2020 vintage benefited from COVID-era dislocation purchases, generating the strongest returns. The 2022 vintage underperformed slightly due to elevated defaults in two media/telecom positions, though equity distributions remained uninterrupted. The manager's cumulative default rate of 1.8% is 60 bps below market average, suggesting disciplined credit selection. Portfolio turnover of 25% indicates a buy-and-hold orientation with selective trading around credit events rather than an active trading strategy.

**Risk Factors:** Mid-size platform with limited scale advantages in primary allocation versus Tier 1 managers. Analyst bench is adequate but lacks the depth of larger platforms (potential key-person risk if senior PM departs).

---

## 5. Cash Flow Waterfall Analysis

The following waterfall projects quarterly equity distributions and annual debt service coverage under three scenarios. All scenarios assume a 65% recovery rate on defaulted loans and SOFR at 4.30%.

### Scenario Definitions

| Scenario | CDR | Recovery | Reinvestment Spread | Description |
|---|---|---|---|---|
| Base Case | 2.0% | 65% | SOFR+370 bps | Aligned with long-term BSL default averages |
| Moderate Stress | 4.0% | 60% | SOFR+340 bps | Recessionary environment; spread compression on reinvestment |
| Severe Stress | 8.0% | 50% | SOFR+300 bps | Deep recession; elevated defaults and lower recoveries |

### Estimated Annual Cash Flow Distribution ($M)

| Priority | Payment | Base Case | Moderate Stress | Severe Stress |
|---|---|---|---|---|
| 1 | Senior Management Fee | 2.0 | 2.0 | 2.0 |
| 2 | Trustee/Admin Expenses | 0.8 | 0.8 | 0.8 |
| 3 | Class A-1 Interest (AAA) | 17.4 | 17.4 | 17.4 |
| 4 | Class A-2 Interest (AA) | 3.3 | 3.3 | 3.3 |
| 5 | Class B Interest (A) | 3.3 | 3.3 | 3.3 |
| 6 | Senior OC/IC Compliance | Pass | Pass | Diversion begins Yr 3 |
| 7 | Class C Interest (BBB) | 5.2 | 5.2 | 4.8 (reduced Yr 4+) |
| 8 | Junior OC/IC Compliance | Pass | Tight Yr 4+ | Fail Yr 2+ |
| 9 | Class D Interest (BB) | 6.3 | 6.3 | 3.1 (partial Yr 3+) |
| 10 | Class E Interest (B) | 5.3 | 4.8 | 0.0 (deferred Yr 2+) |
| 11 | Subordinated Mgmt Fee | 1.5 | 1.2 | 0.0 |
| 12 | **Equity Distributions** | **9.8** | **5.4** | **0.0 (Yr 2+)** |
| | **Total Available** | **54.9** | **49.7** | **34.7** |

**Waterfall Commentary:** Under the base case, the deal generates approximately $9.8M in annual equity distributions, supporting a 17.8% annual cash yield on $55M equity. Under moderate stress, OC tests tighten materially in year 4 but do not breach; equity distributions decline to $5.4M annually (9.8% cash yield). Under severe stress (8% CDR), the junior OC test fails by year 2, halting equity distributions and diverting cash to deleverage mezzanine tranches. At this stress level, the Class C tranche experiences partial interest shortfalls by year 4 and the Class D tranche suffers principal impairment.

---

## 6. Equity Return Analysis

### Base Case and Stress IRR Projections

| Scenario | Equity IRR | Equity MOIC | Cash-on-Cash Yield (Avg) | Breakeven CDR |
|---|---|---|---|---|
| Base Case (2% CDR) | 14.8% | 1.62x | 17.8% | — |
| Moderate Stress (4% CDR) | 9.2% | 1.28x | 9.8% | — |
| Severe Stress (8% CDR) | 1.5% | 1.02x | 0.0% (post Yr 2) | — |
| Equity Breakeven | 0.0% | 1.00x | — | ~7.5% CDR |

### Sensitivity Matrix: Equity IRR Under Varying Default and Recovery Assumptions

| CDR \ Recovery | 50% | 55% | 60% | 65% | 70% |
|---|---|---|---|---|---|
| **1.0%** | 14.2% | 15.0% | 15.8% | 16.6% | 17.3% |
| **2.0%** | 11.5% | 12.6% | 13.7% | 14.8% | 15.8% |
| **3.0%** | 8.6% | 10.0% | 11.3% | 12.6% | 13.8% |
| **4.0%** | 5.4% | 7.1% | 8.3% | 9.2% | 10.8% |
| **5.0%** | 2.8% | 4.5% | 6.0% | 7.4% | 8.8% |
| **6.0%** | 0.5% | 2.1% | 3.8% | 5.4% | 7.0% |
| **8.0%** | -4.2% | -2.0% | -0.2% | 1.5% | 3.5% |

### Reinvestment Spread Sensitivity (at 2% CDR, 65% Recovery)

| Reinvestment Spread | Equity IRR | Impact vs Base |
|---|---|---|
| SOFR+340 bps | 13.1% | -1.7% |
| SOFR+355 bps | 13.9% | -0.9% |
| SOFR+370 bps (base) | 14.8% | — |
| SOFR+385 bps | 15.6% | +0.8% |
| SOFR+400 bps | 16.4% | +1.6% |

**Sensitivity Commentary:** Equity returns are most sensitive to the CDR assumption, followed by recovery rates and reinvestment spreads. Each 1% increase in CDR reduces equity IRR by approximately 200-250 bps. Recovery rate sensitivity is asymmetric: returns degrade faster below 60% recovery than they improve above 65%. Reinvestment spread sensitivity highlights the importance of the manager maintaining portfolio WAS above +360 bps during the reinvestment period; each 15 bps of spread compression costs roughly 90 bps of equity IRR.

---

## 7. Relative Value Assessment

### Primary Market Comparables (Q1 2026 Vintage)

| Deal | Manager | Manager Tier | Size ($M) | AAA Spread | BB Spread | Equity Size % | WARF | Div Score |
|---|---|---|---|---|---|---|---|---|
| Ridgeline CLO IV | Ridgeline Capital | Tier 2 | 500 | +130 | +625 | 11.0% | 2,850 | 65 |
| Mountainview CLO XII | Mountainview Partners | Tier 1 | 600 | +115 | +575 | 10.5% | 2,780 | 72 |
| Cascade Funding VII | Cascade Credit | Tier 2 | 500 | +125 | +610 | 11.0% | 2,900 | 60 |
| Brookstone CLO III | Brookstone Asset Mgmt | Tier 3 | 400 | +145 | +680 | 11.5% | 2,950 | 55 |
| Clearwater CLO IX | Clearwater Capital | Tier 1 | 650 | +110 | +560 | 10.0% | 2,750 | 75 |

### Vintage Comparison (2024-2025 Issuance Benchmarks)

| Metric | Ridgeline IV (2026) | 2025 Avg (Tier 2) | 2024 Avg (Tier 2) |
|---|---|---|---|
| AAA Spread | +130 bps | +135 bps | +155 bps |
| AA Spread | +185 bps | +190 bps | +210 bps |
| BBB Spread | +390 bps | +400 bps | +435 bps |
| BB Spread | +625 bps | +645 bps | +700 bps |
| Equity Target IRR | 14-16% | 13-15% | 14-17% |
| WAS | +378 bps | +372 bps | +385 bps |
| AAA CE | 38.0% | 37.5% | 38.0% |

### Secondary Market Opportunities

| Comparison | Ridgeline IV (Primary) | Secondary Alternative |
|---|---|---|
| AAA Tranche | +130 bps (par) | 2023-2024 vintage AAA trading at +105-115 bps (price: 100.25-100.75) |
| BB Tranche | +625 bps (par) | 2022-2023 vintage BB trading at +700-800 bps (price: 92-96) |
| Equity | 14.8% target IRR (par) | Seasoned 2022 equity at 70-78% NAV; implied IRR 15-18% with shorter duration |

**Relative Value Commentary:** Ridgeline CLO IV prices in line with Tier 2 manager comps and modestly wide of Tier 1 benchmarks, which is expected given the manager's AUM scale and shorter track record. The 15 bps AAA spread premium versus Tier 1 issuance (Mountainview, Clearwater) compensates investors for incremental manager risk. Compared to 2024 vintages, spread compression of 25-75 bps across the stack reflects the tightening trend in primary CLO markets through early 2026.

For rated debt investors, secondary market 2023-2024 vintage AAA tranches offer tighter spreads but carry some seasoning benefit (known portfolio, shorter WAL). For equity investors, secondary seasoned equity positions may offer superior risk-adjusted returns given the combination of comparable IRR, shorter remaining duration, and observable portfolio performance. The primary equity tranche is most attractive to investors who have conviction in Ridgeline's manager ability and prefer to capture the full reinvestment period optionality.

**Recommendation Framework:**

- **AAA Investors:** Fair value at +130; neutral versus secondary alternatives. Consider if seeking reinvestment period exposure and 5-year WAL target.
- **Mezzanine (BBB/BB) Investors:** Attractive at +390/+625 given CE levels and manager track record. Preferable to secondary mezzanine where credit deterioration may be embedded.
- **Equity Investors:** Competitive at 14-16% target IRR. Evaluate against secondary seasoned equity alternatives and confirm conviction in Ridgeline's credit selection and reinvestment capabilities before committing.
