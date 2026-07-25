---
last_updated: "2026-03-21"
---

## Commercial Real Estate Credit Metrics

CRE credit analysis mirrors corporate finance but substitutes property-level cash flows (NOI) for EBITDA and appraised values for enterprise value. The shift is from entity-level metrics (what the company earns) to asset-level metrics (what the property produces).

### NOI (Net Operating Income)

**Definition**: Total revenue minus operating expenses. CRE equivalent of corporate EBITDA.

**Formula**:
```
NOI = Gross Potential Rent (GPR) - Vacancy Loss + Other Income - Operating Expenses
    = Effective Gross Income (EGI) - Operating Expenses
```

**Components**:
- **Gross Potential Rent**: Total rent if property is 100% occupied
- **Vacancy Loss**: Estimated or actual vacancy (e.g., 5–10% for stabilized assets)
- **Other Income**: Parking fees, laundry, late fees, management fees (very property-type dependent)
- **Operating Expenses**: Taxes, insurance, maintenance, utilities, property management, HOA
- **NOT included**: Debt service, capital expenditures, tenant improvements

**Key Versions** (Lenders are cynical about which version is used):
- **In-place NOI**: Based on actual current rents from executed leases (most conservative)
- **Stabilized NOI**: Assumes property reaches 95%+ occupancy at market rents (most optimistic)
- **Pro forma NOI**: Projections after repositioning (e.g., after renovations; intermediate optimism)
- **Underwriter's NOI**: Conservative version lender applies for covenant testing (usually in-place + modest upside)

**Lender practice**: Most use in-place or underwriter's NOI for initial underwriting; test stability against stressed (lower) NOI scenarios.

**Example**:
```
Office Building
Gross Potential Rent: $10M (100% occupancy)
Current Occupancy: 88%
Effective Gross Income: $8.8M
Operating Expenses: $3.3M (33% ratio)
NOI: $8.8M - $3.3M = $5.5M
```

### Cap Rate (Capitalization Rate)

**Definition**: Unleveraged yield on property investment (property value in isolation, ignoring financing).

**Formula**:
```
Cap Rate = NOI / Property Value
```

**Interpretation**:
- **Inverse relationship**: Lower cap rate = higher property value (expensive); higher cap rate = lower value (cheap)
- **Market-derived**: Cap rate reflects market's required unlevered yield; varies by property type, quality, location, tenant credit, lease term, market cycle
- **Risk measure**: Cap rate spread to risk-free rate (Treasury) = property risk premium

Use `references/market-benchmarks.md` for live cap-rate and spread observations. This file should remain focused on how to interpret the metric, not on storing current market levels.

**Determinants**:
- Property type (office 4–6%, industrial 3.5–5%, retail 4–7%, apartments 3–5%)
- Quality/age (new or recent renovation: lower cap rate; older, deferred maintenance: higher)
- Location (primary market: lower; secondary/tertiary: higher)
- Tenant credit (investment-grade: lower; franchisees/mom-and-pop: higher)
- Lease term remaining (longer lease: lower; short/expiring: higher)
- Market conditions (seller's market: cap rates compress; buyer's market: cap rates expand)

**Example**:
```
Property: $50M apartment complex
Stabilized NOI: $5.0M
Cap Rate: $5.0M / $50M = 10.0%
Interpretation: If property were 100% equity-financed, investor earns 10% unlevered.

If market cap rate for this property type/location is 5.5%:
Implied Value: $5.0M NOI / 5.5% = $90.9M
Property is EXPENSIVE relative to comparable sales; buyer paying premium.
```

### DSCR (Debt Service Coverage Ratio) — CRE Context

**Definition**: NOI divided by annual debt service. Tests ability to pay interest + principal from operations.

**Formula**:
```
DSCR = NOI / Annual Debt Service
Annual Debt Service = Interest + Principal Amortization
```

**Underwriting convention**:
- DSCR minimums depend on lender type, amortization, recourse, and asset stability
- Use `references/typical-deal-parameters.md` for current market convention ranges
- Treat DSCR as one of several simultaneous constraints rather than a standalone approval test

**DSCR Variants**:
- **In-place DSCR**: Based on current NOI from actual leases
- **Stabilized DSCR**: Based on projected NOI at stabilization
- **Amortizing DSCR**: DSCR with full debt service (interest + principal)
- **Interest-only DSCR**: DSCR with only interest payments (balloon note at end)

**Stressed DSCR** (Lender due diligence):
- **Rate-up stress**: Apply a benchmark-rate shock using `references/stress-scenario-framework.md`
- **Vacancy stress**: Increase vacancy or downtime and recalculate NOI
- **Expense stress**: Raise insurance, taxes, and operating expenses where relevant

**Example**:
```
Apartment Building
Stabilized NOI: $6.0M
Senior Debt: $40M at 5.0%, 25-year amort
Annual Interest: $40M × 5% = $2.0M
Annual Principal: $40M / 25 = $1.6M
Total Debt Service: $2.0M + $1.6M = $3.6M

DSCR: $6.0M / $3.6M = 1.67x ✓ (strong; lender minimum is 1.25x)

Stressed: If rates rise to 7.0%
Annual Interest: $40M × 7% = $2.8M
Annual Principal: $1.6M (unchanged)
Total Debt Service: $4.4M
Stressed DSCR: $6.0M / $4.4M = 1.36x ✓ (still above 1.25x, passes stress)
```

### Debt Yield (CRE Metric)

**Definition**: NOI divided by loan amount. Increasingly the primary sizing metric (replacing DSCR) because it's rate-independent and amortization-independent.

**Formula**:
```
Debt Yield = NOI / Loan Amount
```

**Interpretation**:
- Inverse analog of **Debt/EBITDA** in corporate finance
- Debt yield of 10% ≈ 10x Debt/NOI ≈ same as corporate 10x Debt/EBITDA leverage
- Minimum acceptable debt yield depends on asset quality, sponsorship, cash-flow durability, and lender mandate
- Use `references/typical-deal-parameters.md` for current convention ranges

**Why Lenders Prefer Debt Yield**:
- **Rate-independent**: Doesn't change if interest rates change (unlike DSCR)
- **Amortization-independent**: Doesn't matter if loan is IO or amortizing (unlike DSCR)
- **Direct comparison**: Easier to size loans across different property types (all benchmarked to NOI yield)

**Example**:
```
Bridge Loan Underwriting
Property NOI: $4.0M
Target Debt Yield: 10%
Implied Loan Size: $4.0M / 10% = $40M
Property Value: $50M
LTV: $40M / $50M = 80%

This sizing is independent of interest rate. Whether loan rates are 6% or 8%, debt yield remains 10%.
```

### LTV (Loan-to-Value) — CRE Context

**Definition**: Senior loan divided by appraised property value.

**Formula**:
```
LTV = Loan Amount / Appraised Property Value
```

**Variants** (different valuation dates yield different LTVs):
- **As-is LTV**: Current appraised value (e.g., value-add property at entry, before improvements)
- **As-stabilized LTV**: Appraised value assuming full repositioning/stabilization
- **As-completed LTV**: Appraised value upon project completion (construction loans)

**Underwriting convention**:
- Acceptable LTV varies with asset quality, market liquidity, lender type, recourse, and business plan risk
- Use `references/typical-deal-parameters.md` for current leverage conventions rather than hard-coding them here

**Relationship to Cap Rate and NOI**:
- Higher cap rate (riskier property) → lower LTV
- Lower cap rate (safer property) → higher LTV
- Higher DSCR → ability to support higher LTV (property generating more coverage)

**Example**:
```
Core Apartment
Appraised Value: $100M (as-stabilized)
Senior Loan: $70M
LTV: 70% (typical for institutional lender)

Value-Add Apartment
As-is Value (current): $50M
As-stabilized Value (post-reno): $75M
Senior Loan: $60M
As-is LTV: 60% / $50M = 120% (over 100%! lender is relying on stabilization)
As-stabilized LTV: $60M / $75M = 80%
```

### Breakeven Occupancy

**Definition**: Occupancy level at which property cash flow is zero (cannot pay debt service or operating expenses).

**Formula**:
```
Breakeven Occupancy % = (Operating Expenses + Annual Debt Service) / Gross Potential Rent
```

**Interpretation**:
- Lower breakeven occupancy = safer (property can cover debt even at lower occupancy)
- **Comfortable threshold**: 75–85% for most property types
- **Risky**: Breakeven >85%; property has no room for vacancy

**Example**:
```
Office Building
Gross Potential Rent: $10M
Operating Expenses: $3.0M
Annual Debt Service: $2.0M
Total Obligations: $5.0M
Breakeven Occupancy: $5.0M / $10M = 50%

Interpretation: Even if property is only 50% occupied, tenant rents cover debt + operating costs.
This is VERY safe. Property could lose 39% of tenants and still service debt.

Compare to risky scenario:
GPR: $10M, OpEx: $4.5M, Debt Service: $4.0M
Breakeven: ($4.5M + $4.0M) / $10M = 85%
If occupancy drops below 85%, property is cash-flow negative (lender concerned).
```

### Operating Expense Ratio

**Definition**: Annual operating expenses divided by effective gross income.

**Formula**:
```
OpEx Ratio = Operating Expenses / Effective Gross Income (EGI)
```

**Benchmarking note**:
- Operating expense ratios vary materially by property type, age, service level, utility burden, and tax regime
- Use `references/market-benchmarks.md` for current market observations
- Use local property comps and borrower operating statements for actual underwriting

**Key Components** (major expense categories):
- Property taxes (10–20% of revenue, varies by jurisdiction)
- Insurance (1–3% of revenue)
- Utilities (varies: office/retail 5–15%, apartments 3–8%)
- Maintenance/repairs (3–8%)
- Management (4–7%)
- Vacancy reserves / bad debt (1–3%)

**Red Flags**:
- OpEx ratio rising over time (cost control issues)
- OpEx ratio well above market norm for property type (operational inefficiency)
- Deferred maintenance (expenses will spike when repairs are made)

**Example**:
```
Stabilized Apartment
EGI: $8.5M (after vacancy loss)
Total OpEx: $3.2M
OpEx Ratio: $3.2M / $8.5M = 37.6%
Comparison: Market average for similar class/location = 38–42%
Assessment: Right on market; no red flags
```

### Comparison: CRE vs Corporate Credit Metrics

| Corporate Metric | CRE Equivalent | Notes |
|---|---|---|
| EBITDA | NOI | Operating income before D&A; comparable cash generation |
| Revenue | Gross Potential Rent (GPR) or EGI | Top-line income |
| Debt/EBITDA | Debt/NOI or Debt Yield inverse | Leverage comparison |
| Interest Coverage (EBITDA/Interest) | NOI/Interest | Tests interest payment ability |
| DSCR (corporate) | DSCR (real estate) | Debt service capacity; similar formula |
| Cap Structure / LTV | Similar | Debt as % of total value |
| EV/EBITDA (valuation) | Price/Cap Rate | Inverse relationship; lower cap = higher valuation |

**Key Difference**: CRE analysis is fundamentally **asset-based** (property value, tenancy, and NOI), while corporate analysis is **entity-based** (company-wide cash flow and balance-sheet flexibility). Compare the metrics carefully, but avoid assuming that a seemingly similar ratio carries the same risk meaning in both contexts.

---
