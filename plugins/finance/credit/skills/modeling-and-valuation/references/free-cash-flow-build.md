---
last_updated: "2026-03-21"
---

## Free Cash Flow Build

### Cash Flow Statement Analysis

The cash flow statement is where credit analysis lives. It shows actual cash movements and must reconcile with balance sheet changes.

#### Cash from Operations (CFO): The Start

```
Operating Cash Flow starts with:
  Net Income
  + Depreciation (non-cash add-back)
  + Amortization (non-cash add-back)
  ± Changes in Deferred Taxes
  ± Changes in Deferred Revenue
  ± Changes in Other Non-Cash Items
  Subtotal: Adjusted Net Income (approx. EBITDA)

  Then adjust for working capital:
  - Increase in Receivables (cash outflow)
  - Increase in Inventory (cash outflow)
  + Increase in Payables (cash inflow)
  + Increase in Accrued Expenses (cash inflow)
  ± Changes in Other Working Capital Items
  _______________
  = Net Cash from Operating Activities
```

**Key insight:** Operating cash flow can be very different from EBITDA due to:
- Large working capital swings (seasonal businesses)
- Timing of tax payments vs. accruals
- Large one-time or non-recurring items with different tax treatment

#### Free Cash Flow (FCF) Derivation

Free Cash Flow represents cash available after reinvestment to service debt and equity.

**Method 1: From Operating Cash Flow (simpler)**
```
Operating Cash Flow
  - CapEx (Capital Expenditures)
  _______________
  = Free Cash Flow
```

**Method 2: From EBITDA (more transparent for credit)**
```
Adjusted EBITDA
  - Cash Interest Paid
  - Cash Taxes Paid
  - CapEx
  ± Changes in Working Capital
  _______________
  = Free Cash Flow
```

**Example FCF waterfall:**

| Item | Amount |
|------|--------|
| Adjusted EBITDA | $100.0M |
| Cash interest paid | (15.0) |
| Cash taxes paid | (12.0) |
| Maintenance CapEx | (8.0) |
| Growth CapEx | (5.0) |
| Working capital increase | (3.0) |
| **Free Cash Flow** | **$57.0M** |

**Interpretation:** $57.0M is available for debt paydown, additional leverage, acquisitions, or dividends.

#### Maintenance vs. Growth CapEx Distinction

CapEx falls into two categories:

**Maintenance CapEx:**
- Sustains existing operations
- Keeps facilities, equipment, and technology current
- Example: Replacing aging machinery, routine facility maintenance
- Necessary to keep business running; non-discretionary
- Estimate as % of revenue (usually 2-5% depending on asset-intensity)

**Growth CapEx:**
- Builds new capacity or enters new markets
- Discretionary in nature; reduces in downturns
- Example: New facility construction, major product line expansion
- Often curtailed first when cash flow pressures arise

**Credit analysis:**
- Conservative models assume maintenance CapEx continues even in stress
- Growth CapEx is first to be cut; don't rely on it in base case
- Ratio: Maintenance CapEx / Total CapEx reveals operating leverage

**Example:**
- Company reports $50M total CapEx
- Maintenance CapEx = $30M (disclosed or estimated)
- Growth CapEx = $20M
- In stress scenario, assume company cuts growth CapEx entirely → FCF = +$20M improvement

#### Working Capital Changes: Cash Impact of Operations

Working capital cycle: Cash → Inventory → Receivables → Cash

```
Working Capital Change = Δ(Receivables + Inventory - Payables)
```

**Changes in working capital impact cash flow:**

| Item | Cash Impact |
|------|------------|
| Receivables increase | Cash outflow (customers owe more) |
| Receivables decrease | Cash inflow (collecting past sales) |
| Inventory increase | Cash outflow (money tied up in stock) |
| Inventory decrease | Cash inflow (selling down stock) |
| Payables increase | Cash inflow (deferring cash outflows) |
| Payables decrease | Cash outflow (paying suppliers) |

**Example:**
- Receivables increase $5M (customers bought more on credit)
- Inventory decreases $2M (working down excess stock)
- Payables increase $3M (extended payment terms)
- Net working capital benefit = +$2M - $5M = -$3M (use of cash)

**Credit assessment:**
- Seasonal businesses see large working capital swings
- Growth businesses consume working capital (need more receivables/inventory)
- Payables stretched too far is unsustainable and precursor to stress
- Working capital facility size must accommodate swings

#### Cash Flow from Investing: CapEx and M&A

```
Cash Flow from Investing includes:
  - CapEx (purchase of PP&E)
  - Acquisitions (cash paid for businesses)
  + Proceeds from asset sales
  + Proceeds from divested businesses
  _______________
  = Net Cash Used in Investing
```

**Credit considerations:**
- Large acquisitions affect debt capacity and leverage ratios
- Asset sales may indicate financial distress or strategic repositioning
- CapEx trends vs. historical patterns reveal management priorities

#### Cash Flow from Financing: Debt and Equity

```
Cash Flow from Financing includes:
  + Debt issuance (new borrowings)
  - Debt repayment
  + Equity issuance
  - Dividends paid
  - Share repurchases
  _______________
  = Net Cash from Financing
```

**Credit analysis:**
- Track when debt is issued/refinanced (maturity management)
- Dividends/buybacks reflect capital allocation; aggressive distributions indicate confidence or buyout pressure
- Financing cash flows must balance the cash generation and investing activity

### Formula
```
Adjusted EBITDA
  - Cash Interest Paid
  - Cash Taxes Paid
  - Maintenance CapEx
  - Growth CapEx
  ± Changes in Working Capital
  = Free Cash Flow (to debt holders)
```

### Cash Interest
```
Cash Interest = Interest on each debt tranche × Cash % + PIK Interest additions
```

Example:
- Term Loan: $400M × (SOFR + 4.0%) = ~$24M cash interest (at 6% all-in rate)
- First Lien Bond: $150M × 6.50% = $9.75M cash interest
- Total: ~$34M annual cash interest

### Cash Taxes
```
Cash Taxes = Taxable Income × Effective Tax Rate
```

**Key adjustments:**
- **NOLs (Net Operating Loss Carryforwards)**: reduce current-year taxable income
  - Example: $50M NOL can offset $50M of income before expiring
  - Limit: "Section 382" restrictions if ownership changes significantly (LBO risk)
- **Tax depreciation**: often accelerates faster than book D&A; creates temporary tax shield
- **Effective tax rate**: 22-28% in normal environment; lower if NOLs present

**Conservative approach:** Model full statutory rate (21-25%) unless company has large proven NOL balance.

### CapEx Modeling
**Maintenance CapEx:**
```
Maintenance CapEx ≈ Depreciation & Amortization
(Rule of thumb: keep the asset base in steady state)
```

**Growth CapEx:**
```
Growth CapEx = Incremental Revenue × (CapEx/Revenue Ratio)
```

Example: $100M additional revenue requires $5M CapEx (5% ratio typical for mature companies)

**Total CapEx = Maintenance + Growth**

In stress scenarios: assume maintenance CapEx is not cut; growth CapEx can be deferred.

### Working Capital
**Model each component as a percentage of revenue or as days:**

```
Days Calculation:
- Receivables Days = (Accounts Receivable / Revenue) × 365
- Inventory Days = (Inventory / COGS) × 365
- Payables Days = (Accounts Payable / COGS) × 365

Cash Conversion Cycle = Receivables Days + Inventory Days - Payables Days
```

**Change in Working Capital:**
```
ΔWVC = (New WVC Balance) - (Prior WVC Balance)
Negative = cash released; Positive = cash invested
```

Example:
- Year 0: 45 days receivables, 60 days inventory, 30 days payables = 75 DCC
- Year 1 (10% revenue growth): still 75 DCC but higher absolute dollars = ~7% of revenue invested

**Optimize in model:**
- Receivables: factoring, accelerated collections
- Inventory: JIT, supply chain improvements
- Payables: extend supplier terms (within reason)

---
