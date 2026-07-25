---
last_updated: "2026-03-22"
---

## Relative Value Analysis for Credit

### Spread Measures Hierarchy

Different spread metrics serve different purposes in credit analysis. Choosing the right metric is essential for accurate comparison.

**Nominal Spread (G-Spread):**
- **Definition**: Difference between bond yield and interpolated Treasury yield at same maturity
- **Formula**: YTM(Bond) − YTM(Treasury)
- **Use case**: Quick approximation; simplest to calculate; ignored optionality and curve structure
- **Limitation**: Ignores option value; misleading for callable bonds or securities with embedded options; doesn't account for term structure of credit risk

**Spread-to-Worst (STW):**
- **Definition**: The standard comparison metric in leveraged finance. Compares the bond's YTW to the Treasury yield corresponding to the YTW calculation date.
- **Formula**: STW = YTW − Treasury Yield(at YTW date)
- **Use case**: Standard for callable bonds in leveraged finance; accounts for call risk by using worst-case date and matching Treasury maturity to actual return horizon
- **Advantage**: Makes bonds with different maturities and call structures comparable; standard in leveraged finance term sheets
- **Example**: YTW = 8.55% (at 3-year call date), 3-year Treasury = 4.25% → STW = 430 bps. Compare to nominal spread of 440 bps (YTM 8.90% − 5-year Treasury 4.50%) — STW correctly captures that call risk compresses the effective spread.

**When STW ≠ Nominal Spread:**
```
Bond A: YTM 8.90%, YTW 8.55% (callable)
Bond B: YTM 8.50%, YTW 8.50% (non-callable)

Nominal Spread:
  A: 8.90% - 4.50% = 440 bps
  B: 8.50% - 4.50% = 400 bps
  → A looks ~40 bps cheaper

STW (using 3Y Treasuries at 4.25%):
  A: 8.55% - 4.25% = 430 bps
  B: 8.50% - 4.25% = 425 bps
  → Only ~5 bps difference once call risk included
  → Market is correctly pricing call risk
```

**Z-Spread (Zero-Volatility Spread):**
- **Definition**: Constant spread over the entire Treasury zero-coupon curve that equates the bond's price to present value of its cash flows
- **Formula**: Discount rate applied to all periods such that: Price = Σ[CF_t / (r_t + Z)^t] where r_t is Treasury zero at time t and Z is the Z-spread
- **Use case**: Standard for non-callable, bullet bonds; appropriate for spreads comparisons across the curve
- **Advantage**: Captures full term structure of interest rates; more accurate than nominal spread
- **Limitation**: Still ignores embedded options; assumes no volatility

**OAS (Option-Adjusted Spread):**
- **Definition**: Z-spread adjusted downward to remove the value of embedded call/put options
- **Formula**: OAS = Z-spread − Option-Adjusted Spread for embedded option
- **Use case**: Essential for callable bonds, putable bonds, floaters with caps/floors — any instrument with embedded optionality
- **How it works**: Model assumes rates will volatilize; estimate probability-weighted value of issuer's call option; subtract from Z-spread
- **Example**: Bond trades at 250 bps Z-spread; embedded call option worth 30 bps → OAS = 220 bps. If rates fall and bond gets called, holder captures 220 bps OAS but loses 30 bps to option exercise.

**Asset Swap Spread (ASW):**
- **Definition**: Spread over SOFR embedded in an asset swap package (fixed-rate bond + interest rate swap to convert to floating-rate equivalent)
- **Use case**: Compare fixed-rate bonds to floating-rate loans; identify cross-market relative value
- **Example**: Bond yields 5%, Treasury curve implies 3% SOFR + risk-free spread → Bond ASW = (5% − 3%) = 200 bps over SOFR. Loan pricing 200 bps SOFR + spread; both appear same on ASW basis.
- **Why use**: Some investors think in floating-rate terms (loan desk, CLO managers); ASW bridges fixed/floating comparison

**When to Use Which:**
```
Security Type                     Best Spread Metric
─────────────────────────────────────────────────────
Bullet bond (non-callable)       Z-spread
Callable bond (leveraged fin.)   STW (standard); OAS (rigorous)
Callable bond (IG / complex)     OAS
Floating-rate bond/loan          Discount Margin (DM) or ASW
PIK / deferred coupon            OAS (complex optionality)
Distressed / high spread         Z-spread (less market depth, OAS model uncertainty)
```

### Credit Curve Analysis

A credit curve is the term structure of spreads for a single issuer across its maturity spectrum.

**What the Credit Curve Tells You:**
- **Flat curve**: Market sees stable credit quality across time — no expected deterioration or improvement
- **Upward-sloping (steep)**: Longer-term concern; market pricing more risk for longer maturities. May reflect: (1) expected deterioration, (2) liquidity premium (long bonds less liquid), or (3) maturity premium
- **Inverted (downward-sloping)**: Unusual; front-end trading at distressed levels. Signals near-term stress (covenant test, maturity wall, refinancing risk) but confidence in long-term recovery

**Roll-Down Benefit:**
As a bond ages, it "rolls down the curve" — moves to shorter maturity as time passes. If the credit curve is upward-sloping, this generates return:

```
Example: Company XYZ has 7-year bonds at 400 bps, 6-year bonds at 385 bps (steep curve)
Purchase 7-year bond; hold for 1 year (no spread change)
After 1 year, bond is now 6-year bond; if spread stays 385 bps, bond has tightened 15 bps
Roll-down return ≈ 15 bps spread compression = 15 bps annual return

Formula: Roll-Down Return ≈ (Spread_current_maturity − Spread_shorter_maturity) × Duration
         = (400 − 385) × 6 = 90 bps return (simplified; doesn't account for duration decay)
```

**Trading Credit Curves:**
Identify mispricing within an issuer's curve and express as trades:
- **Butterfly trade**: If 5-year spread is wide relative to 3-year and 7-year, sell 3/7 and buy 5 (sell wings, buy belly)
- **Duration-neutral switches**: Sell one maturity, buy longer maturity, hedge duration difference with Treasury futures
- **Curve flattening trade**: If curve is very steep, sell long-end, buy short-end (bet on flattening)

### Relative Value Framework — Tight/Wide Analysis

Compare an issuer's current spread against multiple benchmarks to assess whether it offers value:

**Benchmark #1: Issuer's Own History**
- Calculate historical spread range for the issuer over 1-year, 2-year, 5-year periods
- Determine where current spread falls within that range (percentile)
- Example: "XYZ's 5-year bond spread is at 75th percentile of 2-year range; historically this was only reached during distress → likely overpriced"

**Benchmark #2: Rating Peer Comparison**
- Identify all BB-rated (or other rating) bonds in same or similar sector
- Calculate weighted average spread; determine median and percentile
- If issuer trades significantly tighter than rating peers (and no fundamental advantage), may be overpriced
- If issuer trades significantly wider, may offer value relative to peers

**Benchmark #3: Sector Average**
- Group by industry (autos, retail, pharma, etc.)
- Calculate sector average and dispersion
- Is issuer trading tight/wide relative to sector?

**Benchmark #4: Broad Market Index**
- Compare to CDX High-Yield Index level, HY bond index average
- If entire HY market has tightened, individual issuer spread compression may reflect market move, not fundamental improvement

**Percentile Ranking Interpretation:**
```
Percentile Range        Interpretation            Action
─────────────────────────────────────────────────────────
90-100th percentile     Very wide (cheap)         Buy if thesis intact
70-89th percentile      Above average spread      Consider buying
50-69th percentile      Near median (fair value)  Neutral
30-49th percentile      Below average spread      Consider selling
0-29th percentile       Very tight (expensive)    Avoid / trim
```

### Cross-Market Relative Value

Credit opportunities exist across different security types from the same issuer or borrower.

**Bond vs. Loan Comparison:**
- Compare YTM on issuer's bonds to Discount Margin (DM) on issuer's loans
- Adjust for seniority difference: senior secured loan should yield more than senior unsecured bond? If not, loan is relatively cheap
- Adjust for fixed vs. floating: floating-rate loan provides rate protection; fixed-rate bond doesn't
- Example: Issuer's senior bond yields 5%, loan prices at SOFR + 300 bps. If SOFR ≈ 5.5%, loan YTM ≈ 8.5%. Loan offers higher yield but takes floating-rate risk; bond is relatively cheaper if rates stable.

**Bond vs. CDS Basis:**
- CDS spread = market's pricing of default risk (protection cost)
- Bond spread = market's pricing of default risk + liquidity risk + credit curve term structure
- **CDS spread − Bond Z-spread = CDS-Bond Basis**
  - Negative basis (CDS < Bond): CDS cheaper than cash bond → synthetic short position cheaper
  - Positive basis (CDS > Bond): CDS more expensive than bond → synthetic long position more expensive

**Basis Trade Mechanics:**
- If basis is negative (CDS < bond): Buy bond, sell protection (long bond + short CDS). If basis compresses, profit.
- Structure typically as asset swap: bond + receive SOFR + pay fixed on interest rate swap = synthetic SOFR + CDS spread

**Secured vs. Unsecured Basis:**
- Secured debt (e.g., senior secured bond) trades tighter than unsecured debt from same issuer
- Spread differential = recovery value of collateral
- Example: Company's Sr Secured bonds at 250 bps, Sr Unsecured at 350 bps → 100 bps secured/unsecured basis
- If basis widens (secured tightens relative to unsecured), suggests market concerns about collateral value or is revaluing recovery assumptions

### New Issue Concession Analysis

When companies issue new bonds, they price them with a concession (wider spread) to attract investor demand.

**Concession Definition:**
- New issue spread minus the spread that would apply to that maturity on the issuer's secondary curve (if bonds were already trading)
- Typical new issue concessions:
  - Investment-grade: 10–25 bps
  - High-yield: 25–50 bps
  - Distressed / stressed: 50–150+ bps

**Concession Compression:**
- In strong markets with robust demand, concession compresses quickly (bonds tighten in secondary market post-pricing)
- "Breaks" well = quick tightening (e.g., new issue priced at 350 bps, trades at 340 bps day 1 = 10 bps compression)
- Strong technical demand = investors willing to buy at par and hold or flip for quick profit

**Primary Market "Follow" Strategy:**
- If you want exposure to an issuer and bonds are trading expensive in secondary, participate in new issue
- Size participation based on concession: large concession = more attractive entry
- Post-IPO: secondary holdings of same issuer that tighten to new issue level become candidates to trim/sell

**Refinancing Analysis Using New Issue Concessions:**
- When company refinances maturing debt, estimate cost of new issue (old maturity spread + normal concession)
- If refinancing spread is significantly higher than old debt coupon, refinancing cost rises (negative for credit)
- Model interest expense impact on coverage ratios

### Curve Value Trades

Identify specific maturities on an issuer's curve that appear mispriced relative to adjacent points.

**Butterfly Trade Mechanics:**
- Identify point on curve that is disproportionately expensive or cheap
- Example: 3-year at 300 bps, 5-year at 320 bps, 7-year at 310 bps → 5-year is "belly" (wider than interpolation of wings)
- Trade: Sell 3-year + sell 7-year (sell wings) / buy 5-year (buy belly)
- Profit if belly tightens relative to wings (basis compression)

**Duration-Neutral Curve Trades:**
- Want to express curve view without taking net duration bet
- Sell one maturity, buy longer maturity
- Hedge duration exposure: if trade adds duration, sell Treasury futures to neutralize
- Example: Sell 3-year at 280 bps, buy 7-year at 300 bps; sell Treasury futures to keep portfolio duration flat

**Capital Structure Trades:**
- Long senior tranche + short subordinated (or vice versa)
- Example: Long senior unsecured, short subordinated → bet on credit curve flattening (subordinated tightens relative to senior)
- Or: long secured, short unsecured → bet on secured tightening or unsecured widening (collateral value recovering or deteriorating)

---
