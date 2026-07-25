---
last_updated: "2026-03-22"
---

## Part 1: Credit Risk Metrics

### CS01 (Credit Spread 01)

**Definition**: Dollar P&L impact from 1 basis point parallel shift in credit spread.

**Formula**: CS01 = −Modified Spread Duration × Market Value × 0.0001

**How It Works**:
- Measures portfolio sensitivity to credit spread changes (independent of interest rates)
- Example: Portfolio with CS01 = $50,000 loses $50,000 if credit spreads widen 1 bp, and approximately $5.0M if spreads widen 100 bps
- Higher CS01 = higher credit risk exposure
- Used for: position-level risk sizing, portfolio aggregation, hedge ratio calculation

**Application in Buy-Side**:
- Portfolio managers target total CS01 within risk limits (example: $200K CS01 means the portfolio loses about $200K for a 1 bp widening and about $20.0M for a 100 bp widening)
- Position sizing tied to CS01: larger positions = higher CS01; limited by CS01 budget per manager
- Hedging via CDS: buy protection on names/index to offset CS01 exposure

### DV01 (Dollar Value of 01)

**Definition**: Dollar P&L impact from 1 basis point parallel shift in interest rates.

**Formula**: DV01 = −Modified Duration × Market Value × 0.0001

**How It Works**:
- Measures portfolio sensitivity to rate changes (independent of credit spreads)
- Example: Portfolio with DV01 = $100,000 loses $100,000 if rates rise 1 bp, and approximately $10.0M if rates rise 100 bps
- Separates rate risk from credit risk for more precise risk management

**Application in Buy-Side**:
- Portfolio managers often target duration-neutral positioning (DV01 = 0 or low) to isolate credit bets
- Can hedge DV01 via Treasury futures or interest rate swaps without affecting credit exposure
- Typical approach: long credit bonds (positive DV01) + short Treasury futures (negative DV01) = duration-neutral credit positioning

### Spread Duration

**Definition**: Sensitivity of bond price to parallel shift in credit spread (holding rate constant).

**Calculation**: For fixed-rate bonds, approximately equals Modified Duration (same as bond duration)

**For Floating-Rate Loans**:
- Spread duration ≈ time to next reset OR time to maturity, whichever is shorter
- SOFR loans reset quarterly: spread duration typically 0.25–0.75 years
- Implication: loans have minimal interest rate duration but meaningful spread duration
- Example: $10M loan with 3-month SOFR reset and 5-year maturity; DV01 ~$2,000 (low rate risk), but CS01 ~$30,000 (meaningful spread risk)

**Portfolio Implication**:
- Loans + bonds portfolio: total spread duration = blended metric; can be used for hedge sizing
- If portfolio spread duration = 4 years, 1 bps spread move = 4 bps × market value impact

### Expected Loss (EL)

**Definition**: PD × LGD × EAD = expected loss from borrower default

**Where**:
- PD (Probability of Default): % chance borrower defaults within 1 year (from ratings: B = ~5% PD, CCC = ~20% PD)
- LGD (Loss Given Default): % of exposure not recovered; inverse of recovery rate (recovery 60% → LGD 40%)
- EAD (Exposure at Default): total outstanding principal + accrued interest at time of default

**Portfolio EL**:
- Portfolio EL = Σ(EL_i) for all positions
- Used for: credit loss reserving, pricing, pricing new positions
- Example: $100M portfolio, blended PD = 3%, blended LGD = 40% → portfolio EL = $1.2M

**Link to Return Requirements**:
- Required return on credit position must exceed expected loss. Example: if EL = 1.2%, required return ≥ 1.5–2.0% to account for unexpected loss and profit margin

### Unexpected Loss (UL)

**Definition**: Standard deviation of loss distribution around expected loss; captures tail risk and concentration effects.

**Calculation**:
- Single position: UL = Volatility of returns (spread volatility, duration volatility)
- Portfolio: UL = Σ Correlation × individual volatilities; amplified by concentration and correlated defaults

**Portfolio Implication**:
- Diversified portfolio: UL ≈ weighted average individual UL
- Concentrated portfolio (few large positions): UL significantly higher due to correlation effects
- Example: 100-name portfolio vs 10-name portfolio: the 10-name portfolio has 50%+ higher UL despite same average credit quality

**Economic Capital Requirement**:
- Economic capital = Confidence level × UL
- 99% VaR = 2.33 × UL for normally distributed returns
- If portfolio UL = 2%, then 99% 1-year capital at risk ≈ 4.7% of NAV

### Credit VaR

**Definition**: Maximum portfolio loss at a given confidence level over a specified horizon.

**Standard VaR Definition**: 99% 10-day VaR = 99% likelihood portfolio loses no more than X% in 10-day period (1% chance of larger loss)

**Calculation Methods**:

**1. Parametric VaR** (Variance-Covariance):
- Assume credit spread changes are normally distributed
- VaR = Mean spread move + 2.33 × Std Dev of spread move (for 99% confidence)
- Advantage: simple, computationally fast
- Disadvantage: ignores non-normal tails (credit markets exhibit fat tails; actual losses often exceed VaR in stress)

**2. Historical Simulation**:
- Use actual historical spread moves (not assumed distribution)
- Example: analyze past 500 trading days; find largest 5 widening days (99th percentile); apply to current portfolio
- Advantage: captures real market behavior, tail events
- Disadvantage: backward-looking; assumes future similar to past

**3. Monte Carlo Simulation**:
- Simulate 10,000+ scenarios of correlated default events and spread changes
- Generate random economic scenarios (recession, rate shock, credit freeze); calculate portfolio impact in each
- Calculate 99th percentile loss across scenarios
- Advantage: captures correlation dynamics, multiple risk factors
- Disadvantage: computationally expensive; dependent on model assumptions

**VaR Limitations**:
- Does NOT capture tail risk beyond the chosen confidence level (99% VaR tells you nothing about the 0.5% worst case)
- Backward-looking (assumes past volatility = future volatility; breaks in crisis)
- Does not work well in credit markets (defaults are rare/sudden; spreads exhibit jumps not smooth moves)
- Does not account for liquidity risk (can't always exit positions at mark)

**Better Alternative: Expected Shortfall (CVaR)**:
- Average loss beyond VaR threshold
- Example: instead of "99% VaR = 5% loss", use "99% CVaR = average loss in worst 1% of scenarios = 8% loss"
- More conservative; better captures tail risk

---
