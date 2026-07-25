---
last_updated: "2026-03-21"
---

## Practical Calculation Workflows

### Workflow 1: Quick Bond Valuation (at a glance)

**Input:**
- Par value
- Annual coupon (%)
- Time to maturity (years)
- Current yield (investor's required return)

**Steps:**
1. Convert annual coupon to per-period: coupon / 2 (semi-annual)
2. Convert annual yield to per-period: yield / 2
3. Count periods: years × 2
4. Use formula: Price = Coupon×[1-(1+y)^-n]/y + Par/(1+y)^n
5. Express as % of par

**Example:**
- Par: $1M, Coupon: 8%, Years: 5, Yield: 6%

```
Period coupon: 8% / 2 = 4% per $100 par
Per-period yield: 6% / 2 = 3%
Periods: 5 × 2 = 10

Price = 4×[1-(1.03)^-10]/0.03 + 100/(1.03)^10
      = 4×9.229 + 74.41
      = 36.92 + 74.41
      = 111.33 per $100 par

Total bond value: $1M × (111.33 / 100) = $1,113,300
```

### Workflow 2: YTW Calculator (Callable Bond)

**Input:**
- Bond price (per $100 par)
- Semi-annual coupon (%)
- YTM calculation inputs
- Call schedule: [(Years, Call Price), ...]

**Steps:**
1. Calculate YTM (solve for r using maturity date and par)
2. For each call date: Calculate YTC (solve for r using call date and call price)
3. Find minimum yield = YTW

**Example:**
- Price: 104, Coupon: 5%, Call schedule: [(3, 102), (4, 101), (5, 100)], Maturity: 7 years

```
YTM (7 years, par 100): ~4.2%
YTC Year 3 (at 102): ~3.8%
YTC Year 4 (at 101): ~3.9%
YTC Year 5 (at 100): ~4.0%

YTW = min(4.2%, 3.8%, 3.9%, 4.0%) = 3.8%
```

### Workflow 3: Spread-to-Worst Calculation

**Input:**
- Bond YTW (from Workflow 2)
- Treasury yield at YTW settlement date

**Steps:**
1. Identify YTW (the scenario with lowest yield)
2. Note the date when that lowest yield occurs
3. Find Treasury yield for that maturity
4. STW = YTW - Treasury yield

**Example:**
```
YTW = 3.8% (occurs in Year 3 call scenario)
3-year Treasury yield = 2.5%
STW = 3.8% - 2.5% = 130 bps
```

### Workflow 4: Floating-Rate Bond Pricing

**Input:**
- Par
- Reference rate (SOFR) + spread
- Spread
- SOFR floor (if any)
- Years to maturity

**Steps:**
1. For each reset period, calculate coupon: max(SOFR floor, current SOFR) + spread
2. Apply discount at DM (discount margin) to solve for price
3. If trading near par, price ≈ par (floating-rate repricing)

**Example:**
- Par: $100, Coupon: SOFR + 2.5%, SOFR floor: 1.5%, Current SOFR: 5.0%
- Years to maturity: 3

```
Current coupon: max(1.5%, 5.0%) + 2.5% = 7.5%
Since repricing in 6 months, price ≈ 100 (par)
Next period: SOFR resets; coupon adjusts automatically

Risk: If SOFR drops to 0.5%, coupon = 1.5% + 2.5% = 4.0% (floor bites)
Value of embedded floor: Issuer saves (1.5% - 0.5%) = 1.0% if SOFR falls that far
```

### Workflow 5: PIK Accrual & Tax Impact

**Input:**
- Par
- PIK rate (annual %)
- Years to maturity
- Investor's marginal tax rate

**Steps:**
1. Calculate accreted value: Par × (1 + PIK Rate)^years
2. Accrued interest each year: Par × (1 + PIK Rate)^(year-1) × PIK Rate
3. Tax due annually: Accrued interest × Tax Rate (cash outflow)
4. Net return after tax impact

**Example:**
```
Par: $100,000
PIK rate: 12% annually
Years: 5
Tax rate: 35%

Year 1 accrued: $100,000 × 0.12 = $12,000
  Tax due: $12,000 × 35% = $4,200 (out of pocket!)

Year 2 accrued: $112,000 × 0.12 = $13,440
  Tax due: $13,440 × 35% = $4,704

(Pattern: tax bill grows with accreted principal)

Total tax over 5 years: ~$33,400
Accreted value at maturity: $100,000 × (1.12)^5 = $176,234
Investor receives $176,234 less cumulative $33,400 taxes paid
Effective return reduced from 12% to ~8% after tax drag
```

---
