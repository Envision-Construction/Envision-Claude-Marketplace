---
last_updated: "2026-03-22"
---

# Correlation-Adjusted Position Sizing

A framework for identifying, measuring, and managing correlated risk exposures across a credit portfolio, and translating correlation measurement into actionable position sizing adjustments. Sector concentration is necessary but insufficient — factor-based correlation analysis reveals hidden linkages that can amplify losses during stress events.

---

### Correlation Risk Fundamentals

#### Factor-Based Correlation Framework

Credit portfolios are exposed to common risk factors that can cause simultaneous deterioration across seemingly unrelated names. The four primary factor categories:

##### Interest Rate Sensitivity

| Factor | High Exposure | Low Exposure |
|---|---|---|
| Floating-rate proportion | >80% floating-rate portfolio (leveraged loan heavy) | Balanced fixed/floating mix |
| Duration mismatch | Funded with short-term liabilities, invested in long-duration assets | Asset-liability duration matched |
| Refinancing wall | >20% of portfolio matures within 12 months | Staggered maturity profile |
| Rate shock impact | Borrowers with <1.5x interest coverage at current rates | Borrowers with >3.0x coverage with 200 bps rate buffer |

**Monitoring metric:** Portfolio-weighted interest coverage sensitivity — calculate coverage ratio at base, +100 bps, +200 bps, and +300 bps scenarios.

##### Energy Price Exposure

| Exposure Type | Direct | Indirect |
|---|---|---|
| Revenue linkage | E&P, oilfield services, midstream, utilities | Airlines, chemicals, transportation, agriculture |
| Cost linkage | Energy-intensive manufacturing, logistics | Consumer discretionary (fuel costs reduce spending) |
| Correlation direction | Positive (higher energy = higher revenue) | Negative (higher energy = higher costs / lower demand) |

**Monitoring metric:** Portfolio revenue-weighted energy beta — estimate the percentage change in aggregate portfolio EBITDA for a $20/bbl move in WTI.

##### Consumer Spending Sensitivity

| Sensitivity Tier | Sectors | Typical Revenue Decline in Recession |
|---|---|---|
| High cyclicality | Retail, restaurants, leisure, autos, homebuilding | 15-30% peak-to-trough |
| Moderate cyclicality | Healthcare services, business services, media | 5-15% peak-to-trough |
| Low cyclicality | Food & beverage, utilities, defense, waste management | 0-5% peak-to-trough |

**Monitoring metric:** Consumer-sensitive exposure as a percentage of NAV, weighted by cyclicality tier.

##### Regulatory and Political Risk Correlation

| Risk Type | Affected Sectors | Portfolio Impact |
|---|---|---|
| Healthcare policy | Hospitals, pharma, managed care, medical devices | Reimbursement changes can affect 15-20% of typical HY portfolio |
| Environmental regulation | Energy, chemicals, industrials, utilities | Compliance costs and stranded asset risk |
| Trade / tariff policy | Manufacturing, retail (import-dependent), agriculture | Supply chain disruption and margin compression |
| Tax policy | Pass-through entities, REITs, MLPs | Distribution sustainability and structural viability |

**Monitoring metric:** Regulatory-correlated exposure — percentage of NAV where a single regulatory change could affect >10% of the issuer's EBITDA.

#### Issuer-Level Overlap Analysis

Beyond factor correlations, direct business linkages create concentrated risk:

##### Shared Customer Risk

| Overlap Type | Detection Method | Threshold for Action |
|---|---|---|
| Common top-5 customer | Cross-reference customer disclosures across portfolio names | 3+ issuers sharing a top-5 customer |
| Single-customer dependency | Revenue concentration >15% from one customer | Monitor customer credit quality as separate risk factor |
| Government/contract dependence | Multiple issuers reliant on same government program or contract cycle | Aggregate contract-dependent revenue >10% of portfolio NAV |

##### Shared Supplier / Input Risk

| Overlap Type | Detection Method | Threshold for Action |
|---|---|---|
| Common critical supplier | Supply chain mapping for top portfolio exposures | 3+ issuers with common sole-source supplier |
| Input cost correlation | Raw material or component cost sensitivity | >15% of portfolio EBITDA sensitive to same input price |

##### Sponsor Overlap

| Overlap Type | Risk | Threshold for Action |
|---|---|---|
| Same PE sponsor across multiple portfolio names | Correlated LME risk, dividend behavior, management playbook | >5% of NAV controlled by a single sponsor |
| Same management team or board members | Correlated operational decisions, governance risk | Flag for IC awareness when identified |

#### Sector Concentration vs. Factor Concentration

Sector concentration and factor concentration can diverge significantly:

| Scenario | Sector View | Factor View | True Risk |
|---|---|---|---|
| Healthcare + Tech portfolio | Diversified (two sectors) | Concentrated (both consumer-spending sensitive) | Higher than sector view suggests |
| Energy producers + airlines | Concentrated (both transportation-adjacent) | Diversified (negatively correlated to energy prices) | Lower than sector view suggests |
| Multi-sector leveraged buyout portfolio | Diversified (5+ sectors) | Concentrated (all floating-rate, all sponsor-backed, all covenant-lite) | Significantly higher than sector view suggests |

**Key insight:** A portfolio that passes all sector concentration limits can still have dangerous factor concentration. Factor analysis must supplement, not replace, sector-level monitoring.

#### Event-Driven Contagion

How one credit event propagates through a portfolio:

##### Contagion Channels

| Channel | Mechanism | Speed | Mitigation |
|---|---|---|---|
| Sector repricing | Default in one name widens spreads for entire sector cohort | 1-5 business days | Diversification across sub-sectors, not just GICS sectors |
| Supplier/customer chain | Default disrupts supply or demand for connected companies | 1-4 weeks | Supply chain mapping, alternative supplier analysis |
| Sponsor behavior | Sponsor experiences losses in one company, reduces support for others | 1-3 months | Sponsor portfolio diversification limits |
| Market sentiment | "Guilt by association" — similar business models repriced regardless of fundamentals | 1-10 business days | Maintain conviction documentation for unaffected names |
| Structural contagion | CLO or fund forced selling due to one name's downgrade triggers broader selling | 1-2 weeks | Monitor CLO/fund ownership concentration |

##### Contagion Severity Estimation

| Portfolio Overlap | Expected Additional Spread Impact | Position Action |
|---|---|---|
| Direct business linkage (customer/supplier) | 50-150 bps widening | Immediate review of connected positions |
| Same sector, no direct linkage | 25-75 bps widening | Monitor, update models with sector-wide stress |
| Same sponsor, different sector | 10-50 bps widening | Review sponsor support capacity |
| No connection beyond market sentiment | 0-25 bps widening (temporary) | No action unless fundamental thesis changes |

#### Practical Monitoring Tools

##### Correlation Heat Map Template

Build a quarterly correlation matrix covering the top 20 portfolio exposures:

| | Name A | Name B | Name C | ... |
|---|---|---|---|---|
| **Name A** | 1.00 | [corr] | [corr] | |
| **Name B** | [corr] | 1.00 | [corr] | |
| **Name C** | [corr] | [corr] | 1.00 | |

**Data sources for correlation estimation:**
- Trailing 90-day loan price or spread change correlation (where traded)
- CDS spread correlation (where available)
- EBITDA growth correlation (using quarterly financials, 8-quarter lookback)
- Qualitative overlay for business linkages not captured in market data

**Flagging thresholds:** Pairwise correlation >0.6 between any two top-20 names requires documentation of the linkage and combined exposure limit.

##### Top-10 Factor Exposures Report

Produce quarterly for IC review:

| Rank | Risk Factor | Portfolio Exposure (% NAV) | Stress Scenario | Estimated P&L Impact |
|---|---|---|---|---|
| 1 | [e.g., Floating-rate sensitivity] | [X%] | [+200 bps rate shock] | [($X.Xmm)] |
| 2 | [e.g., Consumer discretionary cycle] | [X%] | [15% revenue decline] | [($X.Xmm)] |
| ... | | | | |

---

## 1. Correlation Measurement

Portfolio correlation arises from shared exposure to common risk factors. The four primary dimensions:

### Sector Overlap
- Measure using GICS sector and sub-industry classification
- **Same GICS sector:** Moderate correlation (assign overlap factor 0.3-0.5 depending on sub-industry similarity)
- **Same GICS sub-industry:** High correlation (assign overlap factor 0.6-0.8)
- **Adjustment for diversified companies:** Use revenue-weighted sector exposure rather than primary GICS classification

### Sponsor Overlap
- Relevant for leveraged finance portfolios with PE-backed credits
- **Same sponsor:** High correlation (assign overlap factor 0.5-0.7) — sponsors may pursue similar operational strategies and financial policies across portfolio companies
- **Same sponsor fund vintage:** Very high correlation (assign overlap factor 0.7-0.9) — fund-level liquidity pressure may force simultaneous adverse actions across portfolio companies
- **Co-invested sponsors:** Moderate correlation (assign overlap factor 0.2-0.4)

### Supply Chain Linkage
- **Customer concentration:** If new position shares a top-5 customer with existing position, assign overlap factor 0.3-0.5
- **Supplier dependence:** Shared critical supplier (sole source or >30% of input costs), assign overlap factor 0.2-0.4
- **Geographic supply chain:** Common geographic risk (single manufacturing region, port dependency), assign overlap factor 0.1-0.3

### Geographic Concentration
- **Same country:** Low-moderate overlap (assign factor 0.1-0.2 for developed markets; 0.3-0.5 for emerging markets where sovereign risk is more correlated with corporate)
- **Same region/state:** Moderate overlap for regionally concentrated industries (assign factor 0.2-0.3)
- **Single-asset location risk:** For CRE or project finance with geographic concentration, assign factor 0.3-0.5

---

## 2. Correlation Matrix Construction

### Factor-Based Approach
Construct a simplified correlation matrix using weighted factor exposures rather than historical return correlations (which require long time series and may not capture structural linkages).

#### Step 1: Identify Factor Exposures
For each position, assign factor exposure scores (0.0 to 1.0) across the following factors:

| Factor | Measurement | Source |
|---|---|---|
| Sector beta | Revenue exposure by GICS sector | Company filings, industry classification |
| Sponsor exposure | PE sponsor identity and fund vintage | Deal documentation, PitchBook |
| Commodity sensitivity | Revenue/cost exposure to commodity prices | Company filings, industry analysis |
| Interest rate sensitivity | Floating-rate debt proportion, interest coverage cushion | Credit agreement, financial model |
| Consumer discretionary | Revenue exposure to consumer spending | Company filings, industry analysis |
| Cyclicality | Revenue volatility through economic cycles | Historical financials, industry-sector-analysis |

#### Step 2: Calculate Pairwise Correlation Estimate
For any two positions (A and B), estimate pairwise correlation:

Pairwise Correlation(A,B) = Sum of [Factor Weight(i) x min(Exposure_A(i), Exposure_B(i))] for each factor i

Factor weights should sum to 1.0 and reflect the portfolio's primary risk drivers. Typical weights:

| Factor | Weight |
|---|---|
| Sector beta | 0.30 |
| Sponsor exposure | 0.20 |
| Commodity sensitivity | 0.15 |
| Interest rate sensitivity | 0.15 |
| Consumer discretionary | 0.10 |
| Cyclicality | 0.10 |

#### Step 3: Construct Matrix
- Populate the N x N correlation matrix for all portfolio positions
- Diagonal entries = 1.0 (each position is perfectly correlated with itself)
- Matrix must be symmetric: Correlation(A,B) = Correlation(B,A)

---

## 3. Sizing Formula

### Base Position Size
The base position size is determined by the standard position sizing framework (IC-approved size, typically 1-3% of portfolio NAV for liquid credits, 2-5% for private credits).

### Correlation Adjustment Calculation

**Adjusted Position Size = Base Position Size x (1 - Correlation Adjustment Factor)**

Where:

**Correlation Adjustment Factor = Weighted Average of Overlap Factors between the new position and all existing portfolio positions, weighted by existing position sizes**

#### Detailed Calculation

1. For each existing position (j) in the portfolio, calculate the pairwise overlap with the new position using the factor-based approach from Section 2
2. Weight each pairwise overlap by the existing position's share of portfolio NAV
3. Sum the weighted overlaps to get the Correlation Adjustment Factor
4. Apply the adjustment to reduce the base position size

**Correlation Adjustment Factor = Sum of [Position_Weight(j) x Pairwise_Correlation(new, j)] for all existing positions j**

### Worked Example

**Portfolio context:** $500M portfolio, considering adding $15M (3.0% base size) position in a BB-rated auto parts manufacturer.

Existing correlated positions:

| Position | Size (% NAV) | Sector Overlap | Sponsor Overlap | Supply Chain | Pairwise Correlation |
|---|---|---|---|---|---|
| Auto OEM (Position A) | 2.5% | 0.7 (same sub-industry) | 0.0 | 0.5 (customer) | 0.38 |
| PE-backed industrial (Position B) | 2.0% | 0.3 (same sector) | 0.6 (same sponsor) | 0.0 | 0.27 |
| Tire manufacturer (Position C) | 1.5% | 0.5 (adjacent) | 0.0 | 0.3 (supplier) | 0.22 |

Correlation Adjustment Factor = (0.025 x 0.38) + (0.020 x 0.27) + (0.015 x 0.22) = 0.0095 + 0.0054 + 0.0033 = 0.0182

Since the Correlation Adjustment Factor is expressed relative to the full portfolio, normalize to the relevant correlated subset:

Effective Adjustment = 0.0182 / 0.06 (sum of correlated position weights) = 0.303

**Adjusted Position Size = $15M x (1 - 0.303) = $10.5M (2.1% of NAV)**

The correlation adjustment reduces the position from 3.0% to 2.1% of NAV, reflecting the concentrated exposure to auto sector and shared sponsor risk.

---

## 4. Correlation Stress Scenarios

### Correlation Spike Modeling
In stress environments, correlations increase toward 1.0 as systematic risk dominates idiosyncratic factors. Model the portfolio-level impact:

#### Stress Scenario Parameters

| Scenario | Correlation Assumption | When to Apply |
|---|---|---|
| Base case | Factor-based estimates from Section 2 | Normal market conditions |
| Moderate stress | Factor-based x 1.5, capped at 0.8 | Sector-specific downturn |
| Severe stress | All same-sector positions at 0.9, cross-sector at 0.5 | Recession, broad credit selloff |
| Tail stress | All positions at 1.0 within top-3 sectors | Worst-case concentration test |

#### Portfolio Impact Assessment
For each stress scenario:
1. Recalculate portfolio variance using stressed correlation assumptions
2. Compute portfolio VaR and expected loss under stressed correlations
3. Identify the maximum simultaneous loss across correlated positions
4. Test whether risk limits (single-name, sector, total portfolio) are breached under stressed correlations

### Sector Concentration Stress Test
- Identify the top-3 sectors by portfolio weight
- Apply simultaneous spread widening of 300-500 bps to all positions in each sector
- Assume recovery rates decline by 10-15 percentage points from base case
- Calculate portfolio-level P&L impact and compare against risk appetite limits from `references/risk-appetite-and-limit-framework.md`

---

## 5. Practical Application

### Decision Framework

| Correlation Adjustment Factor | Sizing Action | Rationale |
|---|---|---|
| <5% | No adjustment needed | Minimal incremental correlation risk |
| 5-15% | Reduce base size by adjustment factor | Moderate correlation warrants smaller position |
| 15-30% | Reduce base size by adjustment factor; flag for PM review | Material correlation risk; requires explicit PM acknowledgment |
| >30% | Reduce base size; requires IC-level discussion | High correlation concentration; position adds meaningful portfolio-level tail risk |

### Sizing with and without Adjustment: Summary

| Metric | Without Adjustment | With Adjustment |
|---|---|---|
| Position size | $15.0M (3.0%) | $10.5M (2.1%) |
| Sector exposure (auto) | 9.5% of NAV | 8.1% of NAV |
| Sponsor exposure | 5.0% of NAV | 4.1% of NAV |
| Max correlated loss (severe stress) | $32.5M (6.5%) | $27.3M (5.5%) |
| Within sector concentration limit (15%) | Yes | Yes (larger buffer) |

### Cross-Reference
- For portfolio-level risk limits and concentration constraints, see `references/portfolio-risk-parameters.md`
- For stress testing parameters by asset class, see `references/stress-scenario-framework.md`
- For BDC-specific concentration or leverage constraints, see `skills/private-credit-middle-market/references/bdc-regulatory.md`; otherwise use the governing vehicle documents.
