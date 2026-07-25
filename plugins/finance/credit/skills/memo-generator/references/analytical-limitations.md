---
last_updated: "2026-03-21"
---

# Analytical Limitations & Framework Pitfalls

When standard frameworks produce unreliable results, analysts must recognize the limitation, disclose it, and use supplementary or alternative approaches.

## Corporate Credit Limitations

### EBITDA as a Credit Metric
- **When it misleads**: Asset-light businesses (software, services) with high stock-based compensation; EBITDA overstates cash generation because SBC is a real economic cost
- **When it misleads**: Businesses with heavy maintenance capex requirements; EBITDA does not reflect the capital investment required to sustain operations
- **When it misleads**: Companies with large working capital swings (seasonal, project-based); EBITDA-to-FCF conversion can be <50%
- **Supplementary approach**: Use unlevered free cash flow (UFCF) or cash EBITDA (EBITDA less SBC, less maintenance capex) as the primary metric

### Leverage Ratios
- **When they mislead**: Near-zero or negative EBITDA makes Debt/EBITDA meaningless (division by near-zero)
- **When they mislead**: Companies with large cash balances — Net Debt/EBITDA masks gross debt service obligation
- **When they mislead**: Highly seasonal businesses — point-in-time leverage depends on measurement date
- **Supplementary approach**: Use Debt/Revenue, Debt/Total Assets, or fixed-charge coverage as primary metrics when leverage ratio is unstable

### EBITDA Addbacks
- **When they mislead**: "Run-rate" synergies in pro forma EBITDA for acquisitions may never materialize
- **When they mislead**: "Non-recurring" charges that recur every year are, by definition, recurring
- **Red flag**: Total addbacks >25% of reported EBITDA — the gap between reported and adjusted signals uncertainty in true earnings power

### Comparable Company Analysis
- **When it misleads**: Small peer universe (<5 truly comparable companies) produces statistically unreliable ranges
- **When it misleads**: Companies with different business models grouped together (e.g., a SaaS company in a "technology" comp set with hardware manufacturers)
- **When it misleads**: Trading multiples during market dislocation reflect liquidity, not fundamental value
- **Supplementary approach**: Use through-cycle valuation multiples; weight precedent transactions more heavily than trading comps during periods of market stress

## CRE Limitations

### Cap Rate Valuation
- **When it misleads**: Distressed markets where few transactions occur — cap rates are stale and understated
- **When it misleads**: Transitional properties with below-market rents — applying market cap rate to in-place NOI understates potential value
- **When it misleads**: Single-tenant properties — cap rate reflects tenant credit, not property quality
- **Supplementary approach**: Use DCF with explicit lease-by-lease modeling; replacement cost analysis; comparable sales on a per-square-foot basis

### DSCR for Loan Sizing
- **When it misleads**: Properties with short remaining lease terms — current DSCR looks fine but reversion risk is high
- **When it misleads**: Properties with below-market rents — DSCR may improve at rollover (positive), or tenants may leave (negative)
- **Supplementary approach**: Model DSCR through the full loan term including lease expiration scenarios; use debt yield as a complementary metric

## Structured Finance Limitations

### CLO OC Test Manipulation
- **How it happens**: CLO managers can maintain OC test compliance by purchasing discounted loans at prices below par but marking them at par for OC test purposes (the "par building" trade)
- **Why it misleads**: OC test cushion looks healthy while underlying portfolio credit quality is deteriorating
- **Detection**: Track the gap between OC test par and mark-to-market par; if mark-to-market par is declining while OC par is stable, the manager is likely par building
- **Supplementary approach**: Monitor WARF (weighted average rating factor) and market value OC test as supplements to par-based OC test

### ABS Loss Curve Assumptions
- **When they mislead**: Unprecedented economic environments (pandemic, housing crisis) where historical loss curves are not predictive
- **When they mislead**: Newly originated asset classes without full cycle performance data
- **Supplementary approach**: Stress loss assumptions to multiples of historical peaks; use conditional loss distributions rather than single-point estimates

### Prepayment Model Sensitivity
- **When it misleads**: Rapid rate movements make historical prepayment models unreliable — both faster-than-expected prepayments (shortening WAL) and slower-than-expected (extending WAL) create basis risk
- **Supplementary approach**: Model prepayments at multiple speed assumptions (base, fast, slow); compute yield sensitivity to each

## Private Credit Limitations

### Fair Value Marking
- **When it misleads**: Private credit positions are marked to model, not to market — managers have discretion in marks
- **When it misleads**: Unrealized appreciation in a strong market may reverse in a downturn faster than marks adjust
- **Detection**: Compare fair value marks to public market comps for similar credits; track the lag between public market moves and private credit marks
- **Supplementary approach**: Use public market proxies (comparable rated loans, CLO holdings) to cross-check private marks

### Illiquidity Premium Decomposition
- **When it misleads**: Attributing all excess spread over public markets to "illiquidity premium" ignores that private credits may have higher fundamental risk (smaller borrowers, less diversified)
- **Supplementary approach**: Decompose spread into: credit risk premium + illiquidity premium + complexity premium + origination/structuring value. Only the true illiquidity premium is "free" — the rest compensates for real risk

## General Analytical Pitfalls

### Survivorship Bias
- Analyzing only current performing credits ignores those that defaulted — historical performance looks better than reality
- Always include defaulted/exited positions in performance analysis

### Anchoring to Entry Price
- A credit trading at 95 that was bought at par is not "cheap" — it may be correctly repriced
- Evaluate based on current fundamentals, not entry price

### Confirmation Bias in Stress Testing
- Analysts tend to construct stress scenarios that their thesis survives
- Counter-stress: construct the scenario specifically designed to break the thesis, then assess its plausibility
