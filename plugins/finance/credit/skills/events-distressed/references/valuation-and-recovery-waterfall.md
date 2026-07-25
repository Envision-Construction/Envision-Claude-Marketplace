---
name: Valuation and Recovery Waterfall
description: |
  Enterprise valuation approaches for distressed companies, the recovery analysis waterfall from
  enterprise value through each claim class, and the present-value framework for discounting
  future recoveries to today's price.
last_updated: "2026-03-22"
---

## Valuing the Enterprise

### Step 1: Estimate Enterprise Value (Multiple Approaches)

**Comparable Company Multiples**:
- Distressed company likely worse than peers (why it's in bankruptcy)
- But still useful for benchmark
- "Distressed 4-turn EBITDA" vs. "healthy 7-turn EBITDA"
- Apply range of multiples to stressed EBITDA estimate
- Example: Company now generating $50M EBITDA (down from $80M historically), apply 5.0-5.5x multiple → $250-275M valuation

**Comparable Transactions**:
- Look at recent sales of similar companies
- Discount for size, market conditions, and distressed nature
- Example: Competitor sold for $280M on $55M EBITDA (5.1x), distressed company at $50M EBITDA @ 4.8x = $240M

**Discounted Cash Flow (DCF)**:
- Project 5-year cash flows post-bankruptcy
- Assume management makes improvements: cost cuts, revenue stabilization
- Terminal value at year 5 (or exit)
- Discount at appropriate cost of capital (12-15% for distressed, risky companies)
- Example: Project recovery to $70M EBITDA by year 5, 6x exit multiple, 13% discount rate → $280M present value

### Step 2: Include Non-Cash-Generating Assets

**Real Estate**:
- Owned facilities: separate valuation (appraisal)
- May have significant value independent of operations
- Sale-leaseback opportunity: converts equity to cash, but locks in ongoing rent

**Minority Stakes & Affiliates**:
- Company may own stakes in other companies
- Often valued separately (comparable company multiples or NAV)
- Can be sold separately for liquidity

**Cash on Balance Sheet**:
- Cash not needed for operations is available (after minimum operating balance)
- Example: $30M cash on balance sheet, $5M needed for operations → $25M available

**Inventory & Receivables**:
- Often liquidated at discounts (80-90% of book value)
- Can represent meaningful value in recovery

### Step 3: Adjustment for Operating Efficiency

**Key Insight**: Buyer may pay more if they can improve margins
- Example: Company currently 10% EBITDA margin, buyer thinks 15% margin achievable
- Same revenue base but 50% more EBITDA = significantly higher value to buyer
- Equity sponsors especially likely to pay premium for "bolt-on" improvements

**Sanity Check**:
- Compare estimated enterprise value to comparable companies (EV/Revenue, EV/EBITDA)
- Is valuation reasonable? Too high? Too low?
- Get multiple opinions: bankers, creditors committee, independent appraisers

---

## Recovery Analysis Waterfall

### Framework: From Enterprise Value to Creditor Recovery

**Step 1: Start with Enterprise Value**
- Total value available to distribute
- Example: $650M

**Step 2: Pay DIP Loan (Super-Priority, 100% in Cash)**
- Rank 1: Must be repaid in full
- Typically senior notes or new money at same priority as cash on hand
- Example: $40M DIP → remaining value = $650M - $40M = $610M

**Step 3: Senior Secured Lenders → New Senior Debt**
- Secured by collateral worth value
- Rank 2: Paid in full in new senior notes or cash
- New debt = amount of old debt (or less if haircut)
- Example: $350M senior bank debt → receives $350M in new senior notes, 100% recovery
- Remaining value = $610M - $350M = $260M

**Step 4: Fulcrum Security → Equity**
- **Fulcrum = Most Senior Impaired Class**
- This class is not paid in full but receives the next tranche of value
- Usually receives equity in reorganized company (ownership stake)
- Also receives new junior debt or warrants
- This class "controls" the reorganization (votes yes on plan, gets board seats, sets strategy)
- Example: $500M subordinated notes (impaired: not receiving full claim) = fulcrum
  - Receives 97% in equity + 3% in warrants
  - Value of equity = $200M (97% recovery)

**Step 5: Junior to Fulcrum → Token Equity**
- Subordinated claims getting nothing or minimal recovery
- Receive small equity stake or warrants to avoid cram-down fights
- Usually very dilutive (1-5% of equity)
- Covers: "You get something" vs. "You get nothing"
- Example: $320M 2nd subordinated notes
  - Receive 3% equity (token) + 2.5% in warrants
  - Value of equity = $6M (1.9% recovery)

### BlowUp Co Example

**Enterprise Value**: $650M

**Capital Structure**:
- DIP loan: $40M (new money, super-priority)
- Senior bank debt: $350M (secured)
- Senior subordinated notes: $500M (unsecured, impaired)
- Subordinated notes: $320M (unsecured, impaired)

**Recovery Waterfall**:

1. **DIP Loan**: $40M (paid in cash from liquidity) → 100% recovery
   - Remaining: $650M - $40M = $610M

2. **Senior Bank Debt**: $350M (new senior notes) → 100% recovery
   - Remaining: $610M - $350M = $260M

3. **Senior Sub Notes** (FULCRUM):
   - Claim: $500M, available value: $260M
   - Not paid in full → Impaired → Gets equity
   - Recovery: $260M / $500M = 52%
   - Structure: 97% equity + 3% warrants
   - Meaning: 97% of the $260M to equity (= ~$252M value)
   - Equity stake: Majority ownership

4. **Subordinated Notes**:
   - Claim: $320M, available value: $0M (all taken by fulcrum)
   - Not paid in full → Impaired → Gets minimal stake to avoid cram-down
   - Recovery: 0% in cash/debt, token 3% equity
   - Value of 3% equity: small portion of $260M total ($ TBD by equity valuation)
   - Holding: ~1-2% equity

**Total Equity Value Available**: $260M
- Senior sub notes (fulcrum): ~97% = $252M
- Subordinated notes: ~3% = $8M

---

## Present Value of Recovery

### Why Present Value Matters

**Problem**: Recovery occurs at end of bankruptcy process, not today
- Filing date: today
- Expected emergence: 18-24 months from now
- Creditor gets paid in future → must discount to today's value
- Investor willing to pay less today for future value

### Discount Rate

**Required IRR for Distressed Investing**:
- Depends on risk and time horizon
- Typical range: 15-30% IRR depending on asset class and seniority
- Senior secured: 12-18% IRR (lower risk, more secure)
- Subordinated/equity: 25-35% IRR (higher risk, need higher return)

### Calculation: Present Value of Recovery

**Formula**: PV = Recovery Value / (1 + IRR)^n
- Recovery Value = amount expected to receive
- IRR = discount rate (required return)
- n = years to recovery

**Example**: Subordinated notes investor
- Current market price: $30 per $100 face = $30M position (if $100M total claim)
- Expected recovery: $50M in 2 years (50% recovery at emergence)
- Required IRR: 20%
- PV = $50M / (1.20)^2 = $50M / 1.44 = $34.7M
- Fair value today: $34.7M
- If trading at $30M → **buying at discount, good opportunity**
- If trading at $40M → **selling at premium, not attractive**

### More Complex Structures

**Multi-year recovery with staged equity**:
- Year 1: Receive new debt
- Year 2: Equity released with vesting
- Year 3: Exit, equity converted to cash
- PV = (Debt value at year 1) / (1.20)^1 + (Equity value at year 3) / (1.20)^3
- Longer tail → deeper discount → lower present value

**Probability-weighted recovery**:
- Scenario 1 (60% probability): $50M recovery in 2 years
- Scenario 2 (40% probability): $30M recovery in 3 years
- Expected value = 0.60 x ($50M / 1.20^2) + 0.40 x ($30M / 1.20^3)
- Captures binary outcomes (success vs. liquidation)

---
