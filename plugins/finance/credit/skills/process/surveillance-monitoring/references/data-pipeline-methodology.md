---
last_updated: "2026-03-22"
---

# Data Pipeline Methodology

This reference defines how surveillance metrics should be sourced, calculated, validated, and governed. Use `references/data-pipeline-specification.md` for the current monitoring parameters, cadence targets, escalation cutoffs, and tolerance bands that may change over time.

---

## 1. Metric Methodology Standards

### EBITDA Variance

**Data source hierarchy**
- **Primary:** SEC filings (10-Q quarterly, 10-K annual), sourced within 5 business days of earnings release
- **Secondary:** Management reports (for private credits with information rights), monthly or quarterly depending on credit agreement
- **Supplementary:** Sell-side equity research estimates, consensus estimates (Bloomberg BEst)

**Measurement methodology**
- Calculate LTM EBITDA by summing the most recent four quarters
- Compare LTM EBITDA to the underwriting model projection for the corresponding period
- Variance = (Actual LTM EBITDA - Model LTM EBITDA) / Model LTM EBITDA
- Use the same add-back methodology as the original underwriting, as documented in the credit memo
- For quarterly snapshots, compare quarterly EBITDA to the corresponding quarter in the model rather than only relying on LTM to detect deterioration earlier

### Covenant Headroom

**Data source hierarchy**
- **Primary:** Compliance certificates from agent bank, received quarterly per credit agreement
- **Secondary:** Company financial statements with analyst-calculated covenant metrics
- **Verification:** Cross-check compliance certificate figures against independently calculated metrics from financial statements

**Measurement methodology**
- Extract actual covenant test levels from compliance certificates (e.g., Total Leverage Ratio, Interest Coverage Ratio, Fixed Charge Coverage Ratio)
- Compare actual levels to covenant thresholds in the credit agreement schedule, including step-downs and step-ups
- Headroom = (Actual Level - Covenant Threshold) / Covenant Threshold for maintenance covenants
- For leverage covenants, use (Covenant Max Leverage - Actual Leverage) / Covenant Max Leverage
- Track whether headroom is expanding, stable, or compressing over the trailing four quarters

### Liquidity Runway

**Data source hierarchy**
- **Primary:** Company cash flow statements from SEC filings or management reports
- **Secondary:** Revolver availability from agent bank reports, including drawn amount, letters of credit, and borrowing base availability
- **Supplementary:** Maturity schedules, mandatory amortization, and known capex commitments

**Measurement methodology**
- Liquidity = Cash on Hand + Undrawn Revolver Availability, net of LC usage and borrowing base constraints
- Monthly Cash Burn = LTM Operating Cash Flow / 12, adjusted for working capital seasonality
- Liquidity Runway (months) = Total Liquidity / Monthly Cash Burn
- For seasonal businesses, calculate the minimum liquidity point in the seasonal cycle rather than using an average
- Include upcoming maturities within 12 months as a liquidity demand

### CDS Spread / Loan Price

**Data source hierarchy**
- **Primary:** Bloomberg (BCDS for CDS, TRACE for bonds, LCD for loan prices)
- **Secondary:** Dealer quotes from at least two dealers for verification
- **Supplementary:** LCD/PitchBook leveraged loan pricing and new issue data, MarketAxess bond pricing

**Measurement methodology**
- Calculate a 5-day moving average to smooth daily volatility
- Compare current level to entry level (trade date price or spread)
- For CDS, track spread change in basis points from entry
- For loans, track price change in points from entry price
- For bonds, track both price change and OAS/Z-spread change
- Compare movement to the relevant index to distinguish idiosyncratic from systematic moves

### Rating Changes

**Data source hierarchy**
- **Primary:** S&P Global Ratings, Moody's Investors Service, Fitch Ratings direct alerts
- **Secondary:** Bloomberg RATD/CRDT functions and rating agency portals
- **Monitoring:** Real-time alerts via rating agency platforms and Bloomberg

**Measurement methodology**
- Track notch changes from entry rating
- Monitor outlook changes and CreditWatch/Review for Downgrade placements as leading indicators
- For split-rated credits, use the most conservative agency rating for risk purposes

---

## 2. Data Lineage Standards

Derived metrics must maintain a clear audit trail to source data. This ensures reproducibility and enables rapid validation when metrics are challenged.

### Derived Metric Mapping

| Derived Metric | Source Data Points | Calculation Reference |
|---|---|---|
| Adjusted Leverage (Net Debt / EBITDA) | Total Debt (balance sheet), Cash (balance sheet), EBITDA (income statement + add-backs) | modeling-and-valuation spreading methodology |
| Interest Coverage Ratio | EBITDA (as above), Total Interest Expense (income statement + PIK + commitment fees) | Per credit agreement definition, which may differ from GAAP |
| Fixed Charge Coverage | EBITDA - Capex - Taxes, Total Debt Service (interest + mandatory amort) | modeling-and-valuation FCF waterfall |
| Liquidity Runway | Cash + Undrawn Revolver, LTM Operating Cash Flow | Liquidity runway methodology above |
| Recovery Value | Enterprise Value, Priority Claims, Instrument Seniority | events-distressed recovery waterfall |

### Lineage Requirements
- Every derived metric must reference its source financial statement line items
- Add-back adjustments must be documented and consistent with the underwriting memo
- When source data changes because of a restatement or amendment, all derived metrics must be recalculated
- Maintain version history for model updates, including date, analyst, and change description

---

## 3. Stale Data Handling Method

Reference data files include `last_updated`, `update_cadence`, and `next_review` YAML frontmatter. When the current date exceeds `next_review`, the data may be stale.

### Stale Data Protocol

| Staleness Level | Definition | Required Action |
|---|---|---|
| Current | Current date <= next_review | Use data normally |
| Approaching Stale | Within 30 days of next_review, no update received | Flag for upcoming refresh and continue using with note |
| Stale | Current date > next_review | Warn user prominently, apply wider confidence intervals from `references/data-pipeline-specification.md`, and note data vintage in all outputs |
| Materially Stale | Current date > next_review + 90 days | Warn user that data may be unreliable and recommend sourcing current market data before making investment decisions |

All outputs using stale data must include: "Note: [Metric] data vintage is [date]. Current values may differ materially."

---

## 4. Quality Control Methodology

### Reconciliation Checkpoints

| Checkpoint | Validation Objective |
|---|---|
| Financial statement spreading | Confirm source financials are accurately loaded into surveillance models |
| Covenant compliance | Confirm certificate calculations and independent calculations agree |
| Market pricing | Confirm dealer marks and composite services are directionally aligned |
| Recovery estimates | Confirm recovery work is anchored to external comps and updated assumptions |
| Portfolio risk metrics | Confirm position-level data ties to accounting and custody records |

### Dual-Source Verification
- Material metrics that could trigger escalation require verification from at least two independent sources before escalation
- Rating actions from a single agency are sufficient because the agency itself is the authoritative source
- When sources conflict, use the more conservative figure for risk purposes and document the discrepancy

### Error Correction Protocol
1. Identify the error and its source
2. Assess whether the error affected any prior escalation decisions or IC recommendations
3. Correct the metric and recalculate all dependent derived metrics
4. If the correction changes an escalation tier, notify the PM immediately
5. Document the error, correction, and impact assessment in the surveillance log
