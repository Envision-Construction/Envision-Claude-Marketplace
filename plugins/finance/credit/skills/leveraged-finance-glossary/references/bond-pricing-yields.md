---
last_updated: "2026-03-22"
---

## Bond Pricing & Yields

### Price Quoting Convention

- **Par**: 100 = face value ($1,000 per $1,000 bond)
- **Premium**: > 100 (e.g., 105 = $1,050 for $1,000 bond)
- **Discount**: < 100 (e.g., 95 = $950 for $1,000 bond)

### Accrued Interest

- **Clean price**: Price excluding accrued interest.
- **Dirty price**: Full payment amount including accrued interest.
- **Accrued interest**: Coupon earned by the seller between the last payment date and settlement.
- **Day-count convention**: The rule used to prorate coupon accrual, such as 30/360 for many corporate bonds.

### Yield Measures

**Coupon Yield**
- Annual coupon / Par value
- Useful shorthand but ignores market price.

**Current Yield**
- Annual coupon / Current price
- Ignores pull-to-par and optionality.

**Yield to Maturity (YTM)**
- Internal rate of return of contractual cash flows to maturity.
- Assumes the bond is held to maturity and cash flows are received as scheduled.

**Yield to Worst (YTW)**
- Lowest yield across relevant contractual outcomes such as maturity, call, or put.
- Particularly important when bonds have meaningful call protection or redemption optionality.

**Yield to Call (YTC)**
- Yield assuming the bond is redeemed on a stated call date at a specified call price.
- Most relevant when the bond trades above par or above the call price.

### Spread Measures

**Nominal Spread (Spread Over Treasuries)**
- Difference between the bond yield and a benchmark risk-free yield of similar maturity.
- Simple shorthand, but it does not capture curve shape or embedded options well.

**Spread to Worst (STW)**
- Nominal spread using yield-to-worst rather than yield-to-maturity.

**Option-Adjusted Spread (OAS)**
- Spread measure that attempts to isolate credit compensation after adjusting for embedded options.
- Usually more useful than nominal spread when optionality is material.

**Z-Spread**
- Constant spread added to the entire benchmark curve that equates discounted cash flows to market price.
- Useful when comparing bonds with different cash-flow timing on a curve-consistent basis.

**Asset Swap Spread (ASW)**
- Spread implied when a fixed-rate bond is converted into floating-rate exposure through a swap framework.
- Useful for investors thinking in floating-rate funding terms.

**Discount Margin**
- Floating-rate analogue to spread for instruments such as loans and floaters.
- Reflects the margin earned above the reference-rate framework after adjusting for price.

**Spread Terminology**
- **Tightening**: Spread narrows (yield down, price up) → market confidence improving
- **Widening**: Spread widens (yield up, price down) → market stress increasing
- **Spread compression**: Material tightening across a market or peer set
- **Basis**: Relative difference between two linked pricing measures, such as cash bonds and CDS

### Duration

**Macaulay Duration**
- Weighted average time to receive cash flows
- Measured in years
- Formula: Σ(PV of cash flow × time) / Current price

**Modified Duration**
- Macaulay duration adjusted for yield
- Measures **price sensitivity** to yield changes
- Rule of thumb: price change is approximately duration multiplied by the yield move, subject to convexity.

**DV01**
- Dollar value change for a 1 bp move in the relevant rate curve.
- Useful for interest-rate hedging and portfolio aggregation.

**CS01**
- Dollar value change for a 1 bp move in credit spread.
- Useful for spread-risk aggregation and hedging.

### Total Return Calculation

**Components of Total Return:**
1. Coupon income (interest paid)
2. Carry or spread income
3. Roll-down or pull-to-par
4. Price appreciation or depreciation
5. Reinvestment effects

### Practical Interpretation

Use the simplest measure that matches the question:

- use **price** for mark level;
- use **current yield** for simple income framing;
- use **YTM / YTW** for bond economics;
- use **OAS or Z-spread** for relative value across fixed-rate bonds;
- use **discount margin** for floating-rate instruments; and
- use **duration, DV01, and CS01** for risk sensitivity.

If the user asks for current spread levels or market pricing, read `references/market-benchmarks.md` rather than relying on examples or stale convention.

---
