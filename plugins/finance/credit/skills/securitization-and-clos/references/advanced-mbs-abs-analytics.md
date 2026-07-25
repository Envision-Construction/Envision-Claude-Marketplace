---
last_updated: "2026-03-21"
---

## Advanced MBS/ABS Analytics

### Prepayment Modeling

#### Prepayment Decomposition
Total prepayment = Housing Turnover + Refinancing + Curtailment + Defaults (involuntary)

**Housing Turnover**
- Baseline prepayment from home sales. Driven by demographics, job mobility, life events
- Relatively stable 6–8% CPR across economic cycles
- Seasoning ramp: new loans have low turnover (borrower just moved in), ramps over 30 months, then stabilizes
- Lower balance mortgages trend toward higher turnover CPR (transaction costs lower, easier for borrowers to exit)

**Refinancing Component**
- Rate-driven; borrower's economic incentive = note rate − current market rate
- When incentive is low (<50 bps), refinancing near zero; at moderate incentive (50–150 bps), refi speed ramps; at high incentive (>150 bps), speed plateaus (media effect, servicer/processor bottlenecks, burnout from prior waves)
- S-curve model captures sigmoid response to incentive:

```
Refi_CPR = Max_Refi × [1 / (1 + exp(−β × (Incentive − Threshold)))]

Where:
  Incentive = Note Rate − Current Market Rate (in bps)
  Max_Refi = refi speed at high incentive (typically 40–60% CPR)
  β = steepness parameter (0.01–0.03 typical)
  Threshold = incentive level where refi speed is 50% of max (~100 bps typical)
```

- When interest rates have recently declined sharply, borrowers respond more aggressively → higher β; after several waves of refi, response dampens (burnout) → lower β

**Burnout Effect**
- As pool seasons and fast prepayers exit, remaining borrowers are increasingly "sticky" (may be unable or unwilling to refinance due to credit/documentation issues, rate lock, institutional knowledge gaps, or emotional attachment)
- Burnout factor reduces refinancing speed over time for same incentive
- Pool factor (remaining balance / original balance) serves as practical burnout proxy: lower pool factor → more burnout → slower refi speed
- Simple adjustment: Refi_CPR_burnout = Refi_CPR_base × (Pool Factor)^0.3 (exponent 0.3 calibrated empirically)

**Curtailment**
- Partial principal prepayments (extra payments on mortgage) beyond scheduled amortization
- Small contribution to total prepayment (typically 1–2% CPR)
- Increases with loan age and borrower seasoning (borrowers with equity and confidence make extra payments)

**Default / Involuntary Prepayment**
- Loan defaults produce unscheduled principal through foreclosure/sale proceeds (net of costs and recovery lag)
- Material in subprime and non-prime pools; minimal in prime agency RMBS
- Default rate impacts prepayment timing and WAL (defaults front-load some principal recovery)

#### Prepayment Speed Conventions

**CPR (Conditional Prepayment Rate)**: Annualized percentage of remaining pool principal that prepays unscheduled in a given month
- Example: $100M pool, $2M unscheduled prepayment in month → 2% monthly × 12 = 24% CPR

**SMM (Single Monthly Mortality)**: Monthly equivalent of CPR
```
SMM = 1 − (1 − CPR)^(1/12)
Example: 24% CPR → SMM = 1 − 0.76^(1/12) ≈ 1.96% monthly
```

**PSA Model (Public Securities Association)**: RMBS prepayment benchmark
- Ramps from 0% CPR at month 1 to 6% CPR at month 30, then flat thereafter
- 100% PSA = standard model; 200% PSA = twice as fast; 50% PSA = half as fast
- Widely quoted in RMBS markets as common language for prepayment scenarios

**ABS Speed Conventions**: Auto/equipment ABS quote as absolute prepayment speeds (CPR %), credit card ABS quotes as Monthly Payment Rate (MPR %)

#### Prepayment Scenario Analysis

Run cash flows at multiple prepayment scenarios to assess sensitivity:

| Scenario | Speed | Use Case |
|----------|-------|----------|
| No Prepayment | 0% CPR | Conservative; shows maximum WAL & interest rate risk |
| Slow | 50% PSA or 0.5× median CPR | Low-rate environment, burned-out pool |
| Base | PSA model or median historical | Base case assumption |
| Fast | 2× base CPR | Refi wave, strong turnover environment |
| Extreme Fast | 400%+ PSA | Rare; severe refi incentive, seasoned pool |

For each scenario, calculate:
- **WAL**: Weighted average life; shorter WAL when prepay faster
- **Yield**: Total return; prepay causes negative convexity (yield falls when prepay speeds up in declining rate environment)
- **Price sensitivity**: WAL extension/contraction and reinvestment risk

**Negative Convexity Impact**:
- When rates fall, prepay accelerates → WAL shortens, investor must reinvest at lower yields (opportunity loss)
- When rates rise, prepay slows → WAL extends, investor locked in below-market coupon (extension risk)
- Trade-off asymmetry hurts MBS investors

---

### OAS & Monte Carlo Valuation

#### Option-Adjusted Spread (OAS) Concept
OAS is the constant spread over the Treasury forward rate curve that equates the model price to the market price, after accounting for the embedded prepayment option. OAS strips out the value of the borrower's prepayment option to give a "clean" spread measure comparable across securities.

#### Monte Carlo Simulation for MBS

1. **Interest rate path generation**: Generate N interest rate paths (typically 1000–5000) using a term structure model calibrated to the Treasury curve and interest rate volatility (implied swaption volatility typical)
   - Lognormal short-rate model, Black-Karasinski, or Hull-White model common
   - Ensure paths span realistic range: mean-reversion, volatility smile, realistic path correlation

2. **Path-dependent prepayment modeling**: For each rate path, compute monthly prepayment speeds as a function of:
   - Current loan coupon vs. current market rate (refinancing incentive)
   - Loan age (seasoning ramp) and remaining balance (pool factor for burnout)
   - Prepayment model parameters (S-curve coefficients, refinancing max, seasonal factor)
   - Result: Each path has unique prepayment speed sequence

3. **Cash flow projection**: For each path and each month:
   - Project scheduled principal amortization
   - Apply path-dependent prepayment speed to unscheduled principal
   - Calculate total principal (scheduled + unscheduled)
   - Calculate interest (coupon × current balance)
   - Account for loan losses if non-agency or subprime (reduce principal)

4. **Path discounting**: Discount each path's monthly cash flows back to present using:
   - Treasury zero-coupon rates from the rate path (not market rates)
   - Plus OAS (the spread being solved for)
   - Result: PV of cash flows for each path

5. **Model price calculation**:
```
Model Price = [1/N] × Σ(PV of each path's cash flows)
OAS is solved iteratively: find the spread that makes Model Price = Market Price
```

#### Example Valuation Logic

```
Assume:
  Current market price: 98.50
  Treasury forward curve: 4.0% (2yr) to 4.5% (30yr)
  Interest rate volatility: 12% (lognormal)
  MBS coupon: 4.5%, WAM: 350 months

Monte Carlo procedure:
  (1) Generate 2000 rate paths
  (2) On each path, model prepayment response to rate changes
  (3) Project cash flows (scheduled + unscheduled principal, interest)
  (4) Discount at Treasury rates + trial OAS (e.g., start with 100 bps)
  (5) Average across paths → computed price
  (6) If computed price > market price, OAS too low; increase OAS
  (7) Iterate until computed price ≈ 98.50 → OAS found (e.g., 85 bps)
```

#### Option Cost Calculation

Option Cost = Z-spread − OAS

- **Z-spread**: Spread that discounts cash flows at expected prepayment speed (no option adjustment)
- **OAS**: Spread after option adjustment
- **Option cost** represents the value of the embedded prepayment option to the borrower (cost to investor)

Example:
- Z-spread: 100 bps
- OAS: 85 bps
- Option cost: 15 bps (investor is paying 15 bps annually to offset borrower's prepayment option value)

Current coupon MBS have high option cost (40–80 bps); deep discount MBS have low option cost (0–10 bps).

---

#### Effective Duration (MBS)

Modified duration assumes fixed cash flows and does not work for MBS because prepayment changes with rates. Effective duration recalculates cash flows at shifted rate levels to capture the option effect.

**Effective Duration Formula**:
```
Effective Duration = (P_down − P_up) / (2 × P₀ × Δy)

Where:
  P_down = model price after parallel rate shift down by Δy (e.g., −50 bps)
  P_up = model price after parallel rate shift up by Δy (e.g., +50 bps)
  P₀ = current market price
  Δy = rate shift magnitude (50 bps typical)
```

**Calculation procedure**:
1. Compute OAS at current rates (market price → OAS)
2. Shift Treasury curve down by 50 bps
3. Re-run Monte Carlo with new rate paths using same OAS → compute P_down
4. Shift Treasury curve up by 50 bps
5. Re-run Monte Carlo with new rate paths using same OAS → compute P_up
6. Apply formula to get effective duration in years

**Example**:
```
Current price (P₀): 101.25 (premium MBS)
P_down (rates −50 bps): 102.50 (limited gain from prepayment acceleration)
P_up (rates +50 bps): 99.75 (larger loss from prepayment deceleration/extension)
Δy: 50 bps = 0.005

Effective Duration = (102.50 − 99.75) / (2 × 101.25 × 0.005)
                  = 2.75 / 1.0125
                  = 2.72 years
```

Premium MBS effective duration is typically shorter than modified duration (call option effect).
Discount MBS effective duration is typically longer than modified duration (extension risk).

---

#### Effective Convexity (MBS)

Effective convexity captures the curvature of the price-yield relationship, accounting for prepayment option.

**Effective Convexity Formula**:
```
Effective Convexity = (P_down + P_up − 2 × P₀) / (P₀ × Δy²)

Where variables same as effective duration formula.
```

**Interpretation**:
- **Positive convexity**: Price gains from rates down outweigh price losses from rates up (beneficial for investor)
- **Negative convexity**: Price gains from rates down are capped by prepayment (investor short an option)

**Example (continuing above)**:
```
Effective Convexity = (102.50 + 99.75 − 2 × 101.25) / (101.25 × 0.005²)
                    = (102.50 + 99.75 − 202.50) / (101.25 × 0.000025)
                    = −0.25 / 0.00253
                    = −99

Negative convexity of −99 confirms premium MBS is short the prepayment option.
```

**Premium vs. Discount MBS**:
- Premium (above par) MBS: negative effective convexity (prepayment call risk)
- At-the-money (par) MBS: near-zero convexity
- Discount (below par) MBS: more positive convexity (less likely to prepay, extension risk manifests differently)

---

#### Key Rate Duration (KRD)

Effective duration captures parallel rate shift sensitivity. Key rate duration measures non-parallel shifts, isolating exposure at each maturity point on the curve.

**KRD Calculation**:
1. Identify key maturity points: 2yr, 5yr, 10yr, 30yr (typical grid)
2. Shift only one key rate by 1 bp; hold others fixed (use interpolation for intermediate points)
3. Recompute MBS price (re-run prepayment model at new rate curve)
4. KRD at that key point = price change per 1 bp shift

**KRD Profile Example** (4.5% coupon MBS, current price 101):
| Key Rate | KRD Value | Interpretation |
|-----------|-----------|-----------------|
| 2yr | 0.15 | Short duration at front end (prepayment option effect) |
| 5yr | 0.85 | Medium exposure; transition point |
| 10yr | 1.20 | Highest exposure (cash flows concentrated here) |
| 30yr | 0.50 | Reduced (fewer cash flows at 25+ year horizon) |
| **Total Eff. Duration** | **2.70** | Sum of key rate durations |

**Use cases**:
- **Steepener trade**: If curve expected to steepen (front end rally, back end sell), KRD profile guides hedge (buy short-duration, sell long-duration MBS)
- **Curve flattener trade**: If curve expected to flatten, opposite positioning
- **Bullet structures**: Identify which part of the curve an MBS has most exposure

---

### CMO Analytics (Agency)

#### CMO Structures Overview

Collateralized Mortgage Obligations redistribute MBS pass-through cash flows into tranches with different average lives, coupons, and risk profiles.

#### Sequential-Pay CMO

**Structure**: Tranches receive principal sequentially (A, B, C, Z); all interest payments distributed pro-rata.

| Tranche | Priority | Priority for Interest | Characteristics |
|---------|----------|----------------------|-----------------|
| A | 1st principal | Pro-rata | Shortest WAL (3–5 yr typical) |
| B | 2nd principal | Pro-rata | Medium WAL (5–10 yr typical) |
| C | 3rd principal | Pro-rata | Long WAL (10–20 yr typical) |
| Z (Accrual) | Last principal | Receives as PIK initially | Longest WAL, most extension risk |

**Cash flow waterfall** (after servicer fees and swap costs):
1. All interest distributed pro-rata to A, B, C, Z (regardless of principal waterfall)
2. All principal to A until A retired
3. Then all principal to B until B retired
4. Then all principal to C until C retired
5. Z receives accrued interest (PIK) until senior tranches retired, then principal + accrued

**Advantages**:
- Creates defined short, medium, long average lives from single pool
- Predictable WAL for each tranche

**Disadvantages**:
- As prepayment speeds vary, WAL shortens/extends (negative convexity still present, but now borne separately)
- Z-bond's accrual feature creates duration extension risk (interest compounds; large principal return at maturity)

#### PAC Bond (Planned Amortization Class)

**Structure**: Principal repaid on fixed schedule if prepayments stay within a "PAC band" (e.g., 100–300% PSA). Companion (support) tranche absorbs excess or shortfall prepayments. Interest distributed pro-rata.

**PAC Band Mechanics**:
```
Example: Original pool $500M, 100–300% PSA band

100% PSA scenario:
  Month 1 principal: $1.2M
  Month 12 principal: $2.5M
  Month 60 principal: $3.8M

300% PSA scenario:
  Month 1 principal: $2.1M
  Month 12 principal: $5.0M
  Month 60 principal: $6.5M

PAC schedule (fixed):
  Takes the MINIMUM principal from band at each month
  Month 1: min($1.2M, $2.1M) = $1.2M guaranteed
  Month 12: min($2.5M, $5.0M) = $2.5M guaranteed
  Month 60: min($3.8M, $6.5M) = $3.8M guaranteed

Companion takes residual:
  100% PSA: Companion gets $0 (all excess goes to senior PAC tranches first)
  300% PSA: Companion gets excess prepayments
```

**Benefits of PAC**:
- Very stable WAL within band (100–300% PSA typical; WAL varies <0.5 yr)
- Low extension risk
- Lower option cost (prepayment option value capped by band)

**Drawbacks**:
- Band narrows as pool seasons (companion absorbs cumulative volatility, becomes increasingly subordinated)
- PAC I (wider band, ~100–600% PSA) vs. PAC II (narrower band, ~200–400% PSA) — PAC II more stable but band tighter
- If prepayments outside band, PAC schedule violated (extension if slow, contraction if very fast)

#### TAC Bond (Targeted Amortization Class)

**Structure**: Like PAC but protected against one direction of prepayment volatility only.

**TAC Band Example**:
- 100–300% PSA band (same as PAC above), but companion protects only against fast prepayments
- If prepayments exceed 300% PSA, companion absorbs excess → TAC schedule maintained
- If prepayments fall below 100% PSA, TAC schedule extended (companion cannot absorb shortfall)

**Use**: Cheaper than PAC (narrower protection); often used for intermediate tranches in structure.

#### Companion / Support Tranche

**Role**: Absorbs prepayment volatility that PAC/TAC is shielded from.

**Characteristics**:
- Highest extension and contraction risk
- Highest yield (compensates for volatility)
- WAL is volatile (can swing 2–5+ years based on prepayment environment)
- Most convex (both extension and contraction can occur)

**Subordination in bond stack**:
- PAC and TAC receive full schedule (within bands)
- Companion receives only residual principal
- If prepayments slow, companion principal dries up (extension)
- If prepayments accelerate, companion principal received early (contraction)

#### Interest-Only (IO) Strip

**Cash flow**: Receives all interest accrued; receives no principal.

**Valuation mechanics**:
- When prepayments accelerate, outstanding principal balance declines faster → less interest earned → IO value falls
- When prepayments slow, principal remains longer → more interest earned → IO value rises
- **Negative duration**: IO gains value when rates rise (prepayment slows, duration extends); IO loses value when rates fall (prepayment accelerates)

**Use cases**:
- Hedge for premium MBS (IO short prepayment option; MBS long prepayment option → offset)
- Yield enhancement in certain rate scenarios

#### Principal-Only (PO) Strip

**Cash flow**: Receives all principal (scheduled + unscheduled); receives no interest.

**Valuation mechanics**:
- When prepayments accelerate, principal returned faster → PO value rises (cash returned sooner at higher discount rate)
- When prepayments slow, principal returned slowly → PO value falls (cash returned later)
- **Positive convexity**: PO gains value when rates fall (prepayment accelerates, principal returned faster); PO loses value when rates rise

**Leverage effect**: PO is high-leverage instrument (small rate move → large PO price move due to prepayment sensitivity).

#### CMO Analytics Framework

For each tranche, compute and monitor:

**Scenario analysis (prepayment)**:
- WAL at 50%, 100%, 200%, 400% PSA
- Price at each scenario (using OAS model)
- Yield at each scenario

**Effective duration and convexity**:
- Calculate using rate shifts (±50 bps) at each prepayment scenario
- Understand asymmetry in extension vs. contraction risk

**Yield profile**:
- Compare yield to duration to comparable securities
- Higher yield compensates for higher extension/contraction risk

**Companion absorption capacity**:
- For PAC / TAC analysis: How much cushion does companion provide?
- If companion buffer depleted by losses or extreme prepayment, PAC schedule at risk

**Rate scenario matrix**:
| Rate Move | 100% PSA Price | 200% PSA Price | 300% PSA Price | Comment |
|-----------|---|---|---|---|
| −100 bps | 105.2 | 104.5 | 104.0 | Fast refi; PAC/TAC benefit |
| 0 bps | 101.5 | 101.8 | 101.5 | Base case |
| +100 bps | 96.8 | 97.5 | 98.2 | Extension; companion hurt |

---

### Total Return Analysis

#### Total Return Framework for MBS/ABS

**Total return** over investment horizon (typically 6–12 months) includes:
- Coupon income (monthly interest)
- Principal return (scheduled + unscheduled)
- Price change (from rate move, spread move, volatility change)
- Reinvestment income (coupons reinvested at horizon rates)
- Financing cost (if leveraged)

**Formula**:
```
Total Return (%) = [Coupon Income + Principal Return + Price Change + Reinvestment − Financing Cost] / Initial Investment

Alternative breakdown by source:
  Total Return = Carry + Price Return from Rate/Spread Move

  Where:
    Carry = Monthly coupons + pull-to-par (if discount) + roll-down + reinvestment
    Price Return = −Effective Duration × Δy + 0.5 × Effective Convexity × Δy²
                  −Spread Duration × ΔSpread
```

#### 6-Month Horizon Modeling

Assume 6-month holding period; project total return under different scenarios.

**Steps**:
1. **Base case**: Assume rates unchanged, spreads unchanged
   - Compute monthly carry (coupon + pull-to-par for discounts)
   - Compute prepayment speed (base case PSA or historical median)
   - Project ending WAL after 6 months
   - Ending price from yield at horizon (base case yield curve)
   - Total return = (6 months carry + price change) / initial price

2. **Rate scenarios**: ±50 bps, ±100 bps parallel shift
   - Re-run prepayment model at new rates
   - Recompute ending WAL and price
   - Calculate total return at each rate scenario

3. **Spread scenarios**: ±25 bps, ±50 bps spread widening/tightening
   - Assume rates unchanged but OAS widens/tightens
   - Recompute price using new OAS
   - Calculate total return

4. **Combined scenario matrix**:
   - Rows: Rate moves (−100, −50, 0, +50, +100 bps)
   - Columns: Spread moves (−50, −25, 0, +25, +50 bps)
   - Cells: Total return (%) at each intersection

**Example Matrix** (4.5% coupon MBS, price 101, OAS 85 bps, horizon 6 months):

| Rate / Spread | −50 Sp | −25 Sp | Flat | +25 Sp | +50 Sp |
|---|---|---|---|---|---|
| −100 bps | +6.5% | +5.2% | +4.0% | +2.8% | +1.5% |
| −50 bps | +4.8% | +3.8% | +2.8% | +1.8% | +0.8% |
| Flat | +2.2% | +1.5% | +0.8% | +0.1% | −0.5% |
| +50 bps | −1.0% | −1.5% | −2.0% | −2.5% | −3.0% |
| +100 bps | −4.2% | −4.5% | −4.8% | −5.1% | −5.4% |

**Interpretation**:
- Bullish on rates and spreads → expect upper-left quadrant returns (6%+)
- Neutral base case → expect center cell return (~0.8%)
- Bearish → expect lower-right quadrant returns (−5%+)

#### Scenario Matrix Construction

**Inputs to project**:
1. **Prepayment speed at new rates**: Use S-curve refinancing model or PSA adjustments
   - Lower rates → higher CPR (refinancing wave) → shorter WAL, higher reinvestment risk
   - Higher rates → lower CPR (burnout, less refi incentive) → longer WAL, extension risk

2. **Ending WAL**: Sum of principal-weighted return timing under new prepayment speeds

3. **Ending price**: Use OAS model or simplified yield calculation
   - For each scenario, compute yield and duration to new WAL
   - Price = PV of remaining cash flows at new yield (coupon + OAS)

4. **Reinvestment income**: Assume coupons received over 6 months are reinvested at horizon yield
   - Conservative: assume reinvestment at current coupon (0% carry)
   - Base case: reinvestment at mid-point between current and horizon yield
   - Optimistic: reinvestment at horizon yield

#### Breakeven Analysis

**Question**: How much can spreads widen before total return becomes negative?

**Breakeven spread widening** (6-month horizon):

```
Breakeven = Carry / Spread Duration

Where:
  Carry = 6-month forward carry (coupon + pull-to-par + roll-down + reinvestment), %
  Spread Duration = |ΔPrice / ΔSpread|, years
```

**Example**:
- 6-month carry: 1.5% (0.25% monthly × 6)
- Spread duration: 4.2 years
- Breakeven: 1.5% / 4.2 = 0.357 = ~36 bps annual spread widening = ~18 bps over 6 months
- Interpretation: If spreads widen more than 18 bps, total return falls below zero (assuming rates flat)

**Practical use**:
- High carry, short spread duration → wide breakeven → cushion against spread widening → attractive risk-reward
- Low carry, long spread duration → narrow breakeven → vulnerable to widening → requires strong conviction to own

#### Relative Value Comparison (ABS)

**Framework**: Compare total return profiles across multiple ABS tranches.

**Inputs for each tranche**:
- Current price, coupon, OAS, WAL
- Effective duration, effective convexity
- Base case prepayment speed (for RMBS/ABS)
- Credit rating, loss severity assumptions (for non-agency)
- Carry (6-month forward return if rates/spreads unchanged)
- Breakeven spread widening

**Ranking example** (comparing 3 tranches):

| Metric | Tranche A (Senior) | Tranche B (Mezzanine) | Tranche C (Junior) |
|---|---|---|---|
| Coupon | 4.5% | 6.0% | 8.5% |
| Price | 101.0 | 98.5 | 94.0 |
| OAS | 80 bps | 200 bps | 400 bps |
| Eff. Duration | 2.8 yr | 3.5 yr | 4.2 yr |
| Carry (6mo) | 1.4% | 1.8% | 2.1% |
| Spread Duration | 2.8 | 3.4 | 4.0 |
| Breakeven Spread Widening | 50 bps | 53 bps | 53 bps |

**Interpretation**:
- Tranche A: Tight OAS, high price (premium), shortest duration. Safe, limited upside.
- Tranche B: Mid-tier risk/reward. Carry better than A; spread cushion similar to C despite lower yield.
- Tranche C: High yield (8.5%), but longest duration and longest expected WAL. Vulnerable to extension if rates rise.

**Selection decision**:
- **Risk-on environment**: Overweight Tranche C (highest carry, acceptable extension risk)
- **Risk-off environment**: Overweight Tranche A (capital preservation, lower duration)
- **Neutral**: Ladder or barbell between A and C, use B as intermediate hedge
