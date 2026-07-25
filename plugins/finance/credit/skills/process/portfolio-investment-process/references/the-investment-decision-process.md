---
last_updated: "2026-03-21"
---

## Part 5: The Investment Decision Process

### Overview: Seven-Step Framework

Making an investment decision (buy/sell/hold) requires systematically evaluating:

1. **Big-Picture Items** (macro context)
2. **The Company** (business quality)
3. **Credit Fundamentals** (financial capacity to pay)
4. **Event Analysis** (upcoming catalysts)
5. **Security Analysis** (the specific instrument)
6. **Relative Value & Return** (is this the best risk-adjusted opportunity?)
7. **The Decision** (buy/sell/hold, sizing, triggers)

### Step 1: Big-Picture Items

#### Market Context

Before evaluating an individual credit, understand the environment:

- **LBO wave**: Are sponsors doing lots of deals? (More leverage in the market)
- **IPO window**: Are companies going public? (Refinancing opportunity or exit pressure)
- **Supply/demand for HY paper**: Is the HY market flush with cash or starved for deals?
- **Relative attractiveness**: Are HY spreads attractive vs investment-grade or equities?
- **Technicals**: Are there fund flows driving or limiting demand?

**Use case**: If the HY market is in a "refinancing wave" with lots of new issuance, it's easier for a company to refinance debt. If the market is tight, refinancing risk rises.

#### Interest Rate Environment

- **Rising rates**: Higher refinancing rates; affects call features and FCF allocation to interest
- **Falling rates**: Companies may call debt and refinance cheaper; older bonds may be called
- **Volatility**: Uncertainty affects M&A and capital-raising activity

### Step 2: The Company

#### Business Model and Industry Dynamics

- **What does the company do?** (Recurring revenue vs transactional? High/low margin?)
- **How fragmented is the industry?** (Consolidated = less competitive pressure; fragmented = price pressure)
- **What are the secular trends?** (Growing, flat, or declining market?)
- **Competitive position**: Market share? Pricing power? Switching costs for customers?

#### Management Quality and Ownership Motivation

- **Is the CEO/CFO credible?** (Track record in this industry?)
- **Sponsor motivation**: If PE-owned, what's the timeline to exit? (Influences capital allocation)
- **Alignment**: Do managers have equity upside? (Aligned with debt holders)
- **History**: Has this management team successfully exited other companies?

**Example:**
- Company A: CEO with 15-year track record in telecom, founder-owned → Trustworthy
- Company B: New CEO from outside industry, PE-owned with 7-year fund life and company at year 3 → Exit pressure rising

### Step 3: Credit Fundamentals

This is the heart of credit analysis: **Can this company service its debt?**

#### Financial Metrics and Historical Changes

- **Leverage (Net Debt / EBITDA)**: Stable, rising, or falling? (Rising = deterioration)
- **Interest coverage (EBITDA / Interest)**: How much EBITDA cushion before interest is unpaid?
- **FCF / Debt**: Can the company generate enough cash to reduce debt?
- **Historical trends**: Are metrics improving or worsening quarter-to-quarter?

#### Sensitivity to Operational Declines

**Stress test your assumptions:**

- **If revenue declines 5%**: How much does EBITDA fall? (High-margin business = EBITDA falls faster than revenue)
- **If EBITDA margin declines 200 bps**: Does the company still cover interest?
- **If CapEx increases 20%**: Does FCF still cover debt service?

Example:
```
Base case: Revenue $710M, EBITDA margin 22%, Debt $500M, Interest $35M
- If revenue declines to $675M (-5%): EBITDA margin could compress to 20% = EBITDA $135M
- Interest coverage: $135M / $35M = 3.9x (still healthy, assuming no deleveraging)

Stress case: Revenue $640M (-10%), margin 18%, EBITDA $115M
- Interest coverage: $115M / $35M = 3.3x (still okay, but tighter)

- Severe stress: Revenue $570M (-20%), margin 15%, EBITDA $85M
- Interest coverage: $85M / $35M = 2.4x (below comfort level; potential covenant breach risk)
```

**Conclusion**: This company can withstand a 5-10% revenue decline, but a 20% revenue drop is risky.

#### Cash Flow and Liquidity

- **Operating CFO**: Is it positive? Trending?
- **CapEx**: What's required to maintain the business? Is it rising?
- **FCF after capex**: After paying for maintenance and growth, how much cash is left?
- **Debt maturity profile**: When is debt due? Can it be refinanced in current market?
- **Revolver headroom**: How much undrawn credit line is available?

#### Balance Sheet Review

- **Asset quality**: Are assets worth their stated value? (Intangible assets like goodwill can disappear)
- **Debt structure**: What's secured (collateral risk) vs unsecured (depends on company value)?
- **Off-balance-sheet items**: Operating leases (now capitalized under IFRS/ASC 842), pension obligations?

#### Structural Issues

- **Which entities support which debt?** (Only some entities may have collateral)
- **Guarantees**: Do subsidiary loans guarantee parent company debt?
- **Cross-default clauses**: If one debt tranche defaults, do all tranches?
- **Subordination**: Is debt senior (paid first in bankruptcy) or junior (paid last)?

Example:
- Parent Co issues $300M senior notes
- Parent Co guarantees subsidiary's $150M bank loan
- If subsidiary fails, bank can take subsidiary assets AND has guarantee from Parent
- If Parent fails, senior noteholders lose priority to the bank

#### Asset Values and Equity Cushion

- **Tangible asset value**: Real estate, inventory, equipment that has collateral value
- **Enterprise value vs net debt**: If the company were sold, would equity holders get anything?
- **Equity cushion calculation**: (TEV - Net Debt) / Net Debt

Example:
```
TEV = $2,500M (market cap $2,000M + debt $500M - cash $20M)
Net Debt = $480M
Equity Cushion = ($2,500M - $480M) / $480M = 4.2x (or 81%)
```

Bonds get paid before equity. If this company's asset value falls more than the equity cushion, bonds are impaired.

#### Overall Credit Quality and Default Risk

Synthesize everything above into a credit rating framework:

- **Investment-grade (BBB+ or better)**: Stable cash flow, low leverage, minimal event risk
- **High-yield (BB to B)**: Moderate leverage, sensitive to downturns, event risk present
- **Distressed (CCC or lower)**: High leverage, near-term refinancing risk, significant default probability

### Step 4: Event Analysis

The future matters more than the past. What events could change the credit picture?

#### Liquidity Events: Maturity and Refinancing

- **When is the next maturity?** (e.g., 24 months)
- **What's the refinancing profile?** (Is it a maturity wall or spread out?)
- **Likelihood of successful refinancing**: Market conditions + company quality
- **Impact if refinancing fails**: Would this trigger default?

Probability framework:
- **70% chance of refinancing successfully** → Bond price reflects mild event risk
- **30% chance of distressed refinancing** (wider spreads) → Bond price should be lower
- **10% chance of default** → Bond should be trading at steep discount

#### Maintenance Covenant Risk

- **Leverage ceiling**: How much cushion until breach?
- **Interest coverage test**: Similar analysis
- **Covenant step-downs**: Do tests get tighter over time?
- **Waiver probability**: If a breach seems likely, will lenders grant a waiver?

Example:
```
Leverage test: 3.0x ceiling, currently 3.1x (in breach)
Covenant waiver history: Lender granted waiver in 2022 when company breached
Probability of waiver: 70% (if lender wants company to succeed)
Impact if no waiver: Technical default, but not necessarily cash default
```

#### M&A Probability and Impact

- **Is the company a takeover target?** (Size, industry, strategically important?)
- **Likely buyer and synergies**: What would a buyer pay?
- **Impact on bonds**: Acquisition usually means refinancing (could be positive or negative)

**Three scenarios:**
1. **Strategic acquisition at premium (75% prob)**: Bonds get refinanced by larger acquirer (lower risk). Upgrade likely.
2. **Financial buyer / LBO (20% prob)**: Higher leverage to maximize returns. Bonds may worsen.
3. **No sale, company remains independent (5% prob)**: Status quo.

**Probability-weighted impact**: Most likely scenario is good for bonds, so the credit improves.

#### IPO or Deleveraging Event

- **Is an IPO in sponsor's plans?** (Timeline?)
- **Would IPO involve debt repayment?** (Uses of proceeds matter)
- **How much leverage would decline?** (From 4.0x to 2.5x?)

**Impact**: IPO usually means lower leverage and lower risk for bonds. But if IPO fails or is delayed, it could be a negative catalyst.

#### Dividend or Buyback Constraints

- **Is the company paying dividends?** (Capital leaving the company reduces equity cushion)
- **Buyback programs?** (Same effect)
- **Covenant restrictions?** (Leverage ceiling restricts dividends)

- **Probability of suspension**: If leverage rises or cash tightens, dividend/buyback gets cut first
- **Impact on bonds**: Preserving cash is good (lower leverage, better liquidity)

#### For Each Event: Probability, Impact, Timeframe

Create a simple matrix:

| Event | Probability | Timeframe | Impact (Base Case = 0) | Debt Impact |
|-------|-------------|-----------|--------|--|
| Refinancing | 70% success / 30% distressed | 24 mo | -50 bp (if distressed) | Spread widens |
| Covenant waiver | 80% | 12 mo | 0 bp (business as usual) | No change |
| Strategic acquisition | 20% | 18-24 mo | +75 bp (upgrade) | Spread tightens |
| IPO | 30% | 18-36 mo | +100 bp (deleveraging) | Spread tightens |
| Dividend cut | 40% | 6-12 mo | +25 bp (preserves cash) | Slight tightening |

**Probability-weighted expected impact:**
```
(70% × -50bp) + (30% × -200bp = distressed scenario) = -35bp to -110bp
```

If base case spreads are 300 bp, and events could worsen them by 110 bp, the range is 300-410 bp.

### Step 5: Security Analysis

You're analyzing an individual debt instrument, not the company. Specific factors matter:

#### Primary Instrument Being Examined

- **What tranche?** (Sr Notes, Sub Notes, Bank Loan, etc.)
- **Seniority**: 1st lien (secured) vs unsecured vs subordinated
- **Subordination**: Does this instrument have to wait in line?

#### Structural Ranking and Key Covenants

1. **Seniority waterfall**: In a bankruptcy, who gets paid first?
   - Cash collateral accounts (secured creditors first)
   - 1st lien debt (secured by assets)
   - Unsecured debt
   - Subordinated debt (paid last)

2. **Key covenants for this security**:
   - Maintenance tests (if any): Do we have headroom?
   - Incurrence tests: What restrictions apply to new debt, dividends, asset sales?
   - Call features: When can this debt be refinanced?
   - Make-whole provisions: Is there a penalty for early repayment?

#### Technical Factors

1. **Issue size**: Larger issues are more liquid (easier to buy/sell)
   - $200M issue: Liquid, tight spreads
   - $50M issue: Less liquid, wider bid-ask spreads

2. **Public vs private registration**:
   - Public bonds (traded on exchange): More transparency, more investors, tighter spreads
   - Private placement: Fewer investors, harder to exit, wider spreads

3. **Liquidity**: How easy is it to exit? (Affects required return)

#### Capital Structure Changes

- **Will other tranches be issued?** (Dilutes this security's seniority)
- **Refinancing plans**: Will this tranche be refinanced out?
- **Asset sales**: Could collateral be stripped away?

### Step 6: Relative Value & Return

#### Financial and Operating Metrics vs Comparables

Build your relative value sheet (see Part 2). Specifically:

- **Is this credit's leverage higher or lower than peers?** (If higher, should get more spread)
- **Is growth better or worse?** (Better growth = justify lower spread)
- **Is profitability (margin) better or worse?** (Better margins = justify lower spread)

Example:
```
This Company: 3.5x Net Debt/EBITDA, 4% revenue growth, 20% EBITDA margin, STW 310 bp
Peer Average: 3.2x leverage, 4% growth, 21% margin, STW 290 bp

Conclusion: This company is ~0.3x MORE levered and has worse margin.
It should trade AT LEAST at peer spreads (290 bp) or WIDER (310+ bp preferred).
At 310 bp, this company is fairly valued (small premium for extra leverage).
```

#### Pricing vs Comparables and Indices

1. **Absolute spread**: Is 310 bp tight or wide in absolute terms?
   - HY index average: 400 bp? (This bond is tight, lower yield)
   - HY index average: 250 bp? (This bond is wide, higher yield)

2. **Relative to peers**: Is this tighter or wider than similar companies?

3. **Duration and convexity**: How much will bond price change if spreads move?
   - 4-year duration: 4% price change per 100 bp spread move
   - 8-year duration: 8% price change per 100 bp spread move

#### Expected Return

Simple calculation:
```
Current yield: 5.0% (coupon 4.5% + spread 0.5%)
Expected holding period: 2 years
Expected price change: Spreads tighten 50 bp (bond appreciates ~2%)
Expected return: 5.0% + 2.0% = 7.0% annually

Alternative: Spreads widen 100 bp (bond depreciates ~4%)
Expected return: 5.0% - 4.0% = 1.0% annually

Risk/reward: 7% upside, 1% downside = asymmetric if you believe in thesis
```

**Especially important if event risk is high**: If there's a 30% chance of a negative event with -200 bp impact, factor that into expected return:

```
30% × 1.0% (distressed scenario) + 70% × 7.0% (base case) = 5.2% expected return

Is 5.2% enough to compensate for event risk? Depends on alternatives.
```

### Step 7: The Decision

#### Does This Security Fit Your Investment Strategy and Pool?

- **Strategy constraints**: Are you mandated to hold only Investment-Grade? Or can you hold High-Yield?
- **Pool constraints**: Do you already have too much exposure to this industry, company, or even security type?
- **Sizing**: What's an appropriate position size? (e.g., 1-2% of portfolio for illiquid credits)

#### Risk/Reward Assessment

**Ask:**
- **Downside risk**: How much could I lose in a pessimistic scenario? (e.g., -15% if spreads widen?)
- **Upside potential**: How much could I gain if the thesis works? (e.g., +8% from refinancing?)
- **Base case**: What's most likely? (e.g., +4.5% annual return, no surprises)

**Decision framework:**
- If **risk/reward is 1:2 or better** (e.g., $1 downside risk for $2 upside): **BUY**
- If **risk/reward is 1:1** (e.g., $1 downside, $1 upside): **Questionable**; need strong conviction
- If **downside > upside**: **SELL or PASS**

#### Buy, Sell, or Hold Decision

**BUY if:**
- Fundamental credit quality supports the yield
- Relative value is attractive vs peers and index
- Event risk is pricing into the spread (or non-existent)
- Risk/reward is favorable
- Security fits your strategy and portfolio

**SELL if:**
- Fundamental credit quality has deteriorated
- Relative value has tightened (bond is expensive relative to risk)
- Event risk is uncompensated (e.g., high maturity risk, spread too tight)
- Risk/reward has turned negative
- Can redeploy proceeds to better opportunity

**HOLD if:**
- Fundamental credit quality is stable
- Relative value is fair (not too tight, not too wide)
- No new information suggests change
- No better alternatives available
- Position is appropriate for strategy

#### Position Sizing

Conservative approach:
- **Core holdings (high confidence)**: 2-3% of portfolio
- **Tactical positions (event-driven)**: 1-2% of portfolio
- **Speculative / event risk**: 0.5-1% of portfolio

**Concentrations to monitor:**
- **Single issuer**: If one company grows to > 5% of portfolio, it's a concentrated bet
- **Industry**: If one industry is > 20% of portfolio, you have sector concentration
- **Maturity**: If bonds maturing in next 12 months are > 25%, refinancing risk is significant

#### Review Triggers

Establish upfront **when you'll revisit** this decision:

**Timeframe triggers:**
- "Review quarterly with earnings"
- "Review in 6 months or if maturity approaches"

**Event-based triggers:**
- "Review if covenant test is about to fail"
- "Review if management changes"
- "Review if company announces M&A"

**Price-based triggers:**
- "Review if spread widens > 50 bp (new information?)"
- "Review if equity drops > 15% (distress signal?)"
- "Review if bond appreciates > 3 points (consider selling into strength)"

#### Alternative Expressions of the View

Sometimes the bond itself isn't the best way to express your investment thesis:

1. **If you're bullish on the company**:
   - Buy the bond (get yield + upside if spreads tighten)
   - OR buy a subordinated tranche (higher yield, more upside)
   - OR buy the equity (maximum upside, but more downside)

2. **If you're worried about default risk**:
   - Buy senior secured debt (priority if liquidated)
   - OR buy bond + CDS (hedge default risk explicitly)
   - OR stay away entirely

3. **If you want to express relative value**:
   - Buy the wide bond, short/sell the tight bond in the same issuer
   - OR buy high-yield, short investment-grade (express steepness view)

4. **If there's event risk (M&A, IPO, refinancing)**:
   - Buy the bond as a carry trade (hold until event resolves)
   - OR buy put options on the bond (hedge downside)
   - OR use total return swaps (change exposure without owning bond)

---
