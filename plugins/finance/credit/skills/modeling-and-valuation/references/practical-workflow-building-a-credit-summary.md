---
last_updated: "2026-03-21"
---

## Practical Workflow: Building a Credit Summary

This is the step-by-step process to build a comprehensive credit analysis.

### Step 1: Obtain Latest Financials

- Annual 10-K (or audited financials): Full-year detailed statements
- Latest quarterly 10-Q (or management accounts): Current performance
- Press releases and investor presentations: Management guidance and commentary
- MD&A (Management Discussion & Analysis): Key commentary on results
- Footnotes: Critical for understanding accounting policies and one-time items

### Step 2: Calculate LTM (Last Twelve Months) EBITDA

LTM = trailing twelve months (most recent 4 quarters of actual results).

**Calculation:**
```
LTM EBITDA = Q1 EBITDA + Q2 EBITDA + Q3 EBITDA + Q4 EBITDA (most recent fiscal years/quarters)
```

**Why LTM?** It smooths seasonal variations and reflects current run-rate earnings.

**Example:**
- Most recent Q1 EBITDA: $24M
- Most recent Q2 EBITDA: $26M
- Most recent Q3 EBITDA: $25M
- Prior fiscal Q4 EBITDA: $23M
- LTM EBITDA = $98M

### Step 3: Identify and Evaluate Adjustments

For each adjustment to EBITDA:
1. Verify it's in company disclosure or reasonable estimate
2. Assess whether it's truly non-recurring
3. Determine if it's additive to cash generation
4. Note the dollar amount and whether it's included in covenant EBITDA

**Adjustment worksheet:**

| Item | Amount | Rationale | Covenant? |
|------|--------|-----------|-----------|
| Restructuring charges | $2.5M | Severance from facility closure (one-time) | Yes |
| Stock-based comp | $1.2M | Annual equity grants (recurring but non-cash) | Yes |
| Sponsor management fees | $0.8M | Advisory fees (LBO structure) | Yes |
| Litigation settlement | $0.5M | One-time legal matter (resolved) | Yes |
| Asset sale gain | ($0.3M) | Non-recurring, but non-operational | No |
| **Total Adjustments** | **$4.7M** | | |
| LTM Reported EBITDA | $98.0M | | |
| **LTM Adjusted EBITDA** | **$102.7M** | | |

### Step 4: Build FCF Waterfall

Create a detailed cash flow bridge from adjusted EBITDA to free cash flow.

**Waterfall example (annual basis):**

```
Adjusted EBITDA                              $102.7M

Cash Interest Paid
  Senior Secured Loan (7% on $250M)  $17.5M
  Senior Notes (8% on $200M)         $16.0M
  Sub Debt (12% on $100M)            $12.0M
  Less: PIK accrual (paid in debt)    ($2.0M)
  Total Cash Interest                         ($43.5M)

Cash Taxes Paid
  Effective tax rate ~25% on EBIT     (~11.0M)
  Less: Tax benefit from interest      +5.0M
  Total Cash Taxes                           ($6.0M)

CapEx
  Maintenance CapEx                   ($8.0M)
  Growth CapEx                        ($4.0M)
  Total CapEx                                ($12.0M)

Working Capital Change
  Receivables increase                ($2.0M)
  Inventory decrease                  +1.0M
  Payables increase                   +2.5M
  Other                               ($0.5M)
  Total WC Change                            (+$1.0M)

                                            _________
Free Cash Flow                              $42.2M
```

**Interpretation:**
- Company generates $42.2M of FCF after all cash outflows
- Available for debt paydown, acquisition, dividend, or cash accumulation
- At current debt service, FCF covers 35% of annual debt needs (good indicator of debt paydown capacity)

### Step 5: Calculate Key Ratios

Calculate metrics to assess credit quality. (See credit-ratio-analysis skill for detailed methodology, but key ratios include):

- **Leverage:** Net Debt / EBITDA
- **Interest Coverage:** EBITDA / Cash Interest
- **Debt Service Coverage:** FCF / (Cash Interest + Debt Repayment)
- **Liquidity:** Available Liquidity / Total Debt
- **EBITDA Margin:** EBITDA / Revenue
- **Leverage Trend:** Track over 4-8 quarters

### Step 6: Assess Liquidity Position

Summarize liquidity:

```
Available Liquidity
  Cash on hand                               $25.0M
  Revolver availability (committed - drawn) $75.0M
  Total Liquidity                          $100.0M

Obligations in Next 12 Months
  Quarterly interest payments                $10.9M
  Scheduled amortization                    $15.0M
  Revolver swingline (assume drawn)         $20.0M
  Capex obligations                         $5.0M
  Total 12-month obligations               ($50.9M)

Liquidity Cushion                           $49.1M

Plus: FCF Generation (next 12m)             $42.2M
Total Available Resources                   $91.3M
```

### Step 7: Compare to Prior Periods for Trends

Build a multi-year comparison:

| Metric | 2023A | 2024A | 2025E | Trend |
|--------|-------|-------|-------|-------|
| Revenue | $450M | $475M | $500M | Growing |
| Adj. EBITDA | $95.0M | $102.7M | $110.0M | Improving |
| EBITDA Margin | 21.1% | 21.6% | 22.0% | Stable/expanding |
| Net Debt | $425M | $432M | $420M | Modest growth then paydown |
| Net Leverage | 4.48x | 4.20x | 3.82x | Declining (good) |
| FCF | $28.0M | $42.2M | $50.0M | Strong improvement |
| Cash Interest | $40.0M | $43.5M | $43.5M | Stable (no incremental debt) |
| Int'l Coverage | 2.38x | 2.36x | 2.53x | Stable/improving |

**Analysis:** Company is deleveraging while growing EBITDA and improving FCF—positive trajectory. No near-term refinancing risk.

### Complete Credit Analysis Workflow

Use this workflow to conduct a systematic credit analysis:

#### Step 1: Gather Financials & Calculate Base Metrics

- Collect last 8 quarters of P&L, cash flow, balance sheet
- Calculate LTM (last twelve months) figures
- Calculate leverage, coverage, and cash flow ratios
- Compare to prior period (trend analysis)

#### Step 2: Enterprise Value & Valuation

- Determine market cap / equity value
- Calculate enterprise value
- Compare EV/EBITDA to peers and industry
- Assess valuation reasonableness

#### Step 3: Business Trend Analysis

- Review revenue trends (organic, segment, YoY, sequential)
- Analyze EBITDA margin trajectory
- Assess operating leverage
- Examine expense structure and CapEx
- Calculate working capital metrics
- Review management's guidance track record

#### Step 4: Peer Benchmarking

- Gather peer company metrics (ratios, margins, growth)
- Compare how target company stacks up
- Identify where credit is strong vs weak relative to peers

#### Step 5: Scenario Analysis & Stress Testing

- Base case: Company meets guidance, trends continue
- Upside case: Better growth, margin expansion
- Downside case: Revenue pressure, margin compression
  - Leverage goes to? Coverage goes to?
  - Would company breach covenants?

#### Step 6: Credit Rating Assignment

- Map leverage, coverage, and trends to rating scale (BB, B, CCC, etc.)
- Assess stability vs outlook (improving, stable, negative)
- Identify key risks and monitoring items

#### Step 7: Documentation & Monitoring

- Document key assumptions and conclusions
- Set monitoring schedule (quarterly, event-driven)
- Identify credit trigger points (covenant risk, maturity events, etc.)

#### Final Review Checklist

Before forming the credit opinion, verify that the work package includes:

- Latest annual and quarterly financials
- LTM EBITDA with each adjustment sourced and explained
- Free-cash-flow bridge from adjusted EBITDA to debt paydown capacity
- Key credit ratios: leverage, coverage, liquidity, and maturity profile
- Trend analysis over multiple periods rather than a single snapshot
- Covenant definitions and headroom, where applicable
- Business, sector, and competitive-position context
- Key risks, mitigants, and unresolved diligence items
- At least one downside scenario and a rate/refinancing stress
- Peer or valuation cross-checks where they matter to downside or relative value

---
