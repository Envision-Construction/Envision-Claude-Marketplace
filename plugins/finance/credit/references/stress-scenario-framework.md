---
last_updated: "2026-03-21"
update_cadence: annually
next_review: "2027-03-21"
data_vintage: "FY 2025"
sources:
  - "Historical credit cycle analysis (2001, 2008-09, 2015-16, 2020)"
  - "Rating agency stress methodologies"
  - "Internal risk management frameworks"
---

# Stress Scenario Framework

**Last Updated:** March 2026
**Update Cadence:** Annually
**Next Review:** March 2027

This file provides standardized stress parameters by asset class for use across all credit analysis skills. When performing scenario analysis, stress testing, or "break the thesis" exercises, use these parameters as starting points and adjust for issuer-specific factors.

---

## 1. Corporate Credit Stress Parameters

| Scenario | Revenue Decline | EBITDA Margin Compression | Interest Rate Shock | Spread Widening | Default Rate | Recovery |
|---|---|---|---|---|---|---|
| Mild Downturn | -5 to -10% | -100 to -200 bps | +100 bps | +150-250 bps | 2-3% | 65-75% |
| Moderate Recession | -10 to -20% | -200 to -400 bps | +200 bps | +300-500 bps | 4-6% | 55-65% |
| Severe Stress (GFC-like) | -20 to -35% | -400 to -800 bps | +300 bps | +700-1200 bps | 8-12% | 40-55% |
| Sector-Specific Shock | -25 to -50% (affected) | -500+ bps | Flat | +500-1000 bps | 10-15% (sector) | 35-50% |

**Sector Adjustments to Corporate Stress:**

| Sector | Revenue Sensitivity vs. Base | Margin Sensitivity | Typical Recovery |
|---|---|---|---|
| Healthcare Services | 0.7x (defensive) | 0.8x | 60-70% (asset-light) |
| Technology / SaaS | 0.5x (recurring revenue) | 0.6x | 50-60% (IP-heavy, limited tangibles) |
| Energy & Midstream | 1.5x (commodity-linked) | 1.5x | 65-80% (asset-heavy) |
| Retail & Consumer | 1.3x (discretionary) | 1.2x | 30-50% (lease-burdened) |
| Industrials | 1.2x (cyclical) | 1.0x | 60-75% (equipment value) |
| Financial Services | 1.0x | 1.2x (credit losses) | 40-60% (depends on asset quality) |

**Covenant Breach Calibration:**

| Leverage Level | Headroom to Breach (6.0x max) | Revenue Decline to Breach |
|---|---|---|
| 4.0x | 33% | -30 to -35% |
| 4.5x | 25% | -22 to -27% |
| 5.0x | 17% | -15 to -20% |
| 5.5x | 8% | -8 to -12% |
| 6.0x | 0% | Already at limit |

---

## 2. CRE Stress Parameters

| Scenario | NOI Decline | Cap Rate Widening | Vacancy Increase | Rate Shock | Value Decline |
|---|---|---|---|---|---|
| Mild | -5 to -10% | +25-50 bps | +5-10% | +100 bps | -10 to -20% |
| Moderate | -10 to -20% | +50-100 bps | +10-20% | +200 bps | -20 to -35% |
| Severe | -20 to -35% | +100-200 bps | +20-35% | +300 bps | -35 to -55% |

**Property Type Adjustments:**

| Property Type | NOI Sensitivity vs. Base | Vacancy Sensitivity | Recovery Timeline |
|---|---|---|---|
| Multifamily | 0.6x (essential housing) | 0.5x | 12-18 months |
| Industrial/Logistics | 0.5x (e-commerce tailwind) | 0.4x | 12-18 months |
| Office (CBD) | 1.5x (WFH headwind) | 1.5x | 24-36 months |
| Office (Suburban) | 1.2x | 1.2x | 18-30 months |
| Retail (Grocery-Anchored) | 0.7x | 0.6x | 12-24 months |
| Retail (Non-Essential) | 1.4x | 1.3x | 24-36 months |
| Hospitality | 2.0x (RevPAR volatility) | N/A (occupancy-based) | 18-36 months |

**DSCR Stress Calibration:**

| Current DSCR | Rate Shock to Breach 1.0x | NOI Decline to Breach 1.0x |
|---|---|---|
| 1.50x | +350-400 bps | -33% |
| 1.35x | +250-300 bps | -26% |
| 1.25x | +175-225 bps | -20% |
| 1.15x | +100-150 bps | -13% |
| 1.10x | +50-100 bps | -9% |

---

## 3. Structured Finance (CLO) Stress Parameters

| Scenario | CDR | Recovery Rate | WARF Increase | CCC Bucket Increase | OC Cushion Impact |
|---|---|---|---|---|---|
| Mild | 2-3% | 65-70% | +50-100 | +3-5% | -50 to -100 bps |
| Moderate | 4-6% | 55-65% | +100-200 | +5-10% | -100 to -250 bps |
| Severe (1.5x historical) | 8-12% | 40-55% | +200-400 | +10-20% | -250 to -500 bps |

**CLO Tranche-Specific Stress:**

| Tranche | Attachment Point | CDR to Impair | Loss Severity at Severe |
|---|---|---|---|
| AAA (64% detach) | 36% | >15% sustained | Negligible |
| AA (36% detach) | 26% | >12% sustained | 0-5% |
| A (26% detach) | 20% | >9% sustained | 5-15% |
| BBB (20% detach) | 15% | >7% sustained | 10-25% |
| BB (15% detach) | 11% | >5% sustained | 20-40% |
| Equity (11% detach) | 0% | >2% sustained | 40-100% |

**Prepayment Stress:**

| Scenario | CPR Impact | WAL Extension | Duration Risk |
|---|---|---|---|
| Rates Rise +200bps | CPR drops 30-50% | WAL extends 0.5-1.5 years | Moderate — extends duration |
| Rates Fall -200bps | CPR increases 50-100% | WAL shortens 1.0-2.0 years | Moderate — reinvestment risk |
| Credit Stress | CPR drops 50-70% | WAL extends 1.0-2.5 years | High — extends exposure to deteriorating pool |

---

## 4. Private Credit Stress Parameters

| Scenario | EBITDA Decline | Coverage Compression | Non-Accrual Increase | Fair Value Haircut | PIK Conversion |
|---|---|---|---|---|---|
| Mild | -5 to -15% | -0.5x to -1.0x | +2-3% | -3 to -5% | +5-10% of income |
| Moderate | -15 to -25% | -1.0x to -1.5x | +5-8% | -5 to -10% | +10-20% of income |
| Severe | -25 to -40% | -1.5x to -2.5x | +10-15% | -10 to -20% | +20-30% of income |

**Private Credit-Specific Stress Factors:**

| Factor | Mild | Moderate | Severe |
|---|---|---|---|
| Amendment/Waiver Rate | 5-10% of portfolio | 10-20% | 20-35% |
| Equity Cure Frequency | 1-2 positions | 3-5 positions | 5-10 positions |
| Sponsor Support Probability | 85-90% | 70-80% | 50-65% |
| Recovery (1st Lien) | 70-80% | 60-70% | 45-60% |
| Recovery (Unitranche Last-Out) | 40-55% | 25-40% | 10-25% |

---

## 5. When to Apply Each Severity Level

| Severity | When to Use | Typical Context |
|---|---|---|
| **Mild** | Routine quarterly stress test, sector-specific softness, early-cycle monitoring | Quarterly portfolio review, new investment base case stress |
| **Moderate** | Economic downturn underway, rising defaults, credit deterioration visible | IC challenge scenarios, watchlist assessment, position re-evaluation |
| **Severe** | "Break the thesis" analysis, worst-case recovery estimation, tail risk assessment | IC decline/conditional analysis, distressed valuation, portfolio-level stress test |
| **Sector-Specific** | Industry disruption, regulatory change, commodity shock | Single-sector concentration risk, event-driven analysis |

**Key Principle:** Stress parameters should be adjusted for issuer-specific factors. A company with 80% recurring revenue should use 0.5x the standard revenue decline. A company with high operating leverage should use 1.5x the standard margin compression. Always disclose adjustments and rationale.

---

## 6. Historical Calibration

These stress parameters are calibrated to historical credit cycles:

| Cycle | Duration | HY Default Rate | Loan Default Rate | HY Spread Peak | Recovery (Sr Sec) |
|---|---|---|---|---|---|
| 2001-02 (TMT Bust) | 18 months | 10.7% | 6.3% | +1,100 bps | 57% |
| 2008-09 (GFC) | 15 months | 13.7% | 8.1% | +1,800 bps | 52% |
| 2015-16 (Energy) | 12 months | 5.1% (HY) | 2.8% | +870 bps (HY) | 62% |
| 2020 (COVID) | 6 months | 6.2% | 3.4% | +1,100 bps | 48% |
| 2022-23 (Rate Cycle) | 18 months | 2.8% | 1.9% | +550 bps | 65% |

**Note:** "Severe" parameters approximate the 2008-09 GFC experience. "Moderate" parameters approximate the 2015-16 energy downturn (ex-energy) or 2020 COVID impact. "Mild" parameters approximate routine credit cycle softness.
