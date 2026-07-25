---
last_updated: "2026-03-21"
---

## Quick Refinancing Check Framework

Practical approach to assess if a bond is likely to be refinanced:

### Step 1: Estimate Refinancing Cost
Use the current bond's call price as a proxy for what the issuer would pay to retire it.

**Example:**
```
Existing bond: 10% coupon, currently at 105 per $100 par
Call price: 103 per $100 (3 years until par)

Take call price (103) as proxy for refinancing cost
(This assumes issuer would call existing bond at 103)
```

### Step 2: Estimate New Coupon
Use the existing bond's YTW (not the market rate) as a proxy for new coupon market.

**Logic:**
- If existing bond's YTW = 8.5%, that reflects current market credit spreads
- New issuance would likely be priced at similar yield
- Assume new coupon ≈ YTW

**Example:**
```
Existing bond YTW: 8.5%
Assume new bond would need 8.5% coupon to sell at par

(Or use current market rates if issuer's credit profile likely to improve)
```

### Step 3: Compare Interest Costs
Calculate annual savings (or costs) from refinancing.

**Example:**
```
Existing coupon: 10.0% on $100M = $10.0M annual
New coupon estimate: 8.5% on $100M = $8.5M annual
Gross annual savings: $10.0M - $8.5M = $1.5M

Refinancing cost: Call price 103 vs. par = $3M premium
Net NPV over remaining life:
  If 5 years remaining: $1.5M × 5 years = $7.5M savings
  Minus $3M call cost = $4.5M net benefit

  → Refinancing looks attractive
```

### Step 4: Consider Transaction Costs & Execution
Real-world factors:

| Factor | Adjustment |
|--------|------------|
| Underwriting fees | -0.5% to 1.0% of amount |
| Legal & rating agency fees | -0.1% to 0.2% of amount |
| New issuer pricing pop | Can reduce cost or create profit |
| Market windows | Timing risk; rates may rise before closing |
| Covenant violations | May prohibit refinancing without waiver |

**Refined example:**
```
Gross refinancing cost: $3.0M (call premium)
Plus fees (~0.75%): $0.75M
Total cost: $3.75M

Annual savings: $1.5M
Remaining life: 5 years
Break-even: $3.75M / $1.5M = 2.5 years

If rates stay stable and credit stable, refinance in year 3
If rates drop further, refinance sooner
If rates rise, likely not refinance (existing 10% becomes attractive)
```

### When is Refinancing Worth It?
Use this heuristic:

```
NPV of Refinancing = Σ[Annual Savings] - Refinancing Cost

If NPV > 0 and rates appear stable, refinancing is likely
If NPV < 0, issuer will hold to maturity unless credit deteriorates
If rates likely to fall further, refinance sooner (option value)
If rates likely to rise, hold (saves refinancing cost if rates rise)
```

---
