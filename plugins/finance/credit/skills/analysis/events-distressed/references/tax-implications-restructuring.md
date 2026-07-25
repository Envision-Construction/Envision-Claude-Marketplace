---
last_updated: "2026-03-22"
---

# Tax Implications of Restructuring

Framework for analyzing tax consequences of debt restructuring, bankruptcy, and asset acquisitions — and their impact on recovery analysis and post-emergence credit quality.

> **Note:** Examples use the current 21% U.S. federal corporate tax rate (Tax Cuts and Jobs Act, 2017). If the statutory rate changes, adjust all examples accordingly.

## Cancellation of Debt (COD) Income

### General Rule (IRC Section 61(a)(11))

When debt is discharged for less than its face value, the difference is taxable income to the debtor:

**COD Income = Face Value of Debt - Amount Paid to Settle**

| Example | Face Value | Settlement | COD Income | Tax at 21% |
|---|---|---|---|---|
| Debt exchange at 70 cents | $100M | $70M cash | $30M | $6.3M |
| Debt-for-equity swap | $100M | Equity worth $60M | $40M | $8.4M |
| Partial forgiveness | $100M | $80M new debt | $20M | $4.2M |

### Exceptions to COD Income Recognition

| Exception | IRC Section | Conditions | Effect |
|---|---|---|---|
| Bankruptcy | 108(a)(1)(A) | Debtor is under title 11 (Chapter 11) | COD excluded from income; but tax attributes reduced |
| Insolvency | 108(a)(1)(B) | Debtor's liabilities exceed FMV of assets | COD excluded to extent of insolvency |
| Qualified Farm Debt | 108(a)(1)(C) | Agricultural borrower, qualified lender | COD excluded; attribute reduction required |
| Qualified Real Property | 108(a)(1)(D) | Real property business debt, solvent debtor | COD excluded; basis reduction in depreciable real property |

**Critical Distinction**: Out-of-court restructurings where the debtor is solvent may trigger full COD income taxation. In-court (Chapter 11) restructurings exclude COD from income but require tax attribute reduction.

## Tax Attribute Reduction

### Attribute Reduction Ordering Rules (Section 108(b))

When COD income is excluded under the bankruptcy or insolvency exceptions, the debtor must reduce tax attributes in the following order:

| Priority | Attribute | Reduction Amount |
|---|---|---|
| 1 | Net Operating Losses (NOLs) | Dollar-for-dollar |
| 2 | General business credits | 33.3 cents per dollar of COD |
| 3 | Minimum tax credits | Dollar-for-dollar |
| 4 | Capital loss carryovers | Dollar-for-dollar |
| 5 | Tax basis of property | Dollar-for-dollar (but not below liabilities) |
| 6 | Passive activity loss carryovers | Dollar-for-dollar |
| 7 | Foreign tax credit carryovers | 33.3 cents per dollar of COD |

**Election**: The debtor can elect to reduce the basis of depreciable property first (before NOLs). This preserves NOLs for future use but reduces future depreciation deductions.

### Practical Impact

A company emerging from Chapter 11 with $200M of COD income and $150M of pre-petition NOLs:
- NOLs reduced from $150M to $0 (used first in ordering rules)
- Remaining $50M of COD reduces other attributes (credits, basis)
- Post-emergence entity has significantly reduced tax shield

## Section 382 Limitations on NOLs

### Ownership Change Trigger

Section 382 limits annual use of pre-change NOLs when a company experiences an "ownership change" — defined as >50 percentage point increase in ownership by 5% shareholders over a 3-year testing period.

### Annual Limitation Calculation

**Section 382 Annual Limit = FMV of Old Loss Corporation x Long-Term Tax-Exempt Rate**

| Component | What to Use |
|---|---|
| FMV of Old Loss Corporation | Equity value immediately before ownership change |
| Long-Term Tax-Exempt Rate | The applicable IRS-published rate in effect at the time of the ownership change |

**Example**: Company with pre-change equity value of $100M:
- Annual NOL usage limit = $100M x applicable tax-exempt rate
- If pre-change NOLs materially exceed that annual limit, utilization may extend over many years
- Actual usability depends on the vintage of the NOLs and the tax rules then in force

### Built-In Gains Exception

If the company has net unrealized built-in gains (NUBIG) at the time of ownership change, recognized gains during the 5-year recognition period can increase the Section 382 limit. This is relevant when the company's assets have appreciated (common in real estate, IP-heavy businesses).

### Restructuring-Specific Provisions

| Provision | IRC Section | Effect |
|---|---|---|
| Bankruptcy Exception | 382(l)(5) | If old shareholders/creditors receive >50% of new equity, Section 382 limit may not apply. But subsequent ownership change within 2 years eliminates all pre-change NOLs. |
| Creditor Continuity | 382(l)(5)(E) | Creditors who receive equity must have held debt for 18+ months (or in ordinary course) to qualify |
| Alternative (382(l)(6)) | 382(l)(6) | If 382(l)(5) does not apply, use standard Section 382 calculation with FMV based on post-change value |

## Step-Up Basis in Asset Acquisitions

### 363 Sale Tax Implications

| Transaction Type | Tax Basis to Buyer | Depreciation/Amortization Benefit | Seller Tax Consequence |
|---|---|---|---|
| Asset Purchase (363 sale) | Stepped up to purchase price | Full new depreciation schedule on stepped-up basis | Taxable gain to estate on appreciated assets |
| Stock Purchase | Carryover basis (old tax attributes) | No new depreciation benefit | Seller capital gain on stock sale |
| Stock + Section 338(h)(10) | Treated as asset purchase for tax | Full step-up benefit | Seller treated as asset sale (higher tax) |

### Step-Up Benefit Quantification

**Annual Tax Benefit = Step-Up Amount / Amortization Period x Tax Rate**

Example: $300M asset purchase (vs. $100M carryover basis):
- Step-up: $200M
- Amortizable over 15 years: $13.3M annual amortization
- Tax benefit: $13.3M x 21% = $2.8M annual cash tax savings
- PV of benefit (over 15 years, 8% discount): ~$24M

This step-up benefit is a key component of LTO return analysis — the tax shield enhances post-acquisition cash flow.

## Practical Implications for Credit Analysis

### Recovery Analysis Adjustments

| Factor | Impact on Recovery | How to Model |
|---|---|---|
| COD income tax (out-of-court) | Reduces net recovery to debtor | Deduct estimated tax from settlement savings |
| Section 382 limitation | Reduces value of NOL tax shield | Apply annual limit; discount remaining NOL value |
| Tax attribute reduction | Post-emergence entity has reduced tax shield | Model higher effective tax rate for 3-5 years post-emergence |
| Step-up basis (asset sale) | Enhances buyer's post-acquisition cash flow | Quantify annual depreciation/amortization tax benefit |

### Post-Restructuring Tax Profile

The emerged entity's tax profile may differ significantly from the pre-petition entity:

| Pre-Restructuring | Post-Restructuring | Credit Impact |
|---|---|---|
| Significant NOLs → low cash taxes | NOLs reduced/limited → higher cash taxes | Lower FCF available for debt service |
| Depreciation shield from old assets | Potentially lower basis (attribute reduction) | Reduced depreciation deductions |
| Complex entity structure | Simplified structure (if 363 sale) | Potentially more efficient tax profile |

### Tax Leakage in Recovery Waterfall

For out-of-court restructurings involving solvent debtors:
1. Calculate gross savings from debt reduction
2. Deduct COD income tax (gross savings x effective tax rate)
3. Net savings = actual benefit to creditors
4. Example: $100M debt forgiveness for solvent debtor → $21M tax → net benefit = $79M

### Modeling Best Practices

- **Always model effective tax rate transition** over 3-5 years post-emergence
- **Quantify Section 382 limitation** when ownership change is >50%
- **Compare 363 sale vs. plan of reorganization** tax outcomes for the estate
- **Factor COD income into out-of-court restructuring economics** — tax leakage can make out-of-court solutions less attractive than Chapter 11
- **Assess whether the debtor should elect Section 382(l)(5) vs. (l)(6)** — depends on post-change equity value and desired NOL preservation strategy
