---
last_updated: "2026-03-21"
---

## Core Pricing & Accrued Interest

### Bond Price Calculation
Bond prices are quoted as a percentage of par (100 = par value, the face amount).

**Formula:**
```
Price = Σ[Coupon/(1+y)^t] + Par/(1+y)^n
where:
  Coupon = annual coupon payment (e.g., 5% annual = $50 per $1,000 par)
  y = yield to maturity per period
  t = period number (1, 2, 3, ...)
  n = total number of periods
  Par = face value (typically 100 for % price)
```

**Practical Example:**
- Face value: $1,000,000
- Coupon rate: 10% annual (paid semi-annually = 5% per period)
- Years to maturity: 5 years (10 periods)
- Yield: 8% annual (4% per period)

```
Price = Σ[50/(1.04)^t for t=1 to 10] + 100/(1.04)^10
      = 50×[1-(1.04)^-10]/0.04 + 100×(1.04)^-10
      = 50×8.111 + 100×0.6756
      = 405.55 + 67.56
      = 473.11 (in terms of per-$100 par)
      = $4,731,100 total (bond trading at premium to par at lower yield)
```

### Accrued Interest Calculation
Accrued interest is the portion of the next coupon that has accumulated since the last payment date.

**Formula (30/360 day count convention):**
```
Accrued Interest = (Coupon Rate × Face Value) × (Days Since Last Coupon / 360)
```

**Day Count Convention - 30/360:**
- Each month = exactly 30 days
- Year = exactly 360 days
- If month-end falls on 31st, use 30th
- February always counted as 30 days

**Example:**
- Face value: $1,000,000
- Coupon rate: 10% annual
- Last coupon payment: 90 days ago
- Days since last coupon: 90

```
Accrued Interest = $1,000,000 × 0.10 × (90/360)
                 = $1,000,000 × 0.10 × 0.25
                 = $25,000
```

### Clean Price vs Dirty Price

**Clean Price (Quote Price):**
The price quoted in the market, excludes accrued interest.

**Dirty Price (Full Price/Invoice Price):**
What the buyer actually pays.

**Formula:**
```
Dirty Price = Clean Price + Accrued Interest
```

**Example:**
- Clean price: 103.50 (per $100 par)
- Face value: $1,000,000
- Accrued interest: $25,000 (calculated above)

```
Clean price amount = $1,000,000 × (103.50/100) = $1,035,000
Dirty price = $1,035,000 + $25,000 = $1,060,000
```

---
