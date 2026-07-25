---
last_updated: "2026-03-21"
---

## Discounted Cash Flow (DCF) Analysis

The only intrinsic valuation method not anchored to market multiples. Values a company based on present value of its projected future free cash flows.

### Core Concept

DCF = Sum of PV of projected cash flows + PV of terminal value

Provides an independent valuation view; can highlight if market is overvalued/undervalued versus intrinsic value.

### Why Valuation Matters for Credit

- **Equity cushion**: Enterprise Value - Debt = Equity Value. Larger equity cushion = more protection for bondholders.
- **TEV/Debt coverage**: If TEV declines below total debt, bonds trade below par and recovery risk rises.
- **Acquisition financing**: When a company is acquired, purchase price determines leverage; valuation drives the sources & uses.
- **Refinancing capacity**: A company's ability to refinance depends on how the market values its enterprise relative to its debt load.
- **Distressed analysis**: In bankruptcy, enterprise value determines what each creditor class recovers.

### Step 1: Project Unlevered Free Cash Flow (UFCF)

Typically project 5-10 years of explicit cash flows; terminal value captures remaining value.

**UFCF Waterfall:**
```
Revenue
x EBITDA Margin %
= EBITDA

- D&A
= EBIT (Operating Income)

x (1 - Tax Rate)
= NOPAT (Net Operating Profit After Tax)
  Alternative: EBIT x (1 - Tax) = EBIT(1-T)

+ D&A (add back: non-cash)
- CapEx (cash outflow for investments)
- Change in NWC (increase in Net Working Capital; subtract if building cash needs)
= Unlevered Free Cash Flow (UFCF)
```

**Why "Unlevered"?**
- Removes impact of capital structure (debt vs. equity mix)
- Allows you to value enterprise independent of financing
- Debt & interest expense are handled separately in WACC and EV-to-equity bridge

**UFCF vs. Levered FCF:**

| Metric | UFCF | Levered FCF |
|---|---|---|
| Starting point | EBIT after tax | EBITDA |
| Interest expense | Excluded (capital-structure neutral) | Included (cash interest deducted) |
| Tax shield | NOT included (applied via WACC) | Implicitly included |
| Use | DCF valuation (enterprise value) | Credit analysis (debt service capacity) |

**For credit analysis**: Use Levered FCF for debt service and covenant testing. Use UFCF for enterprise valuation and equity cushion analysis.

**Key Assumptions to Project:**

1. **Revenue Growth**: Historical trends, management guidance, industry comps, market research
   - Years 1-3: Often management's explicit guidance
   - Years 4-5: "Fading growth" toward long-term sustainable rate
   - Terminal: 2-3% perpetual growth (near GDP growth)

2. **EBITDA Margin**:
   - Start from historical/LTM margin
   - Adjust for: operating leverage, scale benefits, one-time costs, competitive dynamics
   - Converge toward long-term normalized margin by year 5

3. **D&A**:
   - Normalize as % of revenue or fixed dollar (if new CapEx is material, D&A may step up)
   - For acquisitions: include purchase accounting amortization (finite-life goodwill/intangibles)

4. **Tax Rate**:
   - Use marginal corporate tax rate (not effective rate)
   - For US corporations: ~21% (post-2017 Tax Cuts and Jobs Act), plus state taxes (~2-8%)
   - Total effective: ~23-28% typical

5. **CapEx**:
   - Normalize as % of revenue (maintenance CapEx) or absolute dollars
   - For growing companies: may be 3-5% of revenue
   - For mature companies: 2-3% of revenue (maintenance level)
   - For declining businesses: lower or negative (harvest)

6. **Working Capital**:
   - Days Sales Outstanding (DSO), Days Inventory Outstanding (DIO), Days Payable Outstanding (DPO)
   - Change in NWC = (NWC Year 2 - NWC Year 1)
   - Subtract from FCF; positive number means cash tied up in working capital

**Example 5-Year Projection:**
```
Year:                         LTM    Y1     Y2     Y3     Y4     Y5
Revenue ($M)                  $1,000 $1,050 $1,121 $1,194 $1,252 $1,304
Growth %                              5.0%  6.8%  6.5%  4.8%  4.2%
EBITDA Margin %               25.0%  25.0% 25.5%  26.0%  26.5%  27.0%
EBITDA ($M)                   $250   $263  $286   $310   $332   $352

D&A ($M)                      $80    $82   $84    $85    $87    $88
EBIT ($M)                     $170   $181  $202   $225   $245   $264
Tax Rate                      25%    25%   25%    25%    25%    25%
Taxes on EBIT ($M)            $43    $45   $51    $56    $61    $66
NOPAT ($M)                    $127   $136  $151   $169   $184   $198

+ D&A ($M)                    $80    $82   $84    $85    $87    $88
- CapEx ($M) [3% of Rev]      $30    $32   $34    $36    $38    $39
- Change in NWC ($M)           $10    $5    $8     $4     $3     $2
= UFCF ($M)                   $167   $181  $193   $214   $230   $245
```

### Step 2: Calculate WACC (Weighted Average Cost of Capital)

WACC is the discount rate--the required return to compensate for both debt and equity investors.

**WACC Formula:**
```
WACC = (E / V) x Cost of Equity + (D / V) x Cost of Debt x (1 - Tax Rate)

Where:
  E = Market Value of Equity
  D = Market Value of Debt
  V = E + D = Total Enterprise Value
  Tax Rate = Marginal tax rate (not effective)
```

**Credit analyst note**: Higher leverage raises levered beta, which raises cost of equity, which raises WACC, which lowers enterprise value, which thins the equity cushion. This circular relationship means over-leveraged companies face compounding valuation pressure.

**Step A: Estimate Cost of Equity (CAPM)**

```
Cost of Equity = Risk-Free Rate + Beta x Equity Risk Premium + Size Premium

Risk-Free Rate (Rf):
  - Use long-term Treasury yield matching projection horizon
  - 10-year Treasury for DCF (typical for M&A): See `references/market-benchmarks.md` for current Treasury yields
  - Can use 20-year if projections extend 10+ years

Beta -- Measure of stock's systematic risk:
  - Raw Beta: Regression of stock returns vs. market returns (2-year weekly data, Bloomberg, Yahoo Finance)
    - Beta = 1.0: Stock moves in line with market
    - Beta > 1.0: Stock is more volatile (risky)
    - Beta < 1.0: Stock is less volatile (defensive)

  - Adjusted Beta (Bloomberg adjustment): (2/3 x Raw Beta) + (1/3 x 1.0)
    - Acknowledges beta tends toward 1.0 over time

  - Unlevered Beta (Asset Beta) -- removes capital structure effect:
    Beta_U = Beta_L / [1 + (1 - Tax Rate) x (D / E)]

    Use unlevered beta from comps, then relever to target's capital structure:
    Beta_L = Beta_U x [1 + (1 - Tax Rate) x (D_Target / E_Target)]

Equity Risk Premium (ERP):
  - Long-term average excess return of stocks over Treasuries
  - Historical: ~5.5-6.5% (Ibbotson, Duff & Phelps surveys)
  - Use consensus: 5.0-6.0% typical in practice

  Calculation using Dividend Growth Model:
    ERP = (Dividend Yield + Expected Growth) - Risk-Free Rate
    Example (illustrative): S&P 500 at 1.5% yield, 5% growth, Rf = 4.5%
    ERP = (1.5% + 5%) - 4.5% = 2.0% (lower than surveys; surveys more common)
    Note: Use current Treasury yields from `references/market-benchmarks.md`

Size Premium:
  - Adjustment for small-cap companies (typically $2B-$10B market cap)
  - 1-3% additional premium (per Duff & Phelps, Morningstar)
  - Larger companies (>$10B): typically no size premium
  - Example: Small-cap cost of equity = Rf + Beta x ERP + 2% (size)

Example Cost of Equity Calculation:
  Rf = [Current risk-free rate -- see `references/market-benchmarks.md`]
  Unlevered Beta (from comps) = 1.0
  For stable capital structure (1.0x D/E):
  Beta_L = 1.0 x [1 + 0.75 x 1.0] = 1.75
  Cost of Equity = [Rf] + 1.75 x 6.0% = [Rf] + 10.5% (using Rf from `references/market-benchmarks.md`)
```

**Beta Mechanics for Credit Analysts:**
```
Step 1: Obtain raw betas for comparable companies
Step 2: Unlever each beta: Beta_U = Beta_L / [1 + (1-t)(D/E)]
Step 3: Calculate median unlevered beta across comps
Step 4: Relever to target capital structure: Beta_L = Beta_U x [1 + (1-t)(D/E)]
```

**Step B: Estimate Cost of Debt**

```
Cost of Debt = Yield to Maturity (YTM) of company's existing or comparable debt

Use market-based rate, not coupon rate (coupon is historical; YTM is forward-looking)

For company with no public debt, estimate using:
  - Comparable company credit spreads
  - Credit rating -> spread lookup
    - Investment grade (A/BBB): 2-4% spread over Rf
    - Speculative (BB): 4-6% spread
    - High yield (B/CCC): 6-10%+ spread

  Example: If Rf = [current risk-free rate from `references/market-benchmarks.md`], and comp has 4% spread (BB-rated)
  Cost of Debt = [Rf] + 4.0% (using Rf from `references/market-benchmarks.md`)

After-Tax Cost of Debt:
  Cost of Debt x (1 - Tax Rate)
  Example: 8.5% x (1 - 0.25) = 8.5% x 0.75 = 6.375%

  (Tax shield: interest is deductible, so cost to equity holders is reduced by tax benefit)
```

**Step C: Calculate WACC**

```
Target Capital Structure Assumptions:
  - E / V = 60% (equity weight)
  - D / V = 40% (debt weight)

  Cost of Equity = 12.0%
  Cost of Debt (after-tax) = 6.4%

  WACC = 0.60 x 12.0% + 0.40 x 6.4%
       = 7.2% + 2.56%
       = 9.76% ~ 10.0%
```

**Typical WACC Ranges:**
- Investment-grade industrial: 6-8%
- Investment-grade tech: 7-9%
- High-yield (BB-rated): 8-12%
- Leveraged (B-rated): 10-14%
- Highly leveraged/distressed: 12-18%+

### Step 3: Calculate Terminal Value

Terminal value (TV) is the estimated value of the business at the end of the explicit projection period. It typically represents 60-80% of total DCF value.

**Credit analyst reality check**: Terminal value is typically 60-80% of enterprise value. This means the equity cushion protecting your bonds is heavily dependent on long-term assumptions. In distressed situations, challenge the terminal value aggressively.

**Method 1: Exit Multiple (More Common in Practice)**

```
Terminal Value = Terminal Year EBITDA x Exit Multiple

Logic:
  - At end of Year 5, company is mature
  - Should revert to steady-state market multiples
  - Conservative: use current market EV/EBITDA (don't assume expansion)
  - Moderate: assume slight contraction from current levels
  - Optimistic: assume expansion (requires strong reasoning)

Example:
  Year 5 EBITDA = $352M
  Exit Multiple = 8.0x (assume stable market multiples)
  Terminal Value = $352M x 8.0x = $2,816M
```

**Method 2: Perpetuity Growth (Theoretical but Used in Practice)**

```
Terminal Value = Terminal Year UFCF x (1 + g) / (WACC - g)

Where:
  g = Long-term perpetual growth rate (typically 2-3%, near GDP growth)
  WACC = Discount rate

Constraint: g must be < WACC (otherwise formula breaks down)

Example:
  Year 5 UFCF = $245M
  Long-term growth = 2.5%
  WACC = 10.0%

  TV = $245M x (1.025) / (0.10 - 0.025)
     = $245M x 1.025 / 0.075
     = $251.1M / 0.075
     = $3,348M
```

**Cross-Check Both Methods:**
The two methods should yield similar results (within 10-15%). If they diverge significantly, investigate assumptions.

### Step 4: Calculate Enterprise Value and Present Value

```
DCF Enterprise Value = Sum [UFCF Year 1-5 / (1 + WACC)^n] + [TV / (1 + WACC)^5]

Where n = year number (1-5)

Example Calculation:
Year 1: $181M / 1.10^1 = $181M / 1.10 = $164.5M
Year 2: $193M / 1.10^2 = $193M / 1.21 = $159.5M
Year 3: $214M / 1.10^3 = $214M / 1.331 = $160.8M
Year 4: $230M / 1.10^4 = $230M / 1.464 = $157.1M
Year 5: $245M / 1.10^5 = $245M / 1.611 = $152.1M
Subtotal FCF PV:                               $794.0M

Terminal Value: $2,816M / 1.10^5 = $2,816M / 1.611 = $1,748.4M

Enterprise Value = $794.0M + $1,748.4M = $2,542.4M
```

### Step 5: Enterprise Value to Equity Value Bridge

DCF gives you enterprise value; need to bridge to equity value (what equityholders receive).

```
Enterprise Value (from DCF)        $2,542M
  - Total Debt                       ($500M)
  - Preferred Stock                  ($0M)
  - Minority Interest                ($0M)
  + Cash & Cash Equivalents          $100M
  + Non-Operating Assets            $0M
  -----------------------------------------
Equity Value                        $2,142M

Equity Value / Diluted Shares Outstanding = Implied Price per Share
$2,142M / 101M shares = $21.20 per share
```

### Enterprise Value Bridge -- From EV to Equity Cushion

For credit analysts, the EV bridge frames recovery and debt protection:

```
Enterprise Value (from DCF, comps, or market)
  - Senior Secured Debt (first lien loans)
  - Senior Unsecured Debt (bonds)
  - Subordinated Debt
  - Preferred Stock
  - Minority Interest
  + Cash & Equivalents
  = Equity Value (Equity Cushion)

Equity Cushion % = Equity Value / Enterprise Value
  Example: $2,000M EV - $1,200M total debt + $100M cash = $900M equity
  Equity Cushion = $900M / $2,000M = 45%
```

**Equity Cushion Benchmarks:**
- >40% equity cushion: Comfortable for senior secured
- 25-40%: Adequate for senior unsecured
- 15-25%: Thin; senior unsecured at risk in downturn
- <15%: Stressed; subordinated debt impaired

### Step 6: Sensitivity Analysis

Always present DCF as a range; sensitivity tables show how valuation changes with key assumption changes.

**WACC Sensitivity (+/-1-2%):**
```
              WACC = 8%    9%     10%    11%    12%
Exit Multiple 8.0x  $2,800M $2,542M $2,320M $2,140M $1,990M
Exit Multiple 8.5x  $2,910M $2,630M $2,390M $2,210M $2,060M
Exit Multiple 9.0x  $3,020M $2,720M $2,460M $2,280M $2,130M
```

**Terminal Growth Rate Sensitivity (+/-0.5-1.0%):**
```
                    g = 1.5%  2.0%   2.5%   3.0%   3.5%
WACC = 9% (1.5% gap) $2,100M $2,310M $2,630M $3,090M  [exceeds WACC, invalid]
WACC = 10% (2.5% gap) $2,300M $2,440M $2,630M $2,890M  [exceeds WACC, invalid]
```

**Revenue Growth Sensitivity:**
Show how varying revenue CAGR affects enterprise value. This highlights operating risk.

### How EV Decline Affects Credit

```
                    EV Decline:    0%     -10%    -20%    -30%    -40%
                    =========     =====   =====   =====   =====   =====
Enterprise Value               $2,000  $1,800  $1,600  $1,400  $1,200
Total Debt                     $1,200  $1,200  $1,200  $1,200  $1,200
Equity Cushion                   $800    $600    $400    $200      $0
Equity Cushion %                  40%     33%     25%     14%      0%
Sr Secured ($600M) Recovery      100%    100%    100%    100%    100%
Sr Unsecured ($400M) Recovery    100%    100%    100%    100%     100%
Sub Debt ($200M) Recovery        100%    100%    100%    100%      0%
```

This table is the core credit analysis output: it shows at what EV decline level each tranche becomes impaired.

---
