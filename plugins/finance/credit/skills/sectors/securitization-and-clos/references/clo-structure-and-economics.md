---
name: CLO Structure and Economics
description: |
  Comprehensive CLO reference covering tranche economics (senior, mezzanine, equity),
  pool construction and lifecycle (warehouse through maturity), coverage tests and portfolio
  constraints, deal selection criteria, and secondary CLO execution mechanics.
last_updated: "2026-03-22"
---

## CLO Tranches And Economics

A CLO is a managed leveraged-loan pool financed by rated debt and an unrated first-loss equity tranche. The central underwriting question is not "what is the spread?" but rather "who absorbs deterioration first, when does cash get trapped, and how much optionality does the manager actually control?"

### Shared Structural Logic

**Capital stack**
- Senior debt sits highest in the payment waterfall and benefits from the most subordination.
- Mezzanine debt sits below senior debt and is more exposed to test deterioration, extension, and trapped cash.
- Equity receives the residual and is the first-loss position economically.

**Core protections**
- **Subordination** determines how much collateral loss must occur before a tranche takes principal impairment.
- **OC tests** compare collateral value or par to liabilities and can divert cash away from junior tranches when breached.
- **IC tests** compare collateral income to liability cost and can accelerate deleveraging when earnings are squeezed.
- **Reinvestment flexibility** allows the manager to reshape collateral quality, spread, and maturity profile during the active period of the deal.

**Primary underwriting inputs**
- Portfolio quality and concentration
- Remaining reinvestment optionality
- Current and forward test cushion
- Manager behavior under stress
- Liability stack and call or reset optionality

Use `references/market-benchmarks.md` for current spread and enhancement ranges, and use the governing CLO indenture for deal-specific test conventions rather than embedding live numbers here.

### Senior CLO Debt

Senior CLO debt is usually a spread, liquidity, and structural-protection decision rather than a first-loss credit decision.

**What matters most**
- Depth of subordination below the tranche
- Stability of OC and IC tests
- Liquidity profile and mark-to-market risk
- Call, reset, or refinancing behavior that can shorten expected life

**Main risks**
- Spread widening and forced mark-to-market losses
- Downgrades or ratings migration in lower investment-grade tranches
- Extension if the structure amortizes more slowly than expected
- Reduced relative value if the deal resets or refinances away from an attractive liability stack

### Mezzanine CLO Debt

Mezzanine CLO debt is where structural volatility begins to matter as much as contractual coupon.

**What matters most**
- Cushion above the tranche's relevant OC tests
- Speed of collateral migration into CCC or default buckets
- Remaining time for the manager to repair par and trade out of deteriorating credits
- Whether the tranche is being paid enough for cash diversion risk, not just default risk

**Main risks**
- Interest diversion or PIK behavior when tests tighten
- Principal impairment if defaults and haircuts exhaust available cushion
- Call and extension risk that change realized WAL and return
- Episodic liquidity, especially in stressed markets

### CLO Equity

CLO equity is a leveraged residual claim on spread, par build, and remaining optionality after all debt and expenses are satisfied.

**Return drivers**
- Asset-liability arbitrage
- Par creation or destruction through trading and default resolution
- Ability to preserve OC cushion
- Timing of calls, resets, and amortization
- Entry price relative to current and future NAV

**What to analyze**
- Current cash yield versus total return potential
- NAV on both par and market-value lenses
- Whether distributions are being supported by healthy collateral or by temporarily favorable timing
- How much reinvestment runway remains

**Red flags**
- High cash yield with deteriorating NAV
- Stable distributions despite worsening collateral metrics
- Tight test cushions with no realistic path to repair
- Reliance on favorable refinancing or spread assumptions to make returns work

### Analysis Checklist

1. Map the current capital stack and payment priorities.
2. Identify which tests are most likely to bind first.
3. Separate collateral deterioration from market spread volatility.
4. Evaluate manager behavior in both benign and stressed periods.
5. Underwrite terminal value explicitly for mezzanine and equity positions.
6. Compare tranche pricing only after the structural path to repayment is clear.

---

## Core CLO Pool Considerations

### CLO Structure Overview
A CLO is a special purpose vehicle (SPV) that:
1. Purchases a diversified portfolio of leveraged loans ($400M-$600M typical)
2. Issues multiple tranches of debt (rated AAA through BB/B) and equity
3. Uses loan portfolio cash flows to pay CLO liabilities in order of seniority

### CLO Lifecycle
1. **Warehouse period** (3-6 months):
   - Manager accumulates loans using warehouse facility (bank credit line)
   - Typically 2-3x leverage on deployed capital
   - Manager bears mark-to-market risk
   - Warehouse funded via short-term credit; costs manager carry if spreads widen

2. **Pricing/closing**:
   - CLO tranches are priced and sold to investors
   - Warehouse facility is collapsed/replaced into CLO structure
   - Manager takes on CLO management fee (typically 0.40-0.50% of starting assets)

3. **Ramp-up period** (3-6 months post-close):
   - Manager deploys remaining cash and remaining warehouse proceeds
   - Portfolio reaches target size ($400M-$600M)
   - Manager still subject to OC tests and portfolio constraints from day one

4. **Reinvestment period** (typically 4-5 years):
   - Core period of active portfolio management
   - Manager can sell loans and reinvest proceeds in new loans
   - Subject to call protection (typically cannot call tranche B or below until after reinvestment period)
   - Repayments and prepayments are reinvested (or used to pay down CLO liabilities if in amortization)
   - Manager disciplines and replaces underperformers
   - Spread environment affects reinvestment spread and CLO equity returns

5. **Amortization period** (post-reinvestment, 2-3 years):
   - Principal repayments flow through to CLO noteholders in order of seniority
   - Limited reinvestment flexibility (only from credit-improved loans or credit-risk sales)
   - Focus shifts from growth to asset quality/recovery

6. **Maturity**:
   - CLO winds down; remaining assets liquidated
   - Proceeds distributed per waterfall (senior to junior)
   - Expected maturity typically 10-12 years post-close

### Portfolio Waterfall and Cash Flow Distribution

**CLO Cash Collections** → **CLO Expense Pool**
- Senior fees (trustee, servicer, rating agencies): ~$0.5-1.0M annually
- Management fee: ~0.40-0.50% of starting assets (~$1.6-3.0M annually for $400-600M CLO)
- Insurance/other: ~$0.2-0.3M

**Remaining Interest Income** → **Ordered Distribution**
1. Trustee expenses, senior debt service, management fees
2. AAA (Senior) interest
3. AA interest
4. A interest
5. BBB interest
6. BB interest
7. Equity (residual)

**Principal Recovery** → **Principal Waterfall** (OC-dependent)
1. Defaults/sales reduce par value, trigger OC diversion
2. If AAA OC test fails: all principal diverted to pay down AAA
3. If AA OC test fails (but AAA passes): divert to AA
4. And so on down the capital structure
5. Once all OC tests pass: principal flows to equity

### Coverage Tests — The Critical Constraints

**Overcollateralization (OC) Test**
- Formula: (Par Value of Loan Portfolio) / (Outstanding CLO Tranche Balance) ≥ Required OC Ratio
- Tested at each payment date (typically quarterly)
- Different OC test for each rated tranche:
  - **AAA OC test**: ~130% minimum (loans must be 130% of AAA notes outstanding)
  - **AA OC test**: ~120% minimum
  - **A OC test**: ~112% minimum
  - **BBB OC test**: ~108% minimum
  - **BB OC test**: ~104% minimum
- **If OC test fails**:
  - Cash diverted from equity/junior tranches to pay down most senior failing tranche until test is restored
  - Called an "OC haircut" or "OC diversion"
  - Can significantly reduce or eliminate equity distributions
  - For example, if AAA OC of 130% is required and actual is 125%, need 5% of AAA notes paid down immediately from cash flow
- **Par value adjustments**:
  - Defaulted loans valued at market value (typically recovery estimate, e.g., 50-70% of par)
  - CCC-rated loans above basket limit (typically 7.5% of portfolio) haircut to lower of market or 85% of par
  - Stressed loans may be discussed for haircut if manager judgment calls them impaired

**Interest Coverage (IC) Test**
- Formula: (Interest Income from Portfolio) / (Interest Due on CLO Tranche + Senior Expenses) ≥ Required IC Ratio
- Typical minimum: 120% for AAA, lower for junior tranches
- **If IC test fails**:
  - Interest diverted from equity/junior to deleverage senior tranches
  - Less common issue than OC failure
  - Occurs in weak interest rate/credit environments

### CLO Portfolio Constraints
CLO indentures contain numerous tests that limit portfolio composition:

**Single Obligor & Industry Limits**
- **Maximum single obligor**: Typically 2-3% of portfolio per borrower (prevents concentration risk)
- **Maximum industry concentration**: Typically 8-12% per industry under Moody's 33-industry classification
- **Issuer concentration tests**: May limit to top 10 issuers at certain percentage

**Portfolio Quality Metrics**
- **Weighted Average Rating Factor (WARF)**: Maximum ≤ 2800-3000
  - WARF measures credit quality via Moody's rating system (Aaa = 1, Aa = 10, A = 20... B3 = 2500, Caa = 3500)
  - Limit ~2800-3000 constrains portfolio to approximate B2 average

- **Weighted Average Spread (WAS)**: Minimum ≥ 3.25-3.50%
  - Ensures sufficient income to service all CLO liabilities + equity returns
  - Rising when spreads widen; falling when spreads compress
  - Direct impact on manager's ability to source investments

- **Weighted Average Life (WAL)**: Maximum ≤ 7-8 years
  - Limits extension risk; ensures maturity in reasonable timeframe
  - Floating-rate leverage loans typically 4-6 year WAL

**Credit Quality Baskets**
- **CCC basket**: Maximum 7.5% of portfolio at CCC+ or below
  - Excess CCC immediately haircuts OC test value to 85% of par (or market, if lower)
  - Acts as automatic brake on manager buying distressed paper

- **Second lien / unsecured limit**: Typically 0-10% of portfolio
  - Some CLOs allow junior capital structure; others restricted to first lien only

- **Covenant-lite limit**: Often no explicit limit (market norm is ~85-95% cov-lite)
  - Reflects reality of leveraged loan market evolution

**Diversity & Risk Concentration**
- **Moody's Diversity Score**: Minimum ≥ 20-25
  - Measures effective number of independent credits
  - Accounts for industry concentration and single obligor limits
  - Score of 50 = portfolio of 50 equal-weight credits; lower scores reflect concentration

### Deal Selection Criteria

**Structure & Subordination**
- **Subordination Levels**: Higher subordination = more cushion
  - BB subordination >10%: More cushion (positive for BB, negative for equity)
  - BB subordination 8-10%: Balanced
  - BB subordination <8%: Tight cushion (positive for equity upside, negative for downside)
- **Reinvestment Period Remaining**:
  - >4 years remaining: High value from manager optionality (can take advantage of spread cycles)
  - 3-4 years: Moderate optionality
  - <3 years: Limited optionality (portfolio becoming static)
  - Longer reinvestment = higher equity option value = higher expected return
- **Payment Frequency**: Most CLOs pay quarterly; some semi-annual (quarterly = higher reinvestment optionality)

**Weighted Average Price (WAP) of Portfolio**
- **WAP <100 (portfolio at discount)**:
  - Manager bought at discount
  - Upside: Par recovery → par build value
  - Example: WAP 98 → if all held to par, par build = $10M
- **WAP = 100 (portfolio at par)**:
  - Manager bought at par or mixed
  - No inherent par build opportunity (unless spreads tighten)
- **WAP >100 (portfolio at premium)**:
  - Manager bought at premium or current prices reflect mark-up
  - Risk: If spreads widen or defaults occur, mark-down likely
  - Downside: May not recover par; realized loss likely

**Reinvestment Period Analysis**
- **Manager Flexibility During Reinvestment**:
  - Can manager reinvest without restriction? Or limited to replacing defaults only?
  - Full reinvestment flexibility: Manager can buy new loans, sell underperformers (higher option value)
  - Restricted reinvestment: Manager limited to amortization reinvestment (lower option value)
- **Spread Environment During Reinvestment**:
  - **Tight spread environment** (low WAS available for reinvestment): Manager forced to buy lower-spread loans, arbitrage compresses, equity returns pressured
  - **Wide spread environment** (high WAS available for reinvestment): Manager can reinvest at high spreads, arbitrage improves, equity returns benefit
  - **Volatile spread environment** (spreads widen then tighten): Creates opportunity for trading gains (if manager has skill and flexibility)

**Call/Refinancing/Reset Analysis**
- **Call Option**: Equity holders (or manager-affiliated investor) have right to call CLO
  - Typical: Non-call protection for first 2 years (equity protected from call)
  - After reinvestment period ends (year 4-5), equity can call
  - Call is exercised when: Equity NAV > purchase price, OR arbitrage deteriorates significantly
  - Implication: If manager expects strong performance (NAV appreciation), call likely → equity gets good exit
- **Refinancing Opportunity**: If CLO liability spreads tighten (AAA spreads compress), manager can refinance cheaper debt
  - Refinancing benefits equity (reduces liability costs, improves arbitrage)
- **Reset Option**: Extend reinvestment period + refinance liabilities (hybrid call + refinance)
  - Creates "new" CLO inside existing structure
  - Beneficial if portfolio is strong and arbitrage re-widens (can extend upside)
  - Negative if portfolio is weak (extends downside risk)

---

## Secondary CLO Execution

Secondary CLO execution sits at the boundary between underwriting and trading. The key principle is that execution mechanics can materially alter realized return, especially for mezzanine and equity positions where liquidity is episodic and trustee-report timing matters.

### Identification And Documentation

- Confirm tranche identity through the deal name, class designation, and security identifiers.
- Tie the trade back to the current indenture, most recent trustee report, and any reset or refinancing history.
- Distinguish carefully between original balance, current balance, and the balance used for quoted price or accrued-interest calculations.

### Liquidity Principles

- Senior tranches generally trade more regularly than mezzanine or equity tranches.
- Liquidity is dealer-intermediated and can disappear quickly during credit stress.
- A position that is small relative to the overall market can still be large relative to the available float in a specific tranche.
- For illiquid paper, execution timing and counterparties can matter as much as model value.

### Execution Discipline

1. **Define the objective first**: Entry, exit, relative-value switch, or liquidity reduction.
2. **Match the process to the tranche**: Senior debt can support broader price discovery; mezzanine and equity often require more targeted inquiry.
3. **Avoid turning an underwriting view into a forced trade**: If a position is large relative to float, stage execution unless urgency overrides.
4. **Check the calendar**: Trustee reports, payment dates, new issue supply, resets, and call periods can all change fair value and dealer appetite.

### Settlement And Operations

- CLO trades usually settle more slowly than highly liquid public bonds.
- Accrued interest, record dates, and payment-date proximity can materially affect all-in economics.
- Cross-border custody, DTC or Euroclear eligibility, and operational readiness should be confirmed before committing to size.
- Delivery-versus-payment discipline matters because the market is OTC and counterparty exposure exists between trade and settlement.

### Post-Trade Monitoring

After execution, the investor still needs to underwrite the position:

- Read each trustee report and compare new test levels with the purchase thesis.
- Track changes in collateral quality, defaulted assets, and manager trading behavior.
- Re-underwrite call, reset, and refinancing optionality as the deal seasons.

### Main Risks

- **Liquidity risk**: The ability to exit may disappear before the model changes.
- **Settlement risk**: Slower settlement creates a window for operational failure or counterparty exposure.
- **Information timing risk**: Prices can move sharply around trustee reports, collateral events, or rating actions.
- **Technical risk**: New issue supply, BWIC flow, or dealer balance-sheet constraints can move spreads independently of fundamentals.

### Practical Routing

- Use this note for durable execution principles tied to CLO underwriting.
- Use `trading-pricing-mechanics` when the question is mainly about market color, RFQ tactics, or live trading conventions.
- Use `references/market-benchmarks.md` for current spread levels and bid-offer context instead of relying on stale point-in-time execution ranges.

---
