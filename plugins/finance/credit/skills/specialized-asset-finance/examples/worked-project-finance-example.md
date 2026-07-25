---
last_updated: "2026-03-22"
---

# Worked Example: Project Finance — Sunfield Energy Project (200MW Solar)

## Project Overview

| Parameter | Detail |
|---|---|
| Project | Sunfield Energy Project |
| Technology | Utility-scale solar photovoltaic (PV), single-axis tracking |
| Capacity | 200 MW (DC) / 160 MW (AC) |
| Location | West Texas (ERCOT region) |
| SPV | Sunfield Energy LLC |
| Sponsor | Meridian Renewables (60%) / Infrastructure Capital Partners (40%) |
| EPC Contractor | SolarBuild International (fixed-price, date-certain EPC) |
| Offtaker | Southwest Utility Corp (AA- rated, 25-year PPA) |
| O&M Provider | SunOps Maintenance Co. (10-year O&M agreement, renewable) |
| COD Target | Q4 2026 |
| Project Life | 35 years (panels), 25 years (PPA term) |

## Project Cost Structure

| Component | Amount ($M) | % of Total |
|---|---|---|
| EPC contract (fixed-price, turnkey) | $200.0 | 71.4% |
| Development costs (land, permits, interconnection) | $25.0 | 8.9% |
| Financing costs (fees, interest during construction) | $18.0 | 6.4% |
| Construction contingency (10% of EPC) | $20.0 | 7.1% |
| Working capital and reserves | $12.0 | 4.3% |
| Development fee to sponsor | $5.0 | 1.8% |
| **Total Project Cost** | **$280.0** | **100.0%** |

### Capital Structure

| Source | Amount ($M) | % of Total |
|---|---|---|
| Senior secured term loan | $196.0 | 70.0% |
| Sponsor equity | $84.0 | 30.0% |
| **Total Sources** | **$280.0** | **100.0%** |

## Revenue Model

### PPA Terms

| Parameter | Value |
|---|---|
| PPA counterparty | Southwest Utility Corp (AA-) |
| PPA price (Year 1) | $45.00 / MWh |
| Escalator | 1.5% per annum |
| Term | 25 years from COD |
| Curtailment provisions | Buyer bears curtailment risk for first 5% of annual generation; seller bears beyond 5% |
| Settlement | Monthly, 30-day payment terms |

### Generation Assumptions

| Metric | P50 | P75 | P90 |
|---|---|---|---|
| Capacity factor | 28.0% | 26.2% | 24.5% |
| Annual generation (GWh) | 491 | 459 | 430 |
| Degradation rate (annual) | 0.50% | 0.50% | 0.50% |

### Year 1 Revenue Calculation

| Component | P50 | P90 |
|---|---|---|
| Generation (GWh) | 491 | 430 |
| PPA price ($/MWh) | $45.00 | $45.00 |
| **Annual revenue** | **$22.1M** | **$19.4M** |

## Operating Cost Structure

| Cost Category | Annual Amount ($M) | Escalation | Notes |
|---|---|---|---|
| O&M contract | $1.60 | 2.0%/yr | Fixed-price, 10-year term ($8/kW-yr) |
| Insurance | $0.50 | 2.5%/yr | Property, liability, business interruption |
| Land lease | $0.30 | 1.5%/yr | 25-year ground lease with extension options |
| Asset management fee | $0.20 | 2.0%/yr | Sponsor-affiliated manager |
| Property taxes | $0.15 | 1.0%/yr | Negotiated PILOT agreement for years 1–15 |
| Grid connection fees | $0.10 | CPI | Transmission service charges |
| **Total annual opex** | **$2.85M** | | ~13% of P50 revenue |

## CFADS Projections (Years 1–5)

| ($M) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Revenue (P50) | 22.1 | 22.3 | 22.4 | 22.5 | 22.5 |
| Revenue escalation | — | +1.5% | +1.5% | +1.5% | +1.5% |
| Panel degradation | — | -0.5% | -0.5% | -0.5% | -0.5% |
| Net revenue growth | — | +1.0% | +1.0% | +1.0% | +1.0% |
| Operating expenses | (2.85) | (2.92) | (2.99) | (3.07) | (3.14) |
| Major maintenance reserve | (0.30) | (0.30) | (0.30) | (0.70) | (0.70) |
| Taxes | (0.45) | (0.42) | (0.40) | (0.38) | (0.36) |
| **CFADS** | **18.50** | **18.66** | **18.71** | **18.35** | **18.30** |

Notes: ITC benefits captured through tax equity structure (modeled separately). Major maintenance reserve increases in Year 4 for inverter replacement program beginning Year 10.

## Debt Sizing

### Coverage Ratio Targets

| Ratio | Target | Definition |
|---|---|---|
| Minimum DSCR | 1.35x | CFADS / Annual Debt Service (P50 basis) |
| Minimum LLCR | 1.20x | NPV of CFADS over loan life / Outstanding debt |
| Minimum PLCR | 1.15x | NPV of CFADS over project life / Outstanding debt |

### Debt Sizing Calculation

| Approach | Max Debt Service ($M) | Implied Debt ($M) | Binding? |
|---|---|---|---|
| DSCR (1.35x on Year 1 CFADS) | $13.70 | $196M | **Yes** |
| LLCR (1.20x) | — | $204M | No |
| PLCR (1.15x) | — | $218M | No |

**Result**: $196M senior secured term loan (70% of project cost). The DSCR constraint is binding in Year 1 (lowest CFADS year due to no escalation benefit yet).

### Debt Terms

| Parameter | Value |
|---|---|
| Facility size | $196M |
| Tenor | 18 years (matures Year 18 post-COD) |
| Amortization | Sculpted to match seasonal and degradation-adjusted cash flows |
| Interest rate | SOFR + 175 bps (fixed via swap at 5.25% all-in) |
| Cash sweep | 50% of excess cash flow if DSCR >1.50x; 75% if >1.60x |
| Lock-up DSCR | 1.20x (distributions blocked below this level) |
| Default DSCR | 1.05x |

## Sculpted vs. Level Amortization Comparison

| Metric | Sculpted | Level |
|---|---|---|
| Year 1 debt service | $13.7M | $15.8M |
| Year 1 DSCR | 1.35x | 1.17x |
| Year 10 debt service | $12.9M | $15.8M |
| Year 10 DSCR | 1.38x | 1.13x |
| Min DSCR (any year) | 1.35x | 1.10x |
| Max DSCR (any year) | 1.42x | 1.68x |
| DSCR variance (std dev) | 0.02x | 0.18x |

Sculpted amortization produces a much flatter DSCR profile (1.35x–1.42x) compared to level amortization (1.10x–1.68x). Level amortization would breach the 1.20x lock-up DSCR in early years when CFADS is lowest. Sculpted repayment is critical for maintaining distribution capacity to equity investors.

## Cash Flow Waterfall

| Priority | Use | Mechanism |
|---|---|---|
| 1 | Operating expenses and taxes | Paid first from revenue |
| 2 | Senior debt service (interest + sculpted principal) | Mandatory; default if missed |
| 3 | DSRA top-up | Replenish to 6-month target if drawn |
| 4 | Major maintenance reserve top-up | Replenish to 3-year forward requirement |
| 5 | Cash sweep (excess cash flow) | 50% to debt prepayment if DSCR >1.50x |
| 6 | Distributions to equity | Residual cash after all senior obligations |

### Distribution Lock-Up Test

| Condition | Threshold | Consequence |
|---|---|---|
| Backward-looking DSCR | <1.20x (trailing 12 months) | Distributions suspended; cash trapped |
| Forward-looking DSCR | <1.20x (next 12 months projected) | Distributions suspended |
| DSRA balance | <6 months debt service | Distributions suspended until replenished |
| Insurance | Not current | Distributions suspended |

## Reserve Accounts

| Reserve | Size | Sizing Basis | Funded At |
|---|---|---|---|
| Debt Service Reserve Account (DSRA) | $6.9M | 6 months of max annual debt service | Financial close (funded from loan proceeds) |
| Major Maintenance Reserve (MR) | $2.1M | 3 years of projected major maintenance | Built up from CFADS over Years 1–3 |
| Construction contingency | $20.0M | 10% of EPC contract | Financial close; released to equity at COD if unspent |

## Key Risk Assessment

| Risk | Mitigation | Residual Risk |
|---|---|---|
| **Construction** | Fixed-price, date-certain EPC with $20M contingency; LD regime for delay and performance shortfall | Low — SolarBuild has completed 15+ projects of similar scale |
| **Resource/Generation** | P50 based on 10-year irradiance data; P90 scenario modeled | Medium — Year-to-year variability of +/-10% is normal |
| **Panel Degradation** | 0.50%/year assumed (manufacturer warranty guarantees <0.70%) | Low-Medium — stress case at 0.70% modeled below |
| **Offtaker Credit** | Southwest Utility Corp rated AA- (stable); regulated utility with cost recovery mechanism | Low — downgrade to BBB would trigger enhanced monitoring |
| **Curtailment** | Buyer bears first 5%; historical curtailment in ERCOT West Texas averages 3%–4% | Medium — grid congestion increasing as more solar capacity added |
| **Interest Rate** | Fully swapped to fixed rate at 5.25% | Negligible — hedged |
| **Regulatory** | ITC clawback risk if project sold or changes use within 5 years; PILOT agreement for property taxes | Low — sponsor committed to 5-year hold minimum |

## Stress Scenarios

### Scenario 1: P90 Generation

| Metric | P50 Base | P90 Stress | Delta |
|---|---|---|---|
| Annual generation (GWh) | 491 | 430 | -12.4% |
| Year 1 revenue | $22.1M | $19.4M | -$2.7M |
| Year 1 CFADS | $18.5M | $15.8M | -$2.7M |
| Year 1 DSCR | 1.35x | 1.15x | -0.20x |
| Distribution capacity | Yes | No (below 1.20x lock-up) | Distributions suspended |

### Scenario 2: P90 Generation + 200bps Rate Shock (Swap Breakage)

| Metric | Base | Stress | Delta |
|---|---|---|---|
| All-in interest rate | 5.25% | 7.25% | +200bps |
| Annual interest cost increase | — | +$3.9M | — |
| Year 1 CFADS (P90) | $15.8M | $15.8M | Unchanged |
| Year 1 debt service | $13.7M | $17.6M | +$3.9M |
| Year 1 DSCR | 1.15x | 0.90x | **Below 1.0x** |

This combined scenario produces a DSCR below 1.0x, triggering a default event. However, the swap structure means this scenario requires counterparty default on the interest rate swap — probability assessed as very low given bank counterparty.

### Scenario 3: Accelerated Panel Degradation (0.70%/year)

| Metric | Year 5 (Base) | Year 5 (Stress) | Year 10 (Base) | Year 10 (Stress) |
|---|---|---|---|---|
| Cumulative degradation | 2.5% | 3.5% | 5.0% | 7.0% |
| Generation impact | -12 GWh | -17 GWh | -25 GWh | -34 GWh |
| Revenue impact | -$0.6M | -$0.8M | -$1.3M | -$1.8M |
| DSCR impact | 1.38x | 1.34x | 1.40x | 1.30x |

Accelerated degradation erodes DSCR gradually. By Year 10, DSCR drops to 1.30x (still above 1.20x lock-up) but reduces cash sweep capacity and equity distributions materially.

### Escalation Trigger Mapping

| Condition | Threshold | Action |
|---|---|---|
| DSCR <1.20x | Lock-up trigger | Distributions suspended; enhanced monitoring |
| DSCR <1.10x | Watch trigger | Escalate to surveillance-monitoring Tier 2 |
| DSCR <1.05x | Default trigger | Escalate to surveillance-monitoring Tier 3 (per specialized-asset-finance handoff rules) |
| Offtaker downgrade below BBB | Counterparty risk | Enhanced monitoring; evaluate replacement offtaker options |
| Curtailment >8% annual | Revenue risk | Update generation model; evaluate grid upgrade timeline |

## Credit Assessment Summary

| Dimension | Assessment | Rating |
|---|---|---|
| Revenue certainty | 25-year PPA with AA- offtaker; 1.5% annual escalation | Strong |
| Operating risk | Fixed O&M contract; proven technology; experienced EPC | Low |
| Financial structure | 70/30 D/E; sculpted amortization; 1.35x min DSCR | Adequate |
| Sponsor quality | Meridian (experienced developer, 15+ projects) / ICP (infrastructure fund) | Strong |
| Stress resilience | P90 passes lock-up but suspends distributions; combined P90 + rate shock fails | Moderate |
| Environmental/permitting | All permits secured; no endangered species or cultural resource issues | Low risk |

**Overall Credit Quality**: Investment grade characteristics (contracted cash flow, rated offtaker, proven technology). Debt sizing is conservative at 1.35x minimum DSCR. Primary risk is generation variability and long-term curtailment exposure in an increasingly congested ERCOT grid.

*Project finance analysis references: `references/project-finance-fundamentals.md`, `references/cash-flow-waterfall-debt-sculpting.md`, `references/project-finance-credit-metrics.md`*
