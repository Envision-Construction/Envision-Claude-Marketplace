---
last_updated: "2026-03-21"
---

## Yield Calculations

### Current Yield
The simplest yield metric—annual coupon divided by current price.

**Formula:**
```
Current Yield = Annual Coupon Payment / Clean Price
```

**Example:**
- Annual coupon: $100,000
- Clean price: $103.50 per $100 = $1,035,000 total
- Current Yield = $100,000 / $1,035,000 = 9.66%

**Limitation:** Ignores price appreciation/depreciation at maturity; useful for quick estimates only.

### Yield to Maturity (YTM)
The internal rate of return if bond is held to maturity; the discount rate that sets present value of all cash flows equal to current price.

**Formula (solve for r):**
```
Price = Σ[C/(1+r)^t] + Par/(1+r)^n

where:
  C = coupon per period
  r = yield per period
  n = number of periods
```

**Iterative Solution Process:**
Since this is a polynomial equation, use Newton-Raphson iteration or financial calculator:

1. Guess initial yield (often start with current yield)
2. Calculate PV of all cash flows at guessed yield
3. If PV > Price: yield is too low, increase guess
4. If PV < Price: yield is too high, decrease guess
5. Iterate until PV ≈ Price (within $0.01 per $100 par)

**Excel/Python approach:**
```python
from scipy.optimize import newton_krylov
import numpy as np

def bond_pv(y, coupons, par, periods):
    """Calculate bond PV given yield"""
    cf = np.array(coupons + [par])
    t = np.arange(1, len(cf) + 1)
    return np.sum(cf / (1 + y)**t)

def find_ytm(price, coupons, par, periods, guess=0.05):
    """Find YTM using Newton-Raphson"""
    f = lambda y: bond_pv(y, coupons, par, periods) - price
    ytm = newton_krylov(f, guess)
    return ytm
```

**Example (by iteration):**
- Bond price: $103.50 per $100 par
- Semi-annual coupon: 5% (10 periods, 5 years)
- Par: 100

```
Try y = 4% per period:
  PV = 5×[1-(1.04)^-10]/0.04 + 100/(1.04)^10
     = 5×8.111 + 67.56
     = 40.555 + 67.56
     = 108.1  (too high)

Try y = 4.5% per period:
  PV = 5×[1-(1.045)^-10]/0.045 + 100/(1.045)^10
     = 5×7.913 + 64.39
     = 39.565 + 64.39
     = 103.96  (close!)

YTM ≈ 4.45% per period = 8.90% annual
```

### Yield to Call (YTC)
Same calculation as YTM, but substitute the call date for maturity and the call price for par value. Assumes issuer calls bond on specified date.

**Formula:**
```
Price = Σ[C/(1+r)^t to call date] + Call Price/(1+r)^(periods to call)

Solve for r = YTC
```

**Example:**
- Bond price: $103.50 per $100
- Semi-annual coupon: 5%
- Call date: 3 years from now (6 periods)
- Call price: 102

```
103.50 = Σ[5/(1+r)^t, t=1 to 6] + 102/(1+r)^6

Iterating: r ≈ 4.22% per period = 8.44% annual YTC
(vs. 8.90% YTM → call reduces yield)
```

### Yield to Worst (YTW)
The **minimum** yield across all possible call scenarios. This is the investor's worst-case outcome.

**Process:**
1. Calculate YTM (assuming no call)
2. Calculate YTC for each call date in the call schedule
3. **YTW = minimum of all yields**

**Why YTW matters in leveraged finance:**
- Callable bonds limit upside if yields fall (issuer refinances)
- YTW protects investors from over-optimistic yield assumptions
- Standard metric for comparing callable bonds

**Example with Call Schedule:**
- YTM (maturity): 8.90%
- YTC (NC3, called Year 3 at 105): 8.55%
- YTC (called Year 4 at 103): 8.62%
- YTC (called Year 5 at 101): 8.75%

```
YTW = min(8.90%, 8.55%, 8.62%, 8.75%)
    = 8.55%
    (investor should assume 8.55% return, not 8.90%)
```

**When does YTW differ from YTM?**
- **Bond trading above call price** + **upcoming call dates** = YTW < YTM
- Typical in high-yield: when yields fall and refinancing becomes attractive
- If bond trades near/below call price, YTW ≈ YTM

**Practical refinancing indicator:**
```
If YTW << YTM, refinancing risk is material
→ Investor should price in call risk even if issuer hasn't announced it
```

---
