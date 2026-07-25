---
last_updated: "2026-03-21"
---

## Macro & Interest Rate Sensitivity Framework

### How Rate Changes Flow Through Credit Quality

Interest-rate moves affect credit quality through multiple channels. The direct effect on interest expense is only the first-order impact; refinancing conditions, valuation, and macro demand can be equally important. A strong sensitivity analysis should test both the contractual rate reset and the broader earnings response.

**Transmission Channels:**
```
Rate Increase
  ├── Direct: Higher interest expense → lower coverage → reduced FCF
  ├── Refinancing: Maturing debt reprices at higher cost
  ├── Macro: Economic slowdown → revenue/EBITDA pressure
  ├── Asset values: Higher discount rates → lower enterprise values → thinner equity cushion
  └── Consumer: Reduced spending power → demand destruction in rate-sensitive sectors
```

### Direct Impact: Floating-Rate Debt

Floating rate instruments (leveraged loans, revolvers, floating rate notes) reprice immediately with benchmark rate changes. This is the most quantifiable and immediate channel.

**Interest Expense Sensitivity Formula:**
```
Incremental annual interest expense = Floating rate debt outstanding x Rate change (bps) / 10,000
```

**Benchmark floor consideration**: Many floating-rate loans include benchmark floors. When the benchmark is above the floor, each basis point change flows through. When the benchmark is below the floor, the borrower effectively pays the floor and is insulated from additional cuts.

### Rate Sensitivity Table

Build a sensitivity table for every credit with meaningful floating-rate exposure. Pull live benchmark levels from `references/market-benchmarks.md`; do not hard-code them here.

```
Benchmark Shock Table:
──────────────────────────────────────────────────────────────
Scenario            Benchmark Move    All-in Cost    Coverage
──────────────────────────────────────────────────────────────
Downside relief      -100 bps         Base - 100     Recalculate
Base case            Current level    Base           Recalculate
Moderate stress      +100 bps         Base + 100     Recalculate
Severe stress        +200 bps         Base + 200     Recalculate
Break-point case     +X bps           Base + X       Covenant / FCF break
──────────────────────────────────────────────────────────────
```

**Critical output**: identify the benchmark move at which covenant thresholds are breached, interest coverage becomes unacceptable, or free cash flow turns negative.

### Fixed vs Floating Rate Exposure

**Natural Hedging:**
- Fixed-rate bonds provide certainty of interest cost regardless of rate moves
- Floating-rate loans expose the borrower to rate volatility
- Optimal mix depends on company cash flow profile and rate outlook
- Highly cyclical businesses often benefit from more fixed-rate debt because higher rates can coincide with weaker earnings

**Synthetic Hedging Instruments:**
| Instrument | Mechanism | Typical Use | Cost Consideration |
|-----------|-----------|-------------|-------------------|
| Interest rate swap | Convert floating to fixed (or vice versa) | Lock in rate exposure on floating debt | Swap premium over the benchmark curve; mark-to-market risk |
| Interest rate cap | Limits maximum rate on floating debt | Protect against extreme rate moves | Upfront premium; no benefit if rates stay below cap |
| Interest rate collar | Cap + floor; sell floor to fund cap purchase | Reduce cap premium | Gives up benefit of rate declines below floor |
| Swaption | Option to enter a swap at future date | Hedge anticipated debt issuance | Premium cost; useful for forward refinancing |

**Evaluating Hedge Effectiveness:**
- What percentage of floating-rate debt is hedged?
- What is the remaining tenor of existing hedges?
- Are hedges rolling off near-term, exposing the company to reset risk?
- Is the company hedging enough of the notional and tenor to be meaningful?

### Fixed-Charge Coverage Sensitivity

Fixed Charge Coverage Ratio (FCCR) captures the full debt service burden including mandatory amortization, lease payments, and capex:

```
FCCR = (EBITDA - Capex) / (Interest + Mandatory Amort + Lease Payments)
```

For tight credits, run FCCR under the same benchmark shocks used in the cash-interest table and identify the break-point case.

### Refinancing Cost Impact

When fixed-rate debt matures into a different rate environment, the borrower faces repricing risk even if business performance is unchanged.

```
Refinancing Cost Template:
  Maturity amount:                    $X
  Existing all-in coupon/spread:      Old cost
  Estimated refinancing cost:         New cost
  Annual interest cost increase:      $X
  Coverage impact:                    Recalculate
  FCF impact:                         Recalculate
```

### Second-Order Effects: The Macro Channel

Rate moves do not occur in a vacuum. Tighter financial conditions can weaken demand, slow capex, tighten customer credit, and pressure enterprise values. Easier conditions can do the reverse.

**The Double Hit Problem:**
```
Combined Stress Chain:
  Step 1: Benchmark shock raises cash interest
  Step 2: Earnings soften because demand or pricing weakens
  Step 3: Recalculate leverage, coverage, liquidity, and covenant headroom

Analyzing only Step 1 often understates the real downside.
```

**Common earnings channels from tighter rates:**
- Consumer demand contraction (discretionary spending, housing, autos)
- Business investment pullback (capex deferral, inventory destocking)
- Tighter bank lending standards (reduced credit availability for customers)
- Asset price deflation (real estate, financial assets) reducing wealth effect

### Rate-Sensitive Sectors

Certain sectors have amplified exposure to rate changes:

| Sector | Rate Sensitivity | Primary Channel |
|--------|-----------------|-----------------|
| Homebuilding / housing-linked | Very High | Affordability, mortgage cost, land values |
| Autos and consumer durables | High | Financing availability and monthly payment sensitivity |
| Commercial real estate | Very High | Cap-rate expansion, refinancing risk, and NOI pressure |
| Consumer finance | High | Funding cost, net interest margin, and credit losses |
| Highly levered LBO credits | High | Direct cash-interest pressure and refinancing risk |
| Retail / discretionary | Moderate-High | Demand pullback and mix pressure |
| Utilities / infrastructure | Moderate | Capital intensity and refinancing dependence |

### Rates and Relative Value

The rate environment affects relative value across credit instruments:

**Loan vs Bond Relative Value:**
- Rising-rate environments can favor floating-rate loans because coupons reset higher
- Falling-rate environments can favor fixed-rate bonds because locked coupons become more valuable
- Relative value depends on spread, duration, call structure, and expected path of rates

**Decision framework:**
```
Prefer More Fixed Exposure When:  Prefer More Floating Exposure When:
────────────────────────────────  ──────────────────────────────────
Cash flows are cyclical           Cash flows are stable
Refinancing risk is elevated      Asset duration is short
Coverage cushion is thin          Balance sheet is lightly levered
Rate downside is more likely      Rate upside protection matters
```

### FX Risk for Cross-Border Credits

For issuers with multi-currency debt or revenue:

**Currency Mismatch Risk:**
- Revenue in local currency, debt in USD/EUR creates mismatch
- Local currency depreciation increases debt burden in local terms
- Hedging costs can be substantial for EM currencies (5-10%+ per annum)

**Natural Hedges:**
- Revenue in same currency as debt obligation
- Local currency costs offsetting local currency revenue (operating hedge)
- Diversified revenue base across multiple currency zones

**FX Stress Test:**
- Model 10-20% depreciation of local currency vs debt currency
- Assess impact on leverage ratios (debt in reporting currency rises)
- Evaluate whether covenants are tested on constant-currency or reported basis

### Practical Sensitivity Matrix

For every credit with material floating-rate exposure, produce:

```
Combined Rate & EBITDA Sensitivity Matrix:
─────────────────────────────────────────────────────────────────
                   EBITDA Scenarios
Benchmark Move   -15%      -10%      Base      +5%       +10%
─────────────────────────────────────────────────────────────────
Down 100 bps     fill       fill      fill      fill      fill
Base             fill       fill      fill      fill      fill
Up 100 bps       fill       fill      fill      fill      fill
Up 200 bps       fill       fill      fill      fill      fill
Break point      fill       fill      fill      fill      fill
─────────────────────────────────────────────────────────────────
Values = Interest Coverage Ratio (EBITDA / Cash Interest)
Shaded cells = below 2.0x coverage threshold
```

### Core Takeaways

- Rate level alone does not determine stress; pace of change and starting leverage matter as much.
- Floating-rate exposure should be reviewed alongside hedge protection and refinancing runway.
- The most dangerous case is usually higher rates plus weaker earnings, not either factor in isolation.
- Use root benchmarks for live calibration and keep this file focused on methodology rather than current market levels.
