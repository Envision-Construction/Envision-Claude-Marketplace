---
last_updated: "2026-03-21"
---

## Delayed Compensation — Economic Adjustment for Timing

### The Delayed Compensation Problem
Economic ownership of a loan transfers on **trade date (T)**, but **settlement** (cash payment) occurs **T+7 or later**. This creates an economic mismatch:
- From trade date to settlement date, the buyer is economically entitled to interest accruals
- From trade date to settlement date, the seller is still on the hook for interest payments to the borrower
- Without adjustment, one party is economically disadvantaged

**Delayed compensation** solves this by adjusting the purchase price to account for the gap.

### Mechanics of Delayed Compensation Calculation

**Scenario**: 3-month SOFR + 300bps term loan, $100M par, trading at 99.00
- Trade date: Monday, March 3
- Settlement date: Monday, March 10 (T+7)
- Current SOFR: 5.50%, so all-in rate = 8.50%
- Daily interest: ($100M × 8.50%) / 360 = $23,611

**Calculation method**:
1. Identify delayed compensation period: March 3 (trade date) through March 7 (day before settlement, not including settlement day)
2. Count business days in period: 5 business days
3. Calculate accrued interest for this period: $23,611 × 5 = $118,055
4. Adjust purchase price: Buyer pays 99.00 + 0.118055% = 99.118055

Buyer pays seller the daily accrued interest from trade date to settlement date because buyer is economically entitled to this accrual.

### Cost-of-Carry Rate for Extended Settlement
If settlement is delayed BEYOND the standard T+7 or T+20 timeline (e.g., settlement moves to T+15 due to documentation delays):
- Seller compensates buyer for **cost of carry** (financing cost of holding the position from standard settlement date through actual settlement date)
- Cost-of-carry rate is typically **federal funds rate** (overnight rate) plus a small spread
- Calculation: (Actual settlement date - standard settlement date) × daily cost-of-carry rate × loan par amount

**Example**: Trade settles on T+15 instead of T+7 (8-day delay)
- Federal funds rate: 5.25%
- Cost-of-carry: FF + 25bps = 5.50%
- Daily cost of carry: ($100M × 5.50%) / 360 = $15,278
- Total carry cost: $15,278 × 8 = $122,222
- Seller pays buyer $122,222 as delayed compensation

### Alternatives to Delayed Compensation
In some cases, parties negotiate **trade-date and settlement-date adjustments** differently:
- **Seller prepays interest**: Seller pays buyer accrued interest directly (not through purchase price adjustment)
- **Price-inclusive**: Parties agree to a price that implicitly includes the interest compensation
- **Flat settlement**: Buyer accepts price without adjustment; rarely used in modern markets

### Regulatory Representations Regarding Delayed Compensation
Most LSTA standard terms require both parties to represent that:
- Neither party is relying on delayed compensation to create an investment return (regulatory compliance)
- Transaction is not being structured to evade investment company act registration
- Delayed compensation is solely for the purpose of economic adjustment

These reps reflect SEC concerns about using delayed compensation improperly to create unregistered securities.

---
