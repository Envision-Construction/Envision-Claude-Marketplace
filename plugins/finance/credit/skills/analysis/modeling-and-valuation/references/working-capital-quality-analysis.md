---
last_updated: "2026-03-22"
---

# Working Capital Quality Analysis

Framework for analyzing working capital trends as indicators of earnings quality, cash flow sustainability, and potential credit deterioration.

## Working Capital Components

| Metric | Formula | What It Measures |
|---|---|---|
| Days Sales Outstanding (DSO) | (Accounts Receivable / Revenue) x 365 | Speed of cash collection from customers |
| Days Inventory Outstanding (DIO) | (Inventory / COGS) x 365 | How long inventory sits before sale |
| Days Payable Outstanding (DPO) | (Accounts Payable / COGS) x 365 | How long the company takes to pay suppliers |
| Cash Conversion Cycle (CCC) | DSO + DIO - DPO | Total days to convert investment in inventory to cash |

**Shorter CCC = more efficient cash generation.** Negative CCC (e.g., Amazon, subscription businesses) means the company collects cash before paying suppliers — a significant credit positive.

### Typical CCC by Sector

| Sector | Typical CCC (days) | Key Driver |
|---|---|---|
| Software/SaaS | -30 to 0 | Prepaid subscriptions, minimal inventory |
| Retail (grocery) | -10 to 15 | Fast inventory turns, supplier payment terms |
| Healthcare Services | 40-70 | Insurance reimbursement delays |
| Industrials/Manufacturing | 50-90 | Raw materials + WIP + finished goods cycle |
| Aerospace/Defense | 80-150 | Long production cycles, government payment terms |
| Construction/Engineering | 60-120 | Project-based billing, retainage |

## Trend Analysis

### DSO Trends as Earnings Quality Indicator

Rising DSO (>10% increase YoY) without corresponding change in payment terms is a significant red flag:

| DSO Trend | Possible Cause | Credit Implication |
|---|---|---|
| Increasing >10% YoY | Channel stuffing, revenue recognition issues | Earnings may be overstated; future revenue risk |
| Increasing modestly (5-10%) | Customer credit deterioration, sales mix shift | Monitor closely; may indicate customer stress |
| Stable | Normal operations | Neutral |
| Decreasing | Improved collections, tighter credit terms | Positive for cash flow quality |

**Diagnostic**: Compare DSO trend to peer group. If subject company DSO is rising while peers are stable, the issue is company-specific, not industry-wide.

### Inventory Quality Assessment

| Inventory Signal | Interpretation | Action |
|---|---|---|
| DIO rising, revenue growing proportionally | Normal growth-related inventory build | Monitor |
| DIO rising, revenue flat/declining | Potential obsolescence, demand weakness | RED FLAG — model inventory write-down risk |
| Finished goods increasing as % of total inventory | Demand weakness, potential markdown risk | Investigate sales pipeline |
| Raw materials increasing as % of total inventory | Anticipatory purchasing or supply chain hedging | Assess whether justified by order book |
| Inventory reserve declining as % of gross inventory | Potentially aggressive reserve management | Compare to peers; may indicate earnings management |

### Payables Trend Analysis

| DPO Trend | Interpretation | Credit Implication |
|---|---|---|
| Stretching significantly (>10% increase) | Supplier pressure — company may be managing cash by delaying payments | Negative — suppliers may tighten terms or demand cash-on-delivery |
| Compressing (<10% decrease) | Suppliers demanding faster payment | Negative — potential supplier concern about creditworthiness |
| Stable | Normal supplier relationships | Neutral |

## Accruals Quality (Sloan Accrual Ratio)

The Sloan Accrual Ratio measures the proportion of earnings derived from accruals vs. cash:

**Sloan Accrual Ratio = (Net Income - Cash from Operations) / Average Total Assets**

| Ratio Range | Interpretation |
|---|---|
| < -5% | High cash quality — CFO exceeds net income (ideal for credit) |
| -5% to +5% | Normal accruals level |
| +5% to +10% | Elevated accruals — monitor for earnings quality concerns |
| > +10% | HIGH accruals — significant earnings quality red flag |

**Credit Relevance**: High accrual ratios suggest net income is not supported by cash generation. For credit analysis, cash flow is what services debt — accrual-heavy earnings provide a false sense of coverage.

## Seasonal vs. Secular Changes

### Distinguishing Normal Seasonality from Structural Deterioration

1. **Pull 12 quarters** of working capital components (DSO, DIO, DPO)
2. **Overlay same-quarter comparisons**: compare Quarter 1 across multiple years rather than Quarter 1 versus Quarter 4
3. **Calculate year-over-year change for each quarter**: If Q1 DSO is rising every year (not just Q1 vs. Q4), the trend is secular, not seasonal
4. **Normalize for revenue seasonality**: Use annualized revenue for quarterly DSO calculation to avoid seasonal distortion

### Common Seasonal Patterns

| Sector | Peak Working Capital | Trough Working Capital |
|---|---|---|
| Retail | Q3 (holiday inventory build) | Q1 (post-holiday liquidation) |
| Agriculture/Food | Q3-Q4 (harvest season) | Q1-Q2 |
| Construction | Q2-Q3 (building season) | Q4-Q1 |

## Working Capital as Cash Flow Swing Factor

In scenario analysis, working capital is often the most volatile component of free cash flow:

### Downturn Working Capital Stress

| Component | Normal Operations | Downturn Impact | Cash Flow Effect |
|---|---|---|---|
| Receivables | Collected per terms | Customers delay payment (DSO +15-30 days) | Cash USE |
| Inventory | Turns per demand | Accumulates as demand drops (DIO +20-40 days) | Cash USE |
| Payables | Paid per terms | Suppliers tighten terms (DPO -10-20 days) | Cash USE |
| **Net Effect** | | **All three move against the company simultaneously** | **Significant cash drain** |

### Quantifying the Swing

For a company with $1B revenue and normal CCC of 60 days:
- Normal working capital = ~$164M ($1B x 60/365)
- Downturn CCC stretches to 90 days: working capital = ~$247M
- **Cash consumed by working capital deterioration = $83M** — often equivalent to 1-2 quarters of EBITDA

This working capital "trap" is why companies with seemingly adequate EBITDA can face liquidity crises in downturns.

## Red Flags Checklist

- [ ] DSO increasing >10% YoY without change in payment terms or customer mix
- [ ] Receivables growing faster than revenue (>5% divergence over 2+ quarters)
- [ ] DPO stretching >10% (potential sign of supplier concern about creditworthiness)
- [ ] Inventory growing faster than COGS (>5% divergence over 2+ quarters)
- [ ] Sloan Accrual Ratio exceeding +10%
- [ ] Significant gap between net income and CFO driven by working capital changes
- [ ] Declining inventory reserves as percentage of gross inventory
- [ ] Finished goods inventory increasing as share of total inventory without revenue growth
- [ ] Cash conversion cycle deteriorating while peers remain stable
- [ ] Management not addressing working capital trends in earnings calls despite visible deterioration
