---
last_updated: "2026-03-22"
---

# Lease Accounting & Covenant Impact

Framework for analyzing the impact of ASC 842 lease accounting on credit metrics, covenant compliance, and cross-company comparability.

## ASC 842 Overview

Effective for public companies from January 2019, ASC 842 requires recognition of virtually all leases >12 months on the balance sheet:

| Lease Type | Balance Sheet Impact | Income Statement Impact | Cash Flow Statement |
|---|---|---|---|
| Finance Lease (formerly capital) | ROU Asset + Lease Liability | Depreciation + Interest Expense | Principal: Financing; Interest: Operating |
| Operating Lease | ROU Asset + Lease Liability | Single lease expense (straight-line) in opex | Operating cash flow (unchanged from pre-842) |

### Classification Criteria

A lease is a **finance lease** if ANY of the following are met:
1. Transfer of ownership at end of term
2. Bargain purchase option
3. Lease term is major part (≥75%) of economic life
4. Present value of payments is substantially all (≥90%) of fair value
5. Specialized asset with no alternative use

All other leases are **operating leases**.

## Impact on Leverage Ratios

### The Definition of "Debt" Matters

| Credit Agreement Term | Typically Includes Operating Leases? | Implication |
|---|---|---|
| "Funded Debt" | NO — excludes operating lease liabilities | Leverage ratio unaffected by ASC 842 |
| "Funded Indebtedness" | NO — typically same as Funded Debt | Leverage ratio unaffected |
| "Total Debt" | MAYBE — depends on specific definition | Check whether lease liabilities are carved out |
| "Total Indebtedness" | POSSIBLY — broader definitions may include | Read definition carefully |
| "Net Debt" | MAYBE — if defined as all balance sheet debt | Check for lease liability exclusion |

**Critical Step**: Always read the credit agreement's definition of Indebtedness/Debt to determine whether operating lease liabilities are included in leverage calculations.

## Impact on Interest Coverage

| Ratio | Finance Lease Treatment | Operating Lease Treatment |
|---|---|---|
| EBITDA / Interest | Interest portion of finance lease included in "Interest Expense" | Lease expense in opex, excluded from Interest Expense |
| EBITDA / Total Fixed Charges | Includes finance lease interest | May or may not include operating lease payments |
| EBITDAR / (Interest + Rent) | N/A — already captured in rent | Lease expense captured as "Rent" in denominator |

### EBITDA vs. EBITDAR

| Metric | Formula | When Used |
|---|---|---|
| EBITDA | Earnings before Interest, Taxes, Depreciation, Amortization | Standard leverage metric |
| EBITDAR | EBITDA + Rent/Lease Expense | Used when operating leases are a significant cost (retail, restaurants, airlines) |

**Credit Agreement Practice**: Some agreements define the leverage test using EBITDAR with a fixed charge coverage test that includes rent in the denominator: EBITDAR / (Interest + Scheduled Debt Amortization + Rent). This captures lease obligations regardless of accounting classification.

## Covenant Compliance Issues

### Frozen GAAP Provisions

| Provision | Language | Effect |
|---|---|---|
| Frozen GAAP | "GAAP as in effect on the Closing Date" | Prevents ASC 842 from affecting covenant calculations |
| Current GAAP | "GAAP as in effect from time to time" | ASC 842 changes flow through to covenant metrics |
| Hybrid | Frozen for specific definitions, current for others | Read each defined term individually |

**Risk Scenario**: Without frozen GAAP, ASC 842 adoption can cause inadvertent covenant breaches:
- Pre-ASC 842: Total Debt/EBITDA = 4.5x (covenant at 5.0x) — 0.5x headroom
- Post-ASC 842: Operating lease liability of $200M added to "Total Debt" → new ratio = 5.8x
- Result: Technical default triggered by accounting change, not business deterioration

**Prevalence**: Most post-2018 credit agreements include ASC 842 carve-outs. Pre-2018 agreements without frozen GAAP may have required amendments to address this.

## Analytical Adjustments for Comparability

### Cross-Company Normalization

When comparing companies with different lease profiles, normalize to a common basis:

| Adjustment | Method | Purpose |
|---|---|---|
| Capitalize operating leases | Add 6-8x annual rent to debt | Quick approximation for pre-ASC 842 analysis |
| Use present value of lease payments | Sum of discounted future minimum lease payments | More precise; use company's incremental borrowing rate |
| EBITDAR-based leverage | Total Debt + Capitalized Leases / EBITDAR | Apples-to-apples comparison |

### Quick Capitalization Formula

**Capitalized Lease Value ≈ Annual Rent Expense x Capitalization Multiple**

| Remaining Lease Term | Suggested Multiple |
|---|---|
| <5 years average remaining | 5-6x |
| 5-10 years average remaining | 6-8x |
| >10 years average remaining | 8-10x |

## Sector Impact

| Sector | Lease Intensity | Primary Lease Type | Balance Sheet Impact |
|---|---|---|---|
| Retail / Restaurants | VERY HIGH | Store leases (operating) | $1B+ for large chains |
| Airlines | HIGH | Aircraft leases (operating + finance) | $5-20B for major carriers |
| Healthcare (hospitals) | HIGH | Facility leases (operating) | $500M-$5B |
| Hotels / Hospitality | HIGH | Property leases (operating) | Significant, varies by model |
| Technology / Software | LOW | Office leases only | Minimal impact |
| Manufacturing | LOW-MEDIUM | Facility + equipment | Moderate |
| Mining / E&P | LOW | Equipment leases | Minimal |

## Sale-Leaseback Transactions

### Credit Analysis Considerations

Sale-leasebacks are a form of financing — the company sells an asset and leases it back, generating upfront cash but committing to future lease payments:

| Factor | Assessment |
|---|---|
| Economic substance | Financing transaction disguised as asset sale |
| Cash flow impact | Immediate cash inflow, ongoing lease expense (reduces future FCF) |
| Balance sheet impact | Asset removed, lease liability added (post-ASC 842: often net neutral) |
| Leverage impact | Depends on credit agreement definition of debt |
| Red flag threshold | Multiple sale-leasebacks in short period may indicate liquidity stress |

## Red Flags

- [ ] Large operating lease portfolio with short remaining terms (<3 years average) — significant renewal/repricing risk
- [ ] Above-market rent obligations vs. current market rates — overpaying for space
- [ ] Sale-leaseback transactions increasing in frequency — potential liquidity management signal
- [ ] Credit agreement lacks frozen GAAP or ASC 842 carve-out language
- [ ] Lease-adjusted leverage (EBITDAR basis) significantly higher than reported leverage — understated financial risk
- [ ] Related-party lease arrangements (e.g., leasing from sponsor-owned real estate) — check arm's-length pricing
- [ ] Variable lease payments with significant upside exposure (percentage rent, CPI escalators without caps)
