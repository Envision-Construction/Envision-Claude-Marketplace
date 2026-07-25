---
name: Distress Diagnosis and Liquidity
description: |
  Root-cause diagnosis for why companies become distressed and forensic liquidity analysis
  for determining when a distressed company will run out of cash.
last_updated: "2026-03-22"
---

## Why Companies Become Distressed

### Root Cause #1: Operational Decline
Companies deteriorate when fundamentals weaken:
- **Revenue erosion**: Competition intensifies, market share lost, customer concentration risk hits
- **Secular change**: Industry disruption, technology shifts, consumer preference shifts render business model obsolete
- **Cost spikes**: Commodity price surge, labor cost inflation, regulatory expenses spike unexpectedly
- **Strategy failures**: Bad capital allocation, failed acquisitions, wrong market positioning

The result: EBITDA drops, leverage ratios spike, coverage ratios deteriorate.

### Root Cause #2: Overleveraged Balance Sheet
The "good company with a bad balance sheet" scenario:
- Company has decent operations but took on debt beyond sustainable levels
- Common in LBOs: too much financial engineering, debt-funded dividends, overleveraged M&A
- The business could work with less debt, but leverage leaves no margin for error
- Any operational hiccup triggers cash flow coverage failure

### Root Cause #3: Deferred Payment Structures
PIK (paid-in-kind) and zero-coupon securities create hidden debt growth:
- **PIK bonds**: Interest paid in additional bonds rather than cash → debt principal grows while cash flow static
- **Zero-coupon bonds**: No coupon paid, bond accretes at specified rate → debt grows mathematically without cash burn
- **Bridge loans structured as PIK at exit**: never paid down, interest capitalizes
- Problem: Debt burden keeps growing while company's cash-generating ability stagnates
- Eventually, refinancing window closes and company hits wall

### Root Cause #4: Combined Deterioration
Worst case: bad operations + overleveraged structure
- Operational decline narrows cash available for debt service
- High leverage leaves no cushion for missed targets
- Refinancing becomes impossible as credit metrics worsen
- Path to distress accelerates

---

## Liquidity Analysis for Distressed Credits

Normal credit analysis looks at coverage ratios over 12-24 months. Distressed credit analysis is forensic: **when exactly does the company run out of cash?**

### Key Timing Considerations

**Payment Schedule Lumpiness**:
- Bank debt: monthly or quarterly interest payments (regular, predictable)
- Bond debt: semiannual coupon payments (lumpy, bi-annual events)
- Bullet maturity: large lump-sum principal due on specific date
- Example: A company with $100M quarterly EBITDA but $75M semiannual bond coupon due in 30 days faces a temporary liquidity crunch even if annual coverage looks OK

**Revenue Seasonality**:
- When does cash actually flow in? Q4 surge? Summer drought?
- Critical for retail, construction, agriculture, tourism
- Tax refunds, government fiscal calendar can matter for service providers
- A company might be EBITDA-positive on annual basis but cash-negative in weak quarters
- Key question: Can the company bridge seasonal gaps with working capital lines?

### Liquidity Sources and Availability

**Asset Sales**:
- Can non-core assets be sold quickly? (plants, real estate, minority stakes)
- Is there a market for assets? Fire-sale discounts may be 20-40% vs. strategic buyer price
- Real estate: sale-leaseback converts equity into cash but locks in long-term lease obligations
- Inventory liquidation: retailers can sell excess inventory at discounts (generates cash but loses margin)

**Receivables Securitization**:
- Can accounts receivable be monetized? (supply chain finance, securitization)
- Requires receivables of stable quality and size
- Credit card processors, healthcare providers, telecom commonly use this
- Distressed companies: receivables may be questioned (customer credit quality deteriorating?)

**Revolver Availability**:
- Is there an undrawn revolving credit facility?
- How much capacity remains? ($50M revolver with $40M drawn = $10M available)
- Covenant compliance: are there financial maintenance covenants that block additional borrowing?
  - Leverage ratio covenant: if net leverage is already at 6.0x and covenant is 6.25x, only small additional draw possible
  - Interest coverage covenant: if EBITDA/Interest approaching 2.0x min and covenant is 2.5x, limited room to take on new debt
- Lenders' willingness: in distressed situations, lenders may refuse to fund revolver draws even if covenant-compliant (especially if lender has doubts)

**Outside Investors**:
- Can the company attract new equity capital or sponsor support?
- Sponsor cliff: when does financial sponsor walk away? (board seat pressure, economics unfavorable)
- Strategic investor: can a buyer inject capital before full bankruptcy?

### Identifying the "Wall" — When Cash Runs Out

**Cash Flow Projection**:
1. Build 13-week rolling cash flow forecast (monthly detail for distressed situations)
2. Include all payment obligations: payroll, utilities, trade payables, debt service, taxes, working capital needs
3. Project revenue based on current run-rate, seasonality, and trends
4. Calculate weekly/monthly surplus or deficit
5. Project when cumulative cash balance hits critical level (operational minimum cash needed)

**Cash Minimum Threshold**:
- Every company needs minimum cash for operations: payroll float, working capital, contingencies
- Too low: company cannot operate, suppliers stop delivering
- Typical range: 10-15 days of operating expenses for stable companies
- Distressed companies: often operate on razor-thin margins (5-7 days)

**Example from Practice**:
- Widget Manufacturing: $30M annual EBITDA, $2.5M monthly cash burn
- $25M bond coupon due in 6 weeks
- Current cash: $8M, minimum operational cash needed: $5M
- Available liquidity (cash + undrawn revolver): $18M
- 6-week burn = $15M (6 weeks x $2.5M)
- Projected cash at coupon date: $18M - $15M = $3M (below $5M minimum)
- **Conclusion: Company will miss coupon or require emergency financing**

---
