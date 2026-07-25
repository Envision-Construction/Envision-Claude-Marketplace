---
title: "Option-Adjusted Spread (OAS) Methodology"
last_updated: "2026-03-22"
update_cadence: "Annual"
next_review: "2027-03-22"
type: "analysis"
---

## Option-Adjusted Spread (OAS) Methodology

### Overview

The option-adjusted spread (OAS) is the constant spread added to a benchmark interest rate curve that equates a security's model-derived theoretical price to its observed market price, after accounting for embedded optionality. For structured products, the primary embedded option is the borrower's right to prepay, which creates path-dependent cash flows that cannot be captured by static spread measures. OAS isolates the credit and liquidity compensation an investor earns after removing the cost of optionality.

OAS is the standard relative value metric for comparing securities with different embedded options, prepayment profiles, or structural features. It allows analysts to compare an agency MBS pass-through against a non-agency RMBS sequential tranche or a CMBS conduit bond on a consistent basis.

### OAS Calculation Framework

The calculation proceeds in five steps:

**Step 1 — Interest Rate Path Generation**

A stochastic interest rate model generates a large number of possible future interest rate paths, typically 500-2,000 paths using Monte Carlo simulation. Common models include:

- **Lognormal short-rate models** (Black-Karasinski, Black-Derman-Toy): Ensure non-negative rates, calibrated to the current yield curve and swaption volatility surface
- **LIBOR/SOFR Market Models**: Calibrated directly to observed cap/floor and swaption prices
- **Hull-White**: Mean-reverting single-factor model; tractable but may underfit volatility smile

Each path produces a sequence of monthly or quarterly short rates from the valuation date through the security's legal final maturity. The model must be arbitrage-free — the average present value of a risk-free cash flow across all paths must equal its observed market price.

**Step 2 — Prepayment Model Integration**

For each interest rate path, a prepayment model generates the projected prepayment speed at each time step. The prepayment model takes as inputs:

- **Refinancing incentive**: Difference between the pool's weighted average coupon and the prevailing market rate on each path
- **Burnout**: Reduction in prepayment sensitivity as rate-sensitive borrowers exit the pool
- **Seasoning**: Ramp-up pattern for new originations (PSA-style)
- **Seasonality**: Cyclical variation in housing turnover by calendar quarter
- **Housing turnover**: Baseline prepayment from home sales independent of rate incentive
- **Credit and default behavior**: CDR and loss severity assumptions for non-agency collateral

The prepayment model converts these inputs into a conditional prepayment rate (CPR) for each month on each path. See `references/cash-flow-metrics-and-prepayment.md` for detailed prepayment conventions and cash flow behavior.

**Step 3 — Cash Flow Projection**

Using the path-specific prepayment, default, and loss severity assumptions, project scheduled principal, interest, and prepayment cash flows for each month on each path. For structured tranches, apply the deal's waterfall rules (sequential pay, pro-rata, shifting interest, etc.) to allocate pool-level cash flows to the specific tranche. This step captures structural features including:

- Credit enhancement mechanics (subordination, excess spread, reserve accounts)
- Trigger tests (delinquency, cumulative loss, OC/IC tests) that redirect cash flows
- Clean-up call provisions
- Step-down dates and lockout periods

**Step 4 — Discounting**

For each path, discount the projected tranche cash flows back to the valuation date using the path-specific short rates plus a trial spread (the candidate OAS). The present value for path *i* is:

PV_i = Sum over t of [ CF_i(t) / Product over s of (1 + r_i(s) + OAS) ]

where CF_i(t) is the cash flow at time t on path i, and r_i(s) is the short rate at time s on path i.

**Step 5 — Solve for OAS**

The OAS is the single constant spread that satisfies:

Market Price = (1/N) × Sum over i of PV_i(OAS)

where N is the number of Monte Carlo paths. The solver iterates on OAS (typically using Newton-Raphson or bisection) until the average present value across all paths equals the observed market price. A wider OAS implies the market demands more compensation for credit, liquidity, and model risk after accounting for optionality.

### Prepayment Conventions

Prepayment conventions standardize how prepayment speeds are expressed and compared across asset types:

| Convention | Definition | Formula | Typical Use |
|---|---|---|---|
| CPR (Conditional Prepayment Rate) | Annualized percentage of remaining principal prepaid | CPR = 1 - (1 - SMM)^12 | Universal; primary metric for all MBS and ABS |
| SMM (Single Monthly Mortality) | Monthly percentage of remaining principal prepaid | SMM = 1 - (1 - CPR)^(1/12) | Monthly cash flow modeling |
| PSA (Public Securities Association) | Standardized ramp: CPR increases 0.2%/month for 30 months, then plateaus at 6.0% CPR | 100% PSA = 6% CPR at month 30+ | Agency MBS structuring and rating agency models |
| CDR (Constant Default Rate) | Annualized percentage of remaining principal that defaults | CDR = 1 - (1 - MDR)^12 | Non-agency RMBS, ABS, CLO collateral |
| ABS (Absolute Prepayment Speed) | Fixed monthly percentage of original (not remaining) balance prepaid | ABS = prepaid / original balance | Auto ABS, equipment ABS |

**CPR-SMM Conversion:**
- SMM = 1 - (1 - CPR)^(1/12)
- CPR = 1 - (1 - SMM)^12
- Example: 10% CPR = 0.874% SMM; 20% CPR = 1.842% SMM

Prepayment behavior varies materially by product. Mortgage products are usually the most rate-sensitive, consumer ABS often depends more on borrower or asset turnover, and CMBS can remain effectively locked until prepayment protection opens. Use product-specific assumptions and current root benchmarks rather than relying on static ranges.

### OAS Decomposition

The total OAS earned by an investor compensates for multiple risk factors. Decomposing OAS into components enables more precise relative value analysis:

**Components:**

- **Credit component**: Compensation for expected and unexpected credit losses. Estimated by comparing OAS of the target security to a comparable-duration, comparable-optionality security with negligible credit risk (e.g., agency MBS for prepayment-exposed securities). For structured tranches, this reflects both collateral credit quality and the tranche's position in the waterfall.

- **Liquidity component**: Compensation for the cost of unwinding the position. Wider for off-the-run, bespoke, or thinly traded securities. Estimated by comparing on-the-run versus off-the-run spreads for similar-risk securities, or by observing bid-ask spread differentials.

- **Optionality component**: The cost of embedded options not fully captured by the prepayment model. If the prepayment model perfectly captured borrower behavior, this component would be zero. In practice, model imprecision leaves residual optionality cost embedded in the OAS. Estimated as the difference between OAS and Z-spread for securities where the Z-spread captures the static cash flow value.

- **Model risk component**: Compensation demanded by the market for uncertainty in the valuation model itself — prepayment model specification, interest rate process assumptions, and correlation structure. This component is unobservable but can be inferred as the residual after estimating credit, liquidity, and optionality components.

The decomposition is conceptual rather than fixed. Credit, liquidity, optionality, and model risk all matter, but their weight changes with product type and market regime. Use `references/market-benchmarks.md` for current spread context rather than treating any static decomposition table as durable truth.

### Interpretation Guidance

**When OAS Overstates Value (security appears cheaper than it is):**

- **Negative convexity environments**: When interest rates are near the pool's weighted average coupon, prepayment optionality is at its peak. If the prepayment model underestimates the speed or asymmetry of the borrower response, the OAS will appear artificially wide. This is most dangerous for premium-coupon MBS in a declining rate environment.
- **Extension risk**: If the model underestimates the probability of slow prepayments in a rising rate environment, it understates duration extension. A wide OAS may simply reflect unmodeled extension risk rather than genuine cheapness.
- **Adverse selection in seasoned pools**: Remaining borrowers in a heavily refinanced pool may have worse credit profiles than the pool average. The prepayment model may not capture this tail-risk deterioration.
- **Trigger risk in structured deals**: If a deal is near a delinquency or loss trigger that would redirect cash flows (shifting from pro-rata to sequential pay, trapping excess spread), OAS may not reflect the binary nature of this risk.

**When OAS Understates Value (security appears richer than it is):**

- **Favorable prepayment characteristics**: Specified pools (low-balance, investor property, high-LTV) have structurally lower prepayment speeds. If the model uses a generic prepayment function, OAS will understate the value of the prepayment protection.
- **Call protection**: CMBS with defeasance or yield maintenance provisions, or lockout periods, provide structural call protection that a generic model may undervalue.
- **High credit quality with credit migration upside**: If the underlying collateral is improving (rising home prices, deleveraging borrowers), the credit component of OAS may decline over time — a form of positive carry not captured in static OAS.
- **Seasoning benefit**: Well-seasoned pools with clean performance histories have lower conditional default probabilities than newly originated pools with the same characteristics.

**Red Flags in OAS Analysis:**

- OAS significantly wider than peers with no fundamental explanation — may indicate model miscalibration or data error
- OAS tightening rapidly as prepayment model is recalibrated — suggests the previous OAS was model-driven, not market-driven
- OAS on a deeply subordinated tranche that appears tight — may not capture tail loss scenarios adequately
- OAS computed with an unreasonably small number of Monte Carlo paths (< 500) — results may not be stable
- OAS that changes materially (> 10 bps) when switching between interest rate models — high model sensitivity is itself a risk

### Spread Comparison Framework

Different spread measures serve different purposes. The choice depends on the security's structural features and the analytical question:

| Spread Measure | Definition | Accounts for Optionality? | Accounts for Curve Shape? | Best Used For |
|---|---|---|---|---|
| **G-spread** | Spread over interpolated Treasury yield at matched maturity | No | No (single-point comparison) | Quick relative value for bullet bonds; Treasury-based benchmarking |
| **I-spread** | Spread over interpolated swap rate at matched maturity | No | No (single-point comparison) | LIBOR/SOFR-based relative value; derivatives-linked hedging analysis |
| **Z-spread** (zero-volatility spread) | Constant spread over the entire spot rate curve that equates present value of scheduled cash flows to market price | No | Yes (full curve) | Amortizing securities with no optionality; bonds with known cash flow schedules |
| **OAS** | Constant spread over the spot curve across all Monte Carlo paths, incorporating prepayment and default model output | Yes | Yes (full curve, path-dependent) | Securities with embedded options: MBS, ABS, CMOs, callable bonds |

**Decision Matrix — Which Spread to Use:**

| Situation | Recommended Spread | Rationale |
|---|---|---|
| Comparing two bullet corporate bonds | G-spread or I-spread | No optionality; single cash flow profile |
| Comparing amortizing ABS with minimal prepayment risk (e.g., auto ABS with tight call window) | Z-spread | Cash flows are relatively predictable; Z-spread captures curve shape |
| Comparing two agency MBS pass-throughs with different coupons | OAS | Prepayment optionality differs materially by coupon; static spreads mislead |
| Comparing a CMO PAC tranche to a support tranche | OAS | Optionality exposure is structurally different; OAS normalizes |
| Comparing an agency MBS to a non-agency RMBS tranche | OAS with matched prepayment model framework | Must ensure consistent modeling; even then, credit and liquidity decomposition is needed |
| Relative value across ABS, RMBS, CMBS, CLO | OAS (with careful decomposition) | Different embedded options, credit profiles, and liquidity; OAS is the common language but decomposition is essential |
| Quick screening of large bond universe | I-spread or Z-spread | OAS computation is expensive; screen first, then run OAS on candidates |

### Limitations

**Prepayment Model Accuracy**

OAS is only as reliable as the prepayment model. Model error sources include: S-curve miscalibration (wrong slope or plateau level), failure to capture behavioral heterogeneity within the pool, inability to forecast borrower responses to novel market conditions (e.g., post-COVID forbearance programs), and static loss severity assumptions that ignore housing cycle dynamics. A 5% CPR error in the base case can shift OAS by 15-40 bps for a current-coupon MBS pass-through.

**Interest Rate Model Calibration**

The choice of interest rate model and its calibration to the volatility surface affects the distribution of rate paths. If the model underestimates the probability of extreme rate movements, it understates optionality cost and inflates OAS. Calibration should be checked against current swaption implied volatilities. Single-factor models may not capture yield curve twist scenarios that materially affect structured product cash flows.

**Path-Dependency Assumptions**

Monte Carlo OAS assumes that the average across independent paths is a valid representation of the security's expected value. This breaks down when structural features create strong path-dependency — for example, a deal that has already breached a trigger cannot recover on future paths, but a standard simulation does not condition on the current deal state. For surveillance of seasoned deals, the model should be initialized with actual pool performance, not generic assumptions.

**Homogeneity Assumption in Pool-Level Analysis**

OAS models typically treat the collateral pool as homogeneous, applying a single prepayment and default function to the aggregate. In reality, pools contain loans with diverse borrower characteristics, geographic concentrations, and origination vintages. Loan-level modeling (projecting each loan individually and aggregating) produces more accurate results but is computationally expensive. Pool-level OAS may understate tail risk from concentrated exposures.

**Computational Complexity**

Convergence of Monte Carlo OAS requires a sufficient number of paths. For complex structures (multi-tranche CMOs, CLO equity with reinvestment optionality), 1,000-2,000 paths may be needed, with each path requiring a full waterfall simulation. Variance reduction techniques (antithetic variates, stratified sampling) improve efficiency but add implementation complexity. Real-time trading decisions often rely on pre-computed OAS tables with interpolation rather than live Monte Carlo runs.

**Negative OAS**

A negative OAS can result from model error (the prepayment model assigns too much value to the embedded option) or from genuine market dislocation (the security trades above its theoretical value, which occurs in short-squeeze or flight-to-quality environments). Negative OAS should not be interpreted at face value — investigate the model assumptions before concluding the security is rich.

### Practical Application

When two tranches look different on nominal spread or Z-spread, OAS asks whether that difference is really compensation for credit and liquidity, or simply payment for different optionality.

Use a relative-value comparison like this:

1. Hold the prepayment model framework constant across both tranches.
2. Compare the gap between Z-spread and OAS for each security.
3. Reconcile whether differences are coming from optionality, credit enhancement, seasoning, or liquidity.
4. Treat a large spread gap with no structural explanation as a prompt to check model assumptions before declaring a bond cheap.

**Workflow integration:** After identifying the preferred tranche through OAS analysis, feed the selection into the waterfall analysis framework (`references/cash-flow-metrics-and-prepayment.md`) for full structural review, and reference the credit enhancement mechanics (`references/securitization-structure-and-risk.md`) to stress-test the subordination under adverse scenarios.
