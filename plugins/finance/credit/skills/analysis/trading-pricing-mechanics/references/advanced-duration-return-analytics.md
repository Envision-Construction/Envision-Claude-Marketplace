---
last_updated: "2026-03-21"
---

## Advanced Duration & Return Analytics

### Effective Duration vs. Modified Duration

**Modified Duration** assumes fixed cash flows and is calculated as the weighted average time to cash flows, adjusted for yield:

```
Modified Duration = Macaulay Duration / (1 + Yield/Frequency)

Works well for: bullet bonds, amortizing loans with fixed schedule
Limitation: Assumes cash flows do not change when yields move
```

**Effective Duration** recalculates cash flows at shifted rate levels, capturing the value of embedded options:

```
Effective Duration = (P_down − P_up) / (2 × P₀ × Δy)

Where:
  P_down = bond price after parallel rate shift DOWN by Δy (e.g., −50 bps)
  P_up = bond price after parallel rate shift UP by Δy (e.g., +50 bps)
  P₀ = current market price
  Δy = rate shift magnitude (typically 25–50 bps)

Works for: callable bonds, MBS, floating-rate instruments, any bond with state-dependent cash flows
```

**Procedure for callable bonds**:
1. Assume current yield of 8.5%, trading at 101 (premium)
2. Shift Treasury curve down 50 bps; recalculate bond price assuming issuer has call at 100
   - At lower rates, issuer more likely to call → price capped at call price (102 hypothetically)
   - P_down = 101.5 (limited upside due to call option)
3. Shift Treasury curve up 50 bps; recalculate bond price
   - At higher rates, issuer unlikely to call → normal price appreciation
   - P_up = 99.2 (full downside exposure)
4. Effective Duration = (101.5 − 99.2) / (2 × 101 × 0.005) = 2.3 / 1.01 = **2.28 years**

**Comparison to Modified Duration**:
```
If modified duration were 4.5 years (no option adjustment),
Effective duration of 2.28 years shows the call option has shortened
the investor's effective duration by more than half.
This is the key cost of owning callable bonds.
```

**When to use**:
- **Modified duration**: Bullets, straight bonds, non-callable instruments
- **Effective duration**: Callable HY bonds, MBS, any structured product with embedded option or path-dependent cash flows

---

### Negative Convexity

Bonds trading above the call price exhibit **negative convexity**—price upside is capped by the call, while downside is not.

**Convexity Definition**:

```
Convexity = (P_down + P_up − 2 × P₀) / (P₀ × Δy²)

Positive convexity: Investors benefit from price curvature (price gains from down move > price losses from up move)
Negative convexity: Investors penalized by price curvature (price gains from down move < price losses from up move)
```

**Example (callable bond at 104 with 100 call price)**:

```
Current price (P₀): 104
Scenario 1: Rates down 100 bps
  − Without call: Price would rise to 108 (full duration effect)
  − With call: Issuer calls at 100, investor receives 100
  − P_down = 100 (capped by call)

Scenario 2: Rates up 100 bps
  − Without call: Price would fall to 100
  − With call: Call option worthless, price falls normally
  − P_up = 100 (coincidentally; full downside)

Effective Duration = (100 − 100) / (2 × 104 × 0.01) = 0 / 2.08 = 0

This extreme example shows zero effective duration because price is pinned at call price.

Modified Duration (if no call): ~5 years
Effective Duration (with call): ~0 years
→ Massive difference due to negative convexity

Convexity = (100 + 100 − 2 × 104) / (104 × 0.01²)
          = −8 / 0.0104
          = −769 (deeply negative)
```

**Economic consequences of negative convexity**:
- When rates rally (market rates fall): Issuer calls the bond → investor's profit capped at call price. The investor misses the market appreciation.
- When rates sell off (market rates rise): Call option expires worthless → investor faces full principal loss. No protection from the option.
- Net result: Investor "short" an option (sold call to issuer). Pays in both directions.

**Quantitative cost of negative convexity** (option cost):

```
Option Cost = Z-spread − OAS

Z-spread: Spread that discounts cash flows at fixed (expected) prepayment speed
OAS: Spread after stripping out option value

Example:
  Callable bond at 104, Z-spread 250 bps, OAS 200 bps
  Option Cost = 250 − 200 = 50 bps

Investor is paying 50 bps annually (in yield terms) to own the embedded call option risk.
This is the insurance premium for call risk.
```

**How to identify negative convexity bonds**:
- Trading near or above the call price
- Upcoming call dates (refinancing likely if rates fall further)
- Spread appears tight relative to credit fundamentals (underpricing credit risk because of duration compression from call)

**Mitigation strategies**:
- Avoid at-the-money and in-the-money callable bonds unless yield significantly higher to compensate
- Pair with interest-rate hedges (buy interest rate floors, long duration instruments)
- Target deep discount callables where call is far out of the money (option cost minimal)

---

### Key Rate Duration Profile

**Effective duration** (single number) masks important rate risk in barbells, callable bonds, and complex structures. **Key rate duration (KRD)** isolates sensitivity at each point on the yield curve.

**KRD Methodology**:
1. Identify key maturity points on the yield curve: 2yr, 5yr, 10yr, 30yr (standard grid)
2. Shift ONLY that key rate by 1 basis point (use linear interpolation for intermediate points on curve)
3. Recompute bond price (accounting for option-adjusted cash flows if callable/MBS)
4. KRD at that point = |ΔPrice| / (Price × 0.0001)

**Example: 7-year callable corporate bond**

| Key Rate | Shift | P_original | P_shifted | KRD Value | Interpretation |
|-----------|-------|-----------|-----------|-----------|-----------------|
| 2yr | −1 bp | 103.50 | 103.505 | 0.05 | Minimal front-end exposure |
| 5yr | −1 bp | 103.50 | 103.55 | 0.48 | Moderate mid-curve exposure |
| 10yr | −1 bp | 103.50 | 103.42 | −0.77 | NEGATIVE KRD! (call effect dominates) |
| 30yr | −1 bp | 103.50 | 103.48 | 0.19 | Small long-end exposure |
| **Total Eff. Duration** | — | — | — | **−0.05** | Net near zero due to call |

**Negative KRD at 10yr point**:
- This callable bond is short duration at the 10-year part of the curve
- A 1 bp drop in 10-year rates → price falls (because 7-year callable's call option becomes more valuable to issuer, lowering bond value)
- This is counterintuitive: normally, lower rates → higher prices
- But here, call option effect dominates: lower rates trigger call probability, capping price upside

**Practical applications**:

**Steepener trade** (bet that yield curve steepens: front end rallies, back end sells):
- Need negative KRD at front (benefit from rally) + positive KRD at back (exposed to selloff)
- Callable bonds provide negative KRD at front → useful for steepener
- Pair with duration hedges at long end

**Flattener trade** (bet that yield curve flattens: front end sells, back end rallies):
- Need positive KRD at front + negative KRD at back
- Deeply discounted callable bonds provide positive KRD across curve → opposite of what steepener needs
- May not be suitable for flattener

**Floating-rate loan KRD**:
```
Example: 5-year floating-rate loan, reset annually at SOFR + 300

KRD profile:
  2yr: 0.00 (next reset in ~1 year; minimal exposure)
  5yr: 4.50 (reset dates cluster at 1, 2, 3, 4 year marks; rate risk concentrated here)
  10yr: 0.00 (no reset beyond maturity)
  30yr: 0.00 (no exposure)

Interpretation: This floating-rate loan has duration exposure only at the annual reset dates.
If 5-year rates fall, the loan's required spread (300 bps) doesn't change, but the SOFR index (base rate) falls → negative carry for investor.
KRD analysis reveals rate risk lives only at reset points, not across full maturity.
```

---

### Carry & Roll-Down Analysis

**Carry** is the forward return from a bond if rates and spreads remain unchanged over the holding period.

**Three components of carry**:

#### 1. Coupon Carry (Accruing Interest)
```
Monthly Coupon Carry = Annual Coupon / 12

Example: 5% coupon bond
  Monthly coupon carry = 5% / 12 = 0.417%
  Over 6 months = 2.5%
```
Simplest component; investor automatically accrues this each month.

#### 2. Pull-to-Par (Discount Bonds Only)
As a discount bond approaches maturity, its price drifts toward par (100), generating capital gain.

```
Pull-to-Par Gain = (Par − Current Price) / Months to Maturity

Example: Discount bond at 95, maturing in 60 months
  Monthly pull-to-par = (100 − 95) / 60 = 0.083%
  6-month pull-to-par = 0.5%

For premium bonds (trading above par), this is negative (price decay toward par).
```

#### 3. Roll-Down (Spread Curve Exposure)
If the credit spread curve is upward-sloping (longer maturities trade wider), a bond "rolls down" the curve as it ages, receiving a capital gain from tighter spreads.

```
Example: Credit curve is upward-sloping:
  1-year maturity: 200 bps spread
  3-year maturity: 250 bps spread
  5-year maturity: 280 bps spread

A 3-year bond trading at 250 bps spread today:
  In 6 months (if spreads unchanged), it will be a 2.5-year bond.
  The 2.5-year point on the curve is tighter than 250 bps (interpolating between 1-yr at 200 bps and 3-yr at 250 bps)

  Estimated 2.5-year spread: ≈ 225 bps (rolled down 25 bps)
  Price change from roll-down ≈ +25 bps of spread duration × 3.5 yr duration = +0.875%
```

Roll-down gain is zero if curve is flat; negative if curve is inverted.

#### Total Monthly Carry

```
Total Monthly Carry = Coupon Carry + Pull-to-Par + Roll-Down + Reinvestment Income

Example:
  5% coupon bond, trading at 98 (1-year maturity), upward-sloping credit curve:

  Coupon carry: 5% / 12 = 0.417%
  Pull-to-par: (100 − 98) / 12 = 0.167%
  Roll-down: +0.2% (estimated from curve shape)
  Reinvestment: 0.1% (coupons reinvested at 4.5%)

  Total monthly carry = 0.417% + 0.167% + 0.2% + 0.1% = 0.884%
  Annualized = 0.884% × 12 = 10.6%
```

**Practical use**:
- High carry → comfortable holding position even if rates/spreads stable or slightly wider
- Low or negative carry → need spread tightening or rate decline to achieve target return
- Carry = "free money" if rates/spreads static; valuable cushion against adverse moves

---

### Breakeven Spread Widening

**Question**: How much can credit spreads widen over the holding period before total return becomes negative?

**Breakeven Formula**:

```
Breakeven Spread Widening = Carry / Spread Duration

Where:
  Carry = annualized carry (coupon + pull-to-par + roll-down), %
  Spread Duration = price sensitivity to 1 bp move in spread, years
```

**Example**:
```
Corporate bond, 5% coupon, trading at 102 (premium)
  Effective duration = 4.2 years
  Spread duration ≈ 4.0 years (close to effective duration for corporate bonds)
  OAS = 150 bps
  Annualized carry = 2.1% (from coupon, some negative pull-to-par because premium)

Breakeven = 2.1% / 4.0 = 0.525 = 52.5 bps annual spread widening

Interpretation: If spreads widen by 52.5 bps, total return = 0.
  If spreads widen <52.5 bps (e.g., 40 bps), investor still positive (carry covers most loss)
  If spreads widen >52.5 bps, investor negative

Conservative approach: Require breakeven of at least 75–100 bps for adequate cushion.
```

**Spread Duration Estimation** (for bonds without embedded options):
- Spread duration ≈ 70–90% of effective duration (general rule)
- More precise: Use Bloomberg or internal system to calculate price change from 1 bp spread shift

**High-yield bonds** (more spread risk):
```
HY bond, 8% coupon, trading at 100:
  Effective duration = 3.5 years
  Spread duration ≈ 3.2 years
  Carry = 5.2% (coupon minus some reinvestment at lower rates)

Breakeven = 5.2% / 3.2 = 162.5 bps annual spread widening

Higher carry → higher breakeven cushion (compensates for high spread risk)
```

**Distressed bonds** (low carry, high spread risk):
```
Distressed bond, 12% coupon, trading at 40:
  High coupon, deep discount → pull-to-par is large benefit
  Spread duration ≈ 2.0 years (short duration due to price compression)
  Carry = 15% (coupon 12% + pull-to-par 3%)

Breakeven = 15% / 2.0 = 750 bps spread widening

Enormous cushion. Even if spreads blow out (widening 300–500 bps), carry still positive.
This is why distressed bonds offer attractive risk-adjusted returns in stress scenarios.
```

---

### Total Return Framework (Bonds & Loans)

**Total return** is the all-in return over a specified holding period (typically 3, 6, or 12 months). Unlike yield to maturity (which assumes buy-and-hold to maturity), total return captures actual mark-to-market and is dependent on rate/spread moves.

**Components**:
```
Total Return = [Coupon Income + Principal Return + Price Change + Reinvestment − Financing Cost] / Initial Investment

Alternative calculation by source:
  Total Return = Carry Component + Price Component

  Carry Component (base return if rates/spreads static):
    = Coupon + Pull-to-Par + Roll-Down + Reinvestment

  Price Component (price appreciation/depreciation from rate/spread moves):
    = −Effective Duration × Δy + 0.5 × Effective Convexity × Δy²
      −Spread Duration × ΔSpread
```

**Taylor expansion for bond returns** (first-order duration, second-order convexity):
```
ΔPrice / Price ≈ −Duration × Δy + 0.5 × Convexity × Δy²
                 −Spread Duration × ΔSpread

Where:
  Δy = change in yield (parallel shift), % (e.g., +0.01 for +100 bps)
  ΔSpread = change in spread, % (e.g., −0.003 for −30 bps tightening)
  Convexity = second derivative of price w.r.t. yield
```

**Example: 5-year corporate bond**

**Bond data**:
- Price: 102.5
- Coupon: 4.5%
- Yield: 3.8%
- Effective Duration: 4.3 years
- Effective Convexity: +65
- Spread Duration: 4.0 years
- OAS: 140 bps
- 6-month carry: 1.5%

**Scenario 1: Rates flat, spreads unchanged (base case)**
```
Price change from rates: 0 (flat)
Price change from spreads: 0 (flat)
Total return = Carry = 1.5%
```

**Scenario 2: Rates fall 50 bps, spreads unchanged**
```
Price change from rates:
  = −4.3 × (−0.005) + 0.5 × 65 × (−0.005)²
  = +0.0215 + 0.5 × 65 × 0.000025
  = +0.0215 + 0.000813
  = +0.0223 = +2.23%

Price change from spreads: 0 (unchanged)

Total return = Carry (1.5%) + Rate price gain (2.23%) = 3.73%
```

**Scenario 3: Rates unchanged, spreads widen 30 bps**
```
Price change from rates: 0
Price change from spreads:
  = −4.0 × (+0.003) = −0.012 = −1.2%

Total return = Carry (1.5%) + Spread loss (−1.2%) = 0.3%
```

**Scenario 4: Rates rise 100 bps, spreads widen 50 bps (recession)**
```
Price change from rates:
  = −4.3 × (+0.01) + 0.5 × 65 × (+0.01)²
  = −0.043 + 0.5 × 65 × 0.0001
  = −0.043 + 0.00325
  = −0.0398 = −3.98%

Price change from spreads:
  = −4.0 × (+0.005) = −0.02 = −2.0%

Total return = Carry (1.5%) + Rate loss (−3.98%) + Spread loss (−2.0%) = −4.48%
```

#### Scenario Matrix for Corporate Bonds

Create a table showing total return across rate and spread scenarios:

| Rate / Spread Change | −50 Sp Tight | −25 Sp | Flat | +25 Sp Wide | +50 Sp Wide |
|---|---|---|---|---|---|
| **−100 bps down** | +7.8% | +6.8% | +5.8% | +4.8% | +3.8% |
| **−50 bps down** | +5.3% | +4.3% | +3.3% | +2.3% | +1.3% |
| **Flat (+0 bps)** | +2.8% | +1.8% | +0.8% | −0.2% | −1.2% |
| **+50 bps up** | +0.3% | −0.7% | −1.7% | −2.7% | −3.7% |
| **+100 bps up** | −2.2% | −3.2% | −4.2% | −5.2% | −6.2% |

**Interpretation**:
- **Upper-left quadrant (rates down, spreads tighten)**: Bull case; highest returns (+7–8%)
- **Center cell (rates/spreads flat)**: Base case return (~0.8% from carry)
- **Lower-right quadrant (rates up, spreads widen)**: Bear case; highest losses (−5 to −6%)
- **Diagonal from lower-left to upper-right**: Least favorable outcomes (rates up but spreads tight, or rates down but spreads widen) → intermediate returns

**Portfolio positioning decision**:
- **Bullish outlook**: Overweight bonds with high carry, shorter duration (more convexity benefit from rate fall)
- **Bearish outlook**: Reduce duration, raise cash, rotate to shorter-maturity bonds
- **Neutral**: Ladder maturities, ladder credit quality, balance carry with spread risk

---

### Relative Value Comparison Across Credit Sectors

**Framework**: Use total return scenarios to compare attractiveness across different bonds/loans.

**Example: 3 corporate bonds**

| Metric | Bond A (Investment Grade) | Bond B (HY, Investment Case) | Bond C (Distressed) |
|---|---|---|---|
| **Valuation** |
| Price | 103.5 | 98.0 | 42.0 |
| Coupon | 3.5% | 6.5% | 11.0% |
| YTM | 2.8% | 6.8% | 15.2% |
| OAS | 80 bps | 250 bps | 1,200 bps |
| **Duration & Risk** |
| Effective Duration | 5.1 yr | 3.8 yr | 2.1 yr |
| Spread Duration | 4.9 yr | 3.5 yr | 1.5 yr |
| Effective Convexity | 90 | 40 | −200 |
| **Carry & Breakeven** |
| 6-month carry | 0.9% | 2.1% | 4.5% |
| Spread duration | 4.9 yr | 3.5 yr | 1.5 yr |
| Breakeven spread widening | 18 bps | 60 bps | 300 bps |
| **Base Case Return (6mo)** |
| Scenario: rates flat, spreads unchanged | 0.9% | 2.1% | 4.5% |
| Scenario: rates +50 bps, spreads +25 bps | −1.8% | 0.0% | +2.8% |
| Scenario: rates −50 bps, spreads −25 bps | +3.8% | +4.5% | +6.2% |

**Analysis**:

**Bond A (Investment Grade)**
- Low carry (0.9%), tight spreads (80 bps) → vulnerable to spread widening
- Very short breakeven (18 bps) → only 18 bps cushion before negative return
- High duration (5.1 yr) and positive convexity → benefits significantly from rate decline
- Best case: rates fall 50 bps; gain +3.8%
- Worst case: rates rise 100 bps, spreads widen 100 bps; lose −10%+
- **Position**: Defensive; suitable for rate-bullish outlook, not for spread-widening scenarios

**Bond B (High-Yield)**
- Attractive carry (2.1%); moderate breakeven (60 bps)
- Mid-range duration (3.8 yr) → reasonable rate risk
- Moderately positive convexity → partial protection from rate move extremes
- Returns fairly stable across scenarios (−1.8% to +4.5% across rate/spread moves)
- **Position**: Good core holding; balanced risk/reward for neutral outlook

**Bond C (Distressed)**
- Very high carry (4.5%); massive breakeven (300 bps) → huge cushion
- Short duration (2.1 yr) → limited rate sensitivity
- Negative convexity → some price risk if rates fall sharply (but offset by high carry)
- Returns robust across most scenarios; even if rates rise and spreads widen, positive return (2.8%)
- **Position**: Tactical position for risk-off/volatility trade; good downside protection; best in distressed phases of credit cycle

**Relative value selection**:
- **If expecting rate stability, spread stability**: Bond B (high carry, reasonable spread cushion)
- **If expecting rates to fall significantly**: Bond A (highest convexity, biggest gain)
- **If expecting stress/widening spreads**: Bond C (massive carry shield, short duration)
