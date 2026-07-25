---
last_updated: "2026-03-22"
---

## Duration, Price Sensitivity & Rules of Thumb

### Macaulay Duration
The weighted average time to receive cash flows, expressed in years.

**Formula:**
```
Duration = Σ[t × PV(CF_t)] / Price

where:
  t = time in years to cash flow
  CF_t = cash flow at time t
  PV(CF_t) = present value of that cash flow
```

**Interpretation:** If bond yields change by 1%, price changes by roughly Duration %.

**Example:**
Bond with semi-annual coupons:

| Period | Time (yrs) | Cash Flow | PV at 4.5% | Weight (t × PV) |
|--------|-----------|-----------|-----------|-----------------|
| 1      | 0.5       | 5         | 4.89      | 2.45            |
| 2      | 1.0       | 5         | 4.79      | 4.79            |
| 3      | 1.5       | 5         | 4.69      | 7.04            |
| ...    | ...       | ...       | ...       | ...             |
| 10     | 5.0       | 105       | 74.55     | 372.75          |

```
Total PV (Price) = 103.50
Duration = (2.45 + 4.79 + 7.04 + ... + 372.75) / 103.50
         ≈ 4.42 years
```

### Modified Duration
The price sensitivity metric—accounts for compounding frequency.

**Formula:**
```
Modified Duration = Macaulay Duration / (1 + y/periods)

where:
  y = annual yield
  periods = coupons per year (2 for semi-annual)
```

**Example:**
```
Modified Duration = 4.42 / (1 + 0.0890/2)
                  = 4.42 / 1.0445
                  ≈ 4.23 years
```

### Price Sensitivity
How bond price changes with yield movements.

**Formula (first-order approximation):**
```
ΔPrice ≈ -Modified Duration × Δyield × Price

where:
  Δyield = change in yield (e.g., +0.01 for +100 bps)
```

**Example:**
```
Bond price: 103.50
Modified Duration: 4.23 years
Yield change: +100 bps (+0.01)

ΔPrice ≈ -4.23 × 0.01 × 103.50
       ≈ -4.38 per $100 par

New price ≈ 103.50 - 4.38 = 99.12 per $100
```

**Verification (full calculation):**
```
Old price (y = 8.90%): 103.50
New price (y = 9.90%):
  PV = 5×[1-(1.0495)^-10]/0.0495 + 100/(1.0495)^10
     ≈ 98.90
Actual price change: 98.90 - 103.50 = -4.60 (vs. -4.38 estimate)
Error: ~0.22 due to convexity (see below)
```

### Convexity
Second-order correction for larger yield changes. Reflects that the price-yield relationship is curved, not linear.

**Formula:**
```
Convexity = Σ[t(t+1) × PV(CF_t)] / [Price × (1+y)²]
```

**Price change with convexity:**
```
ΔPrice ≈ -Modified Duration × Δyield × Price + Convexity × (Δyield)² × Price
```

**Example (using 100 bps move above):**
```
Convexity ≈ 25 (typical for 5-year bond)

ΔPrice ≈ -4.38 + 25 × (0.01)² × 103.50
       ≈ -4.38 + 0.26
       ≈ -4.12

Revised estimate: 103.50 - 4.12 = 99.38
(vs. actual 98.90 → still slightly off due to 3rd+ order terms)
```

**Convexity characteristics:**
- **Positive convexity:** price goes up more if yields down, down less if yields up (good for investor)
- **Negative convexity:** price goes up less if yields down, down more if yields up (bad for investor)
  - Typical of **callable bonds** near the call price
  - Issuer has incentive to call when rates fall
  - Investor loses upside from falling rates

**Callable bonds in leveraged finance:**
- Typically have **negative convexity** at lower yields
- Reduces yield advantage of call-protected period
- Important to include in risk models

### Duration Estimates by Bond Type

| Bond Type | Duration Range | Notes |
|-----------|----------------|-------|
| 1-year bond | 0.9 - 1.0 years | Near maturity |
| 5-year par | 4.2 - 4.5 years | ~coupon/2 shorter than maturity |
| 10-year par | 8.0 - 8.5 years | |
| 10-year deep discount | 9.0 - 9.8 years | Longer duration; more sensitivity |
| 5-year callable @ 103 | 2.5 - 3.5 years | Call risk shortens duration |
| Floating-rate (3M SOFR) | < 0.3 years | Reprices frequently |

### Quick Estimation: Duration × Yield Change = Price Impact
```
Bond modified duration: 4.5 years
Yield +100 bps (+1%): Price drops ~4.5%
Yield -50 bps (-0.5%): Price rises ~2.25%
(First-order approximation; convexity adjusts for large moves)
```

---
