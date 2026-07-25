---
last_updated: "2026-03-21"
---

## Liquidity Analysis: Assessing Short-Term Survival

Liquidity is the ability to meet near-term cash obligations (next 12 months).

### Components of Liquidity

**Available liquidity = Cash on hand + Undrawn revolver capacity - Letter of Credit reserves**

**Example:**
- Cash on hand: $25M
- Revolver size: $100M
- Revolver drawn: $20M
- Letters of credit: $5M
- Available liquidity = $25M + ($100M - $20M - $5M) = $25M + $75M = **$100M**

### Upcoming Maturities and Required Payments

List near-term obligations:

| Due | Amount | Type |
|-----|--------|------|
| Within 6 months | $10M | Revolver interest |
| 6-12 months | $15M | Term loan payment (scheduled amortization) |
| 12 months | $50M | Senior notes maturing |
| Within 12 months | $75M | **Total** |

If available liquidity is $100M and near-term obligations are $75M, cushion = $25M. Comfortable? Depends on FCF generation in those 12 months.

### Covenant Compliance Headroom

**Leverage ratio covenant:** Total Debt / EBITDA ≤ 4.5x

**Example:**
- Net Debt: $450M
- LTM EBITDA: $110M
- Current Leverage = 4.09x
- Covenant limit: 4.5x
- **Headroom: 41bp (basis points) or ~0.4x**

Low headroom means:
- Little room for EBITDA decline
- Covenant waiver risk if EBITDA misses
- Higher refinancing risk

### Cash Generation Capacity

Assess how much FCF the business can generate in the next 12 months.

**Use the FCF waterfall:**
1. Start with LTM EBITDA (or forward guidance if available)
2. Subtract cash interest and taxes
3. Subtract maintenance CapEx
4. Adjust for expected working capital changes
5. Result: Expected 12-month FCF available for debt paydown

**Example:**
- Expected 12-month EBITDA: $110M
- Less: Cash interest: (15M)
- Less: Cash taxes: (11M)
- Less: Maintenance CapEx: (8M)
- Plus: Working capital benefit (seasonal reduction): 3M
- **Expected FCF: $79M**

Combine with available liquidity:
- Liquidity: $100M + FCF generation: $79M = $179M available to meet $75M near-term obligations
- Comfortable position with $104M cushion

---

## Covenant Compliance Modeling

### Maintenance Covenants (Bank Loans)

**Leverage Test (Maximum Debt/EBITDA):**
```
Covenant Test: (Total Debt - Cash) / EBITDA < X.Xx
```

**Coverage Test (Minimum EBITDA/Interest):**
```
Covenant Test: EBITDA / (Interest Paid + Amortization) > X.Xx
```

### Covenant Step-Downs
Bank agreements typically include **step-down schedules:**

```
Year 1-2: Maximum Leverage 5.0x -> Minimum Coverage 2.5x
Year 3-4: Maximum Leverage 4.5x -> Minimum Coverage 2.8x
Year 5+:  Maximum Leverage 4.0x -> Minimum Coverage 3.0x
```

**Implication:** Company must improve ratios over time or refinance to loosen covenants.

### Headroom Calculation
```
Headroom = Covenant Threshold - Actual Ratio
```

**Example:**
- Max Leverage covenant: 4.5x
- Actual Leverage: 4.1x
- Headroom: 0.4x or ~9% cushion

**Interpretation:**
- Headroom < 0.2x: very tight, high refinancing risk
- Headroom 0.2x - 0.5x: adequate but monitor
- Headroom > 0.5x: comfortable cushion

### Rule of Thumb: Bank Cushion
Lenders typically build in **20-25% cushion** over company's internal (conservative) base case projections.

Example:
- Company's stress case: 3.8x leverage in Year 1
- Bank covenant: 5.0x (provides ~25% cushion)
- If company's case deteriorates, covenant becomes at-risk

### Covenant Compliance in Each Scenario

**Model actual covenant compliance:**

| Covenant | Threshold | Year 1 Base | Year 1 Downside | Year 1 Upside | Status |
|---|---|---|---|---|---|
| Max Leverage | 5.0x | 3.8x | 4.8x | 3.1x | All pass |
| Min Coverage | 2.5x | 3.8x | 2.6x | 5.2x | Downside marginal |

**Downside analysis:**
- If downside case breaches covenant, evaluate:
  - **Equity cure:** Can equity sponsor inject $X million to reduce debt below threshold?
  - **Amendment negotiation:** Can lenders/sponsors renegotiate covenant levels?
  - **Asset sale:** Can company raise cash to reduce debt?

### Equity Cure Mechanics
Many bank agreements allow equity sponsor to **cure a covenant breach** by injecting equity:

```
Equity Injection -> Reduces Total Debt -> Improves Leverage Ratio
Example: $50M equity injection can reduce leverage by ~0.1-0.2x if EBITDA is $250M+
```

---
