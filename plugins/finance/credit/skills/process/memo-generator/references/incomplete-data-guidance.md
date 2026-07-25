---
last_updated: "2026-03-21"
---

# Incomplete Data Guidance

Credit analysis frequently proceeds with imperfect information. The analyst's responsibility is not to delay indefinitely until all data is available, but to identify gaps explicitly, assess their materiality, use defensible proxies where appropriate, and ensure the recommendation reflects the residual uncertainty. Suppressing data gaps — or silently filling them with assumptions — undermines the memo's credibility and exposes the portfolio to unquantified risk.

---

## Common Data Gaps by Credit Type

### Corporate Credit (Public)

| Data Element | Typical Gap | Materiality |
|---|---|---|
| Segment-level profitability | Consolidated reporting only; no margin breakdown by business line | Medium — prevents assessment of cross-subsidization and business mix risk |
| EBITDA add-back detail | Aggregate "pro forma adjustments" without line-item breakdown | High — can mask 1.0-2.0x of leverage difference between reported and actual |
| Customer concentration | Not disclosed beyond "no single customer > 10% of revenue" | Medium — relevant for credits where top-customer loss would impair EBITDA > 15% |
| Capex split (maintenance vs. growth) | Total capex only; no maintenance/growth breakdown | Medium — affects FCF sustainability assessment |
| Working capital seasonality | Annual data only; quarterly swings not disclosed | Low-to-Medium — matters for liquidity-constrained credits |

### Private Credit / Middle Market

| Data Element | Typical Gap | Materiality |
|---|---|---|
| Audited financials | Quality of earnings (QoE) report only; no audited statements available | High — QoE adjustments may be sponsor-favorable; no independent verification of underlying data |
| Historical track record | Fewer than three years of operating history post-acquisition or carve-out | High — limits ability to assess cyclical resilience |
| Management depth | Limited information beyond CEO and CFO | Medium — key-person risk often unquantified |
| Comparable company data | Few or no publicly traded direct peers | Medium — impairs relative value analysis and recovery assumptions |
| Credit agreement details | Draft or summary terms; final documentation not yet available | High — covenant protections, incremental capacity, and permitted baskets may change materially |

### Commercial Real Estate

| Data Element | Typical Gap | Materiality |
|---|---|---|
| Tenant-level financials | Rent roll available, but no tenant credit quality data | High for concentrated properties — single-tenant default could impair DSCR below 1.0x |
| Lease renewal probability | No historical renewal data for the specific property | Medium — assumptions drive cash flow beyond current lease term |
| Comparable sales data | Limited transaction volume in the submarket | Medium — affects cap rate and valuation assumptions |
| Environmental assessments | Phase I only; no Phase II when indicators warrant | High for industrial and legacy properties |
| Deferred maintenance estimates | Owner-provided estimates only; no independent assessment | Medium — affects exit valuation and near-term capital requirements |

### Structured Finance (ABS / CLO / CMBS)

| Data Element | Typical Gap | Materiality |
|---|---|---|
| Granular pool-level data | Summary statistics only; no loan-level tape available | High for concentrated pools; lower for granular, homogeneous pools (> 500 assets) |
| Historical performance by vintage | Manager or originator track record limited to recent vintages (post-2020) | High — no through-the-cycle data available for credit stress calibration |
| Servicer quality metrics | Limited data on loss mitigation effectiveness, modification rates, and timeline to resolution | Medium — servicer performance drives realized losses vs. modeled defaults |
| Prepayment behavior | Limited prepayment data for the specific asset class or originator | Medium — affects weighted average life, reinvestment risk, and excess spread |
| Correlation assumptions | No empirical basis for default correlation in the specific pool | High for mezzanine and equity tranches where correlation drives loss distribution |

---

## Flagging Gaps in the Memo

### Principles

1. **Never silently fill a gap with an assumption.** Every material assumption must be disclosed, labeled as an assumption, and sensitivity-tested.
2. **Distinguish between "unknown" and "unknowable."** A tenant's financial statements may be obtainable with further diligence (unknown). Historical performance of a newly originated asset class through a recession may not exist (unknowable).
3. **Quantify the impact of the gap.** Do not simply note that data is missing — state what effect the missing data could have on the analysis. "Tenant financials are unavailable" is informational. "Tenant financials are unavailable; if the anchor tenant (38% of NOI) is downgraded or defaults, property DSCR falls from 1.45x to 0.90x" is analytical.
4. **Place the flag where it matters.** Disclose data gaps in the section where the gap affects the analysis, not only in a catch-all appendix.

### Template Language for Data Limitation Callouts

Use the following format to flag material data gaps within memo sections. These should be visually distinct (bold header, indented block) so reviewers can identify limitations quickly.

**For missing financial data:**

> **Data Limitation — [Topic]**: [Specific data element] is not available. Analysis in this section relies on [proxy/assumption used]. Sensitivity analysis indicates that [range of outcomes if the actual data differs from the proxy]. This gap [does / does not] affect the recommendation at the stated conviction level.

**Example:**

> **Data Limitation — Maintenance Capex**: The issuer does not disclose maintenance vs. growth capex. We estimate maintenance capex at 3.5% of revenue based on the peer median for specialty chemicals companies. If actual maintenance capex is 5.0% of revenue (the high end of the peer range), normalized FCF declines by $45M annually and FCF/Debt falls from 8.2% to 5.4%. This gap is reflected in the medium (rather than high) conviction level assigned to the recommendation.

**For missing market data:**

> **Data Limitation — [Topic]**: No directly comparable [transactions / trading levels / benchmarks] are available for [reason]. We use [proxy] as the closest substitute, which may [overstate / understate] [specific metric] by an estimated [range]. The relative value assessment should be interpreted with this limitation in mind.

**For missing documentation:**

> **Data Limitation — Credit Agreement**: Final documentation is not yet available; analysis is based on the [summary terms / draft credit agreement dated MM/DD/YYYY]. Key provisions subject to change include [specific items]. The recommendation is conditional on final documentation being consistent with draft terms. A material weakening of [specific provision] would trigger a reassessment.

---

## Acceptable Proxies

When primary data is unavailable, the following proxies are ranked from most to least reliable:

| Proxy Type | Use When | Reliability | Caveats |
|---|---|---|---|
| **Peer median / industry benchmark** | Specific data point is missing but peers disclose it | High, if peer set is genuinely comparable | Adjust for company-specific factors (scale, geography, business mix) |
| **Rating agency estimates** | Agency has conducted independent analysis and published an assessment | Medium-to-High | Agency methodologies may lag; estimates may be stale |
| **QoE / third-party diligence reports** | Private credit or M&A transaction with sponsor-commissioned reports | Medium | QoE providers are retained by the sponsor; adjustments may reflect sell-side optimism |
| **Management guidance / projections** | No independent data available for future periods | Low-to-Medium | Must sensitivity-test; historically, management projections have a positive bias of 15-25% on EBITDA for leveraged borrowers |
| **Historical analogues** | No data exists for the specific asset but a similar situation has been observed | Low-to-Medium | Analogues are never exact; differences must be identified and impact assessed |
| **Sector-wide statistical averages** | No company-specific or peer-specific data exists | Low | Averages mask dispersion; use the range (25th to 75th percentile), not just the median |

**Proxy disclosure requirement**: Whenever a proxy is used, the memo must state: (1) what primary data is missing, (2) what proxy is substituted, (3) the source of the proxy data, and (4) the direction and estimated magnitude of potential error.

---

## Decision Framework: When Gaps Are Acceptable vs. Blocking

### Acceptable Gaps (Proceed with Adjusted Conviction)

- Gap affects a secondary analytical dimension, not the core thesis
- A reliable proxy is available and the sensitivity range is bounded
- The gap can be closed through post-investment diligence within a defined timeframe
- Position sizing is reduced to reflect residual uncertainty
- Spread compensation is sufficient to absorb the range of outcomes under the proxy

### Blocking Gaps (Do Not Proceed / Conditional Pass)

- Gap affects the core thesis or primary credit driver
- No reliable proxy exists and the range of outcomes is wide enough to span the entire buy/avoid spectrum
- The gap cannot be closed within a reasonable diligence timeline
- The gap relates to structural protections (credit agreement terms, intercreditor provisions) that define loss-given-default
- Recovery analysis cannot be performed because asset values or lien priorities are unverifiable

### Decision Table

| Gap Materiality | Proxy Available & Reliable | Proxy Unreliable or Unavailable |
|---|---|---|
| **Low** (does not affect core thesis or key metrics by > 0.5x leverage or > 50bps spread) | Proceed at full conviction | Proceed; disclose gap; no conviction adjustment needed |
| **Medium** (affects one key metric by 0.5-1.0x leverage or 50-150bps spread equivalent) | Proceed with conviction reduced one level; sensitivity-test the proxy | Conditional Pass — identify what data is needed to proceed |
| **High** (affects core thesis or multiple key metrics by > 1.0x leverage or > 150bps) | Proceed only if proxy is independently verifiable; conviction reduced one level | Decline — insufficient basis for responsible underwriting |

---

## Integration with Other Frameworks

- **Conviction calibration**: Data gaps directly reduce conviction levels. See `references/conviction-calibration.md` for the conviction decision matrix linking information completeness to recommendation actions.
- **Conflict resolution**: Data gaps can create apparent conflicts when one analytical dimension uses verified data and another relies on proxies. See `references/conflict-resolution-guide.md` for weighting by data quality.
- **Memo checklist**: The pre-submission checklist (`references/memo-structure-and-writing-guide.md`) includes data integrity checks. Every proxy should be traceable to a disclosed source, and every material gap should appear in the relevant memo section.
