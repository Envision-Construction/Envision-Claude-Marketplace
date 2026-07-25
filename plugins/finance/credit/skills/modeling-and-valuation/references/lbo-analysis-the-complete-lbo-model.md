---
last_updated: "2026-03-21"
---

## Part 4: LBO Analysis — The Complete LBO Model

The leveraged buyout model determines: (1) the maximum price a PE firm can pay, and (2) what returns (IRR/MOIC) they'll achieve at that price.

### LBO Concept Overview

1. **Acquisition**: PE firm (sponsor) buys target company, financed with significant debt (50–70%) and equity (30–50%)
2. **Hold Period**: 3–7 years; cash flows used to service and pay down debt
3. **Exit**: Company sold; remaining debt repaid; remaining value goes to equity
4. **Returns**: Measured as IRR (annualized return) and MOIC (multiple on invested capital)

**Return Targets:**
- Sponsor return hurdles vary by market regime, asset quality, and fund mandate
- Use `references/typical-deal-parameters.md` for current convention ranges and calibrate to the specific sponsor situation
- Treat the LBO as a sensitivity framework, not a single "correct" buyer return target

### Step 1: Sources & Uses of Funds

Shows where acquisition capital comes from (sources) and where it's deployed (uses).

**Must balance: Total Sources = Total Uses**

**Common Sources (Debt + Equity):**
```
SOURCES OF FUNDS
════════════════════════════════════════
Revolving Credit Facility              $0M     (undrawn; available for working capital)
Term Loan A (TLA)                     $XXM     (senior, amortizing, 5–7 yr maturity)
Term Loan B (TLB)                     $XXM     (senior, lower amortization, 6–8 yr maturity)
Senior Unsecured Notes                $XXM     (investment grade or high yield)
Subordinated Notes / Mezzanine        $XXM     (subordinated to senior debt; often with PIK toggle)
Preferred Equity / Rollover Equity    $XXM     (target management rolling some equity in)
Sponsor Equity                        $XXM     (PE firm's equity check)
────────────────────────────────────────
Total Sources                         $XXXM
```

**Common Uses (Capital Deployment):**
```
USES OF FUNDS
════════════════════════════════════════
Equity Purchase Price                 $XXXM    (primary use: buying the business)
Repay Existing Debt                   $XXM     (if target has existing debt)
Transaction Fees (M&A advisory, legal)$XXM     (verify against deal context)
Financing Fees (debt arranging)       $XXM     (verify against debt structure)
Working Capital Adjustment            $XXM     (if any)
────────────────────────────────────────
Total Uses                            $XXXM
```

**Determining Entry Price:**

```
Starting Point: Market Opinion of Value (MOOV)
  = Target EBITDA × Entry Multiple

Entry Multiple drivers:
  • Comps analysis (trading multiples): range depends on sector, cycle, and quality
  • Precedent transactions (deal comps): range depends on deal vintage and control premium
  • DCF: "Fair value"
  • Seller expectations and competitive dynamics

Example:
  Target LTM EBITDA = $200M
  Entry Multiple Range = 9.0x – 10.0x (based on market comps)

  Entry Enterprise Value = $200M × 9.5x = $1,900M
  Less: Target Net Debt = ($400M) [debt - cash]
  Equity Purchase Price = $1,500M
```

**Financing Structure & Debt Sizing:**

```
Debt / EBITDA Target = use current market and lender convention ranges from
`references/typical-deal-parameters.md`, then adjust for stability, cyclicality,
asset coverage, and documentation flexibility

Debt Mix:
  • Senior debt sizing depends on cash-flow durability and lender appetite
  • Junior debt or preferred capital depends on market depth and sponsor tolerance for cost

Pricing:
  • Use `references/market-benchmarks.md` for current base rates and spread context
  • Use `references/typical-deal-parameters.md` for convention ranges by instrument
  • Keep the model flexible enough to test tighter or wider financing cases
```

**Example Sources & Uses:**

```
Transaction: Acme Corp Acquisition
Target LTM EBITDA: $200M

ENTRY VALUATION
  Entry Multiple:           9.5x EBITDA
  Enterprise Value:         $1,900M
  Less: Net Debt:          ($400M)
  ────────────────
  Equity Value:            $1,500M

SOURCES & USES
──────────────────────────────────────────
SOURCES                                Uses
──────────────────────────────────────────
Revolver (undrawn)      $0M            Equity Purchase Price  $1,500M
TL-A (3.5x EBITDA)     $700M          Retire Existing Debt     $400M
TL-B (2.0x EBITDA)     $400M          Trans. Fees (~2%)         $40M
Senior Notes           $200M          Financing Fees (~3%)      $50M
Sub Notes (PIK)        $150M
Rollover Equity        $100M
Sponsor Equity         $350M
────────────────────────────────────  ────────────────────────
Total Sources        $1,900M          Total Uses             $1,990M

Sponsor equity plugged to balance uses, or recalibrate debt/rollover.
```

### Step 2: Operating Model (5-Year P&L and Balance Sheet)

Project income statement, cash flow, and key balance sheet items Year 1–5.

**Income Statement Projection:**

```
                        LTM       Y1      Y2      Y3      Y4      Y5
Revenue ($M)            $1,000   $1,100  $1,210  $1,331  $1,464  $1,610
Growth %                         10.0%   10.0%   10.0%    9.9%    9.9%
EBITDA Margin           20.0%    20.0%   20.5%   21.0%   21.5%   22.0%
EBITDA ($M)             $200     $220    $248    $280    $315    $354

D&A ($M)                $50      $52     $54     $56     $58     $60
EBIT ($M)               $150     $168    $194    $224    $257    $294

Interest Expense        $XXX     (from debt schedule, varies as debt paid down)
  Y1: $320M (high; max debt)
  Y5: $180M (low; debt significantly reduced)

EBT ($M)                $100     variable per year based on interest burn
Taxes (25%)             $25      variable
Net Income ($M)         $75      variable per year
```

**Key Cash Flow Items:**

```
Operating Cash Flow:
  EBITDA
  - Cash Interest Expense (from debt schedule)
  - Cash Tax Expense
  = Operating Cash Flow (before working capital and CapEx)

Free Cash Flow:
  EBITDA
  - Cash Interest
  - Cash Taxes
  - CapEx (~3% of revenue)
  ± Δ Working Capital
  = Free Cash Flow Available for Debt Paydown
```

### Step 3: Debt Schedule (Most Critical LBO Component)

The debt schedule models each debt tranche and tracks paydown over the holding period. Each tranche has different terms (rate, maturity, amortization, call period).

**Key Debt Terms:**

```
Revolver:
  • Size: working-capital buffer sized to volatility and seasonal need
  • Pricing: benchmark plus margin; calibrate from root references
  • Commitment Fee: 0.75–1.0% on undrawn portion
  • No amortization; repaid from operating cash flow as needed
  • Example: If drawn $0 in Year 1, only pay commitment fee

Term Loan A:
  • Size: depends on lender appetite, amortization tolerance, and covenant package
  • Pricing: benchmark plus margin; calibrate from root references
  • Amortization: ~1.0% per year (5% cumulative by year 5)
  • Maturity: 5–7 years (tightest covenant package)
  • Prepayment: Can pay early without penalty (after 1-year call period)

Term Loan B:
  • Size: depends on cash-flow durability, market depth, and refinanceability
  • Pricing: benchmark plus margin; calibrate from root references
  • Amortization: 0.25–0.50% per year (lower; more refinance risk)
  • Maturity: 6–8 years
  • Prepayment: 1–2% prepayment penalty for first few years, then free

Senior Notes:
  • Size: depends on unsecured market access and target maturity profile
  • Pricing: fixed coupon or spread over benchmark; calibrate from root references
  • Amortization: 0% (bullet maturity)
  • Maturity: 7–10 years
  • Refinance risk: Must re-finance at maturity

Subordinated Notes / Mezzanine:
  • Size: depends on total leverage tolerance and sponsor equity appetite
  • Pricing: cash coupon plus potential PIK features; calibrate from root references
  • Amortization: 0%
  • Maturity: 7–10 years
  • PIK: If sponsor cash-constrained, can "toggle" to pay-in-kind (no cash outlay, but balance increases)
  • Subordination: Junior to all senior debt
```

**Debt Schedule Build-Out (Simplified, Year 1):**

```
                          TL-A        TL-B        Sr Notes    Sub Notes
                          ────────────────────────────────────────────────
Opening Balance          $700M        $400M        $200M        $150M
+ PIK Accrual             $0M          $0M          $0M          $8M (at 5% PIK rate)
- Mandatory Amortization ($7M)         $1M          $0M          $0M
  [TL-A: 1% annual = $7M; TL-B: 0.25% = $1M; Sr/Sub: 0% (bullet)]
- Cash Flow Sweep         ($50M)       ($0M)        $0M          $0M
  [Apply excess FCF to senior-most debt first: TL-A takes priority]
────────────────────────────────────────────────────────────────────────
Closing Balance          $643M        $399M        $200M        $158M
  [If $60M of FCF available, reduce TL-A first, then TL-B, etc.]
```

**Interest Expense Calculation (Year 1):**

```
TL-A:
  Drawn: $700M
  Rate: benchmark + margin
  Interest: drawn balance × all-in rate

Revolver:
  Drawn: $0M
  Undrawn: $100M
  Commitment Fee: 0.75%
  Commitment Fee: $100M × 0.75% = $0.75M

TL-B:
  Drawn: $400M
  Rate: benchmark + margin
  Interest: drawn balance × all-in rate

Senior Notes:
  Drawn: $200M
  Fixed Coupon: model-specific assumption
  Interest: drawn balance × coupon

Sub Notes:
  Drawn: $150M
  Coupon: cash component + potential PIK component
  Cash Interest: drawn balance × cash coupon
  PIK Accrual: drawn balance × PIK component
  Total Interest Expense: cash interest + PIK accrual

Total Interest Expense (Year 1) = $54.6 + $0.75 + $33.2 + $10.0 + $15.0 = $113.55M
```

**Paydown Priority (Waterfall):**

1. Revolver must be drawn/repaid first for working capital
2. Mandatory amortization on TL-A, TL-B (required by loan terms)
3. Cash flow sweep on most senior debt (TL-A) up to sweep percentage (e.g., 50–100% of excess cash)
4. Optional prepayment on most expensive debt (Sub Notes, then TL-B) if excess liquidity

### Step 4: Returns Analysis

At exit (typically Year 5), calculate equity value and returns to sponsor.

**Exit Assumptions:**

```
Exit Multiple:
  • Conservative: 8.0x EBITDA (assume multiple compression)
  • Base case: 9.5x EBITDA (same as entry)
  • Optimistic: 10.5x EBITDA (assume expansion)

Exit Enterprise Value:
  Year 5 EBITDA × Exit Multiple
  Example: $354M × 9.5x = $3,363M

Less: Remaining Net Debt (from Year 5 debt schedule):
  Total Debt (after paydown)    = $800M
  Less: Cash (assumed at minimum) = ($50M)
  Net Debt                       = $750M

Exit Equity Value:
  $3,363M - $750M = $2,613M

Less: Remaining Preferred / Minority Interest
Plus: Dividends Recaps (if any cash taken during hold)
= Total Equity Proceeds
```

**IRR and MOIC Calculation:**

```
Entry Sponsor Equity (cash invested)         $350M      (Year 0)
Exit Equity Proceeds                        $2,613M     (Year 5)
Dividends taken during hold (if any)           $0M

MOIC (Multiple on Invested Capital):
  = Total Proceeds / Total Cash Invested
  = $2,613M / $350M
  = 7.5x

IRR (Internal Rate of Return):
  Solve for discount rate that makes:
  PV of outflows = PV of inflows

  $350M (Year 0) = $2,613M / (1 + IRR)^5

  (1 + IRR)^5 = $2,613M / $350M = 7.47
  1 + IRR = 7.47^(1/5) = 1.485
  IRR = 48.5%

  (Note: This 48.5% assumes $0 interim dividends; in practice, some cash
  may be extracted via dividends, refinancings, or special distributions)

Target Benchmarks:
  Use sponsor-specific and market-specific hurdles from `references/typical-deal-parameters.md`.

  This 48.5% IRR / 7.5x MOIC is intentionally illustrative and depends heavily
  on debt paydown, multiple expansion, and growth assumptions.
```

**Value Creation Bridge (Sources of Return):**

```
Entry Equity Value                          $350M

+ EBITDA Growth (Y1–Y5 EBITDA expansion)   $154M    [(354 - 200) × 9.5x entry multiple]
+ Multiple Expansion (if exit > entry)      $270M    [(10.5x - 9.5x) × Y5 $354M EBITDA]
+ Debt Paydown (debt reduction from CF)     $600M    [$1,500M - $900M remaining debt]
+ Non-Operating Gains (asset sales, etc.)    $0M
- Dividend Recaps (cash taken out)          ($100M)  [(if applicable)]
────────────────────────────────────────────────────
= Exit Equity Value                       $2,274M

(Note: This simplified bridge may not reconcile exactly; professional LBO models include
full waterfall and all financing components)
```

### Step 5: Sensitivity Tables (Critical for Presentation)

Always show returns as a range, not a point estimate.

**Entry Multiple vs. Exit Multiple (IRR Grid):**

```
                       Exit Multiple
                 8.0x      9.0x      10.0x    11.0x    12.0x
Entry 8.0x      ─────────────────────────────────────────────
               32%      38%       44%      50%      56%

Entry 9.0x     ──────────────────────────────────────────────
              27%       33%       39%      45%      50%

Entry 10.0x   ──────────────────────────────────────────────
             23%       28%       34%      40%      45%
```

**Leverage at Entry vs. Exit IRR:**

```
Entry Leverage    IRR (Base Case)
─────────────────────────────────
3.0x EBITDA         15%  (lower leverage = lower returns)
4.0x EBITDA         25%  (sweet spot)
5.0x EBITDA         35%  (high leverage = high returns, high risk)
6.0x EBITDA         45%+ (very high leverage = distress risk)
```

**EBITDA Growth vs. Exit IRR:**

```
                Exit Multiple
EBITDA CAGR    8.0x    9.5x    11.0x
─────────────────────────────────
 0% (flat)     18%     23%      28%
 3% growth     24%     30%      36%
 5% growth     28%     35%      41%
 8% growth     36%     43%      50%
```

---
