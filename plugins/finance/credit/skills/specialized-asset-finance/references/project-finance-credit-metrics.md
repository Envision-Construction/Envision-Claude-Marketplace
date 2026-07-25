---
last_updated: "2026-03-22"
---

## Project Finance Credit Metrics

Project finance metrics are designed to answer a narrow question: how much durable project cash flow stands between the lender and a payment default? Use the metrics below as analytical tools, then calibrate thresholds and market conventions from the project-root references.

## DSCR

**Debt Service Coverage Ratio (DSCR)** measures period-by-period debt service capacity:

`DSCR = CFADS / Scheduled Debt Service`

Where:

- **CFADS** is cash flow available for debt service after operating costs, taxes, required working-capital needs, and any other deductions defined in the financing documents.
- **Scheduled debt service** is the interest and principal due in the period being tested.

Use DSCR to judge:

- current payment capacity
- sensitivity to revenue, cost, or rate shocks
- whether distributions should be permitted or trapped
- whether the debt profile is matched to the project's cash generation

## LLCR

**Loan Life Coverage Ratio (LLCR)** measures debt coverage over the remaining loan life:

`LLCR = NPV of CFADS over remaining loan life / Outstanding Debt`

Use LLCR to judge:

- how much cushion exists across the remaining debt tenor
- whether debt sizing relies too heavily on late-period cash flow
- whether the refinancing or mini-perm structure leaves too little room for underperformance

LLCR is more stable than a single-period DSCR because it captures the shape of future cash flow, not just the next payment date.

## PLCR

**Project Life Coverage Ratio (PLCR)** extends the same logic to the full remaining project or concession life:

`PLCR = NPV of CFADS over remaining project life / Outstanding Debt`

Use PLCR to judge:

- whether there is meaningful value beyond the debt tenor
- whether the contract or concession tail genuinely supports recovery
- whether equity still has an incentive to support the project through stress

PLCR should not be used to excuse weak near-term DSCR; it is a tail-value measure, not a substitute for current debt service capacity.

## Practical Interpretation

When reading these metrics together:

- **DSCR** answers whether the project can service debt now.
- **LLCR** answers whether the remaining debt life still looks money-good.
- **PLCR** answers whether the full project life provides additional value beyond the loan term.

Large gaps between the three ratios often reveal the real issue:

- Strong PLCR with weak DSCR may indicate back-ended cash flow, ramp-up dependence, or excessive refinancing risk.
- Strong DSCR with weak LLCR may indicate a near-term good year masking structural weakness later in the debt tenor.
- Strong LLCR but weak PLCR may indicate little concession tail or a poor residual position after debt maturity.

## Calibration Notes

- Metric definitions should match the legal documents; do not mix management definitions with covenant definitions.
- Reserve funding, sweep mechanics, and locked-up cash can materially change the numerator or the timing of cash available to debt.
- Current threshold ranges and market conventions belong in `references/typical-deal-parameters.md`.
- Stress calibration belongs in `references/stress-scenario-framework.md`.
