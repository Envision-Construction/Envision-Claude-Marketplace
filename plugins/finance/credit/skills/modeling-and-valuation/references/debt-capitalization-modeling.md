---
last_updated: "2026-03-21"
---

## Debt Capitalization Modeling

### Debt Schedule Setup
**Create a detailed schedule listing every debt tranche:**

| Tranche | Face Amount | Coupon | Maturity | Amortization | Ranking |
|---|---|---|---|---|---|
| Revolver | $50M | SOFR + 4.5% | 2029 | None (seasonal) | Senior Secured |
| Term Loan B | $400M | SOFR + 4.0% | 2032 | 1% annual | Senior Secured |
| First Lien Bond | $150M | 6.50% | 2031 | None | Senior Secured |
| Second Lien Bond | $100M | 8.25% | 2033 | None | Second Lien |

### Interest Expense Calculation
**Cash Interest (paid annually or quarterly):**
```
Cash Interest = Debt Balance × Coupon Rate
```

**PIK Interest (paid-in-kind, added to principal):**
```
PIK Interest = Debt Balance × PIK Rate
Ending Debt Balance = Beginning Balance + PIK Interest
```

Typical structure:
- Bank debt (revolver, term loans): cash interest only
- Bonds: usually cash; some distressed bonds include PIK toggle option
- Mezzanine: often PIK interest

### Mandatory Amortization Payments
```
Mandatory Amortization = Debt Balance × Amortization %
```

Example: $400M term loan with 1% annual amortization = $4M principal paydown each year

Track separately from voluntary prepayments (see below).

### Cash Flow Sweeps & Prepayments
**Typical sweep language (Senior Secured bank debt):**
```
50% of Excess Free Cash Flow applied to Term Loan B prepayment
```

Meaning:
- Calculate Free Cash Flow after all operating and maintenance CapEx
- Excess FCF = FCF - Minimum Cash Retention (e.g., $25M)
- 50% of Excess FCF prepays term loan
- Remaining 50%: retained for dividend, growth, debt reduction

**In base case:** assume FCF + sweep drives deleveraging over time
**In stress case:** limited/no sweep if FCF is consumed by working capital or CapEx

### Revolver Modeling
**Seasonal or event-driven draws:**

```
Revolver Balance = Working Capital Needs + Buffer
```

- **Working capital need**: (Receivables Days + Inventory Days - Payables Days) × Daily Revenue
- **Buffer**: lenders typically require 10-15% headroom above peak need
- **Borrowing base**: often tied to collateral (receivables × % + inventory × %)
- **Model draws/repayments**: revolver is repaid when working capital needs decline

**Example:**
- Q1: Draw $20M for seasonal inventory
- Q2: Peak receivables, maintain $35M drawn
- Q3-Q4: Receivables convert, repay to $15M minimum

---
