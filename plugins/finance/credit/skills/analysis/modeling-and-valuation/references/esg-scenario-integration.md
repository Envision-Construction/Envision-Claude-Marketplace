---
title: "ESG Scenario Integration"
last_updated: "2026-03-22"
update_cadence: "Annual"
next_review: "2027-03-22"
purpose: "Framework for translating ESG findings from due-diligence-and-assessment into financial scenario adjustments within modeling-and-valuation"
sources:
  - "Internal cross-skill analytical framework"
  - "Institutional credit analysis best practices"
---

# ESG Scenario Integration

This reference defines how ESG findings produced by the `due-diligence-and-assessment` skill should flow into the financial scenario analysis performed by `modeling-and-valuation`. ESG factors should not create standalone "ESG scenarios" but should instead modify existing base/downside/upside scenario probabilities and assumptions.

---

## 1. Environmental Risk to Financial Impact

### 1.1 Carbon Regulation

For companies with material Scope 1 emissions, model incremental compliance costs using a carbon tax range of $25-$75/ton applied to reported Scope 1 emissions. In the base case, use the midpoint ($50/ton) if regulation is pending or probable. In the downside case, use the upper bound ($75/ton) plus potential Scope 2 pass-through costs from utilities. Carbon costs flow through COGS or a dedicated environmental compliance line item.

### 1.2 Physical Climate Risk

For CRE and infrastructure assets, model the following physical climate impacts:

- **Insurance cost increases**: 10-30% premium increases in high-risk zones (coastal flood, wildfire, hurricane). Apply the increase as a step function at the next policy renewal date in the projection period.
- **Property value impairment**: For properties in FEMA Special Flood Hazard Areas or equivalent high-risk designations, apply a 5-15% cap rate premium relative to non-exposed comparable properties.
- **Business interruption**: For operating businesses in high-risk zones, model 5-15 days of revenue disruption per year in the downside scenario, calibrated to historical weather event frequency for the specific geography.

### 1.3 Transition Risk

For fossil fuel-adjacent sectors (oil & gas, coal, gas-fired power, petrochemicals, heavy transport), model demand decline scenarios:

- **Base case**: 5% revenue reduction over 7 years from energy transition and demand substitution
- **Downside case**: 15% revenue reduction over 5 years, reflecting accelerated regulatory action or technology disruption
- **Stranded asset risk**: For long-lived physical assets (reserves, generation capacity, pipelines), assess whether remaining economic life exceeds the transition timeline. If so, model accelerated depreciation or impairment.

### 1.4 Water Stress

For water-intensive industries (agriculture, mining, chemicals, semiconductors, beverage), model:

- **Water cost increases**: 15-40% increase in water procurement costs in water-stressed basins, based on WRI Aqueduct risk ratings
- **Operational constraints**: In the downside scenario, model 10-20% capacity reduction from water curtailment orders in high-stress regions
- **Capital expenditure**: Model incremental capex for water recycling, desalination, or alternative sourcing if the company lacks existing mitigation infrastructure

---

## 2. Social Risk to Financial Impact

### 2.1 Labor Practices

When due-diligence identifies workforce practices creating regulatory or reputational risk (wage violations, safety incidents, union activity), model:

- **Wage inflation**: 3-8% above baseline wage growth for 2-3 years to reflect remediation, union contract settlements, or regulatory compliance
- **Turnover costs**: Elevated recruiting and training costs at 50-100% of annual salary per incremental departure above baseline turnover

### 2.2 Product Safety

For companies with product safety exposure (consumer products, pharmaceuticals, food & beverage, automotive):

- **Recall costs**: Model scenario-specific recall reserves based on industry precedents (typically 1-5% of affected product revenue)
- **Litigation reserves**: Model litigation tail risk as a contingent liability, with probability weighting based on case stage and jurisdiction
- **Revenue impact**: Model 5-15% revenue decline in affected product lines for 1-2 years post-incident from brand damage

### 2.3 Data Privacy

For companies handling material personal data (technology, healthcare, financial services, retail):

- **Regulatory fines**: GDPR fines up to 4% of global revenue; CCPA/state-level fines calibrated to jurisdiction. Model as a one-time charge in the downside scenario.
- **Customer attrition**: Model 3-8% customer churn following a material data breach, with recovery over 12-18 months
- **Remediation costs**: Model incremental cybersecurity and compliance spending at 1-3% of revenue for 2-3 years post-incident

---

## 3. Governance Risk to Financial Impact

### 3.1 Board Quality

When due-diligence identifies governance weaknesses (limited independent oversight, lack of relevant expertise, entrenched management), adjust scenario probabilities:

- **Weak governance**: Increase probability of downside scenario by 10-15 percentage points relative to base assumption
- **Strong governance**: Decrease probability of downside scenario by 5-10 percentage points, reflecting better crisis management and strategic execution

### 3.2 Related-Party Transactions

When related-party transactions are identified, model value leakage:

- **Non-arm's-length pricing**: Estimate the delta between related-party pricing and market pricing for comparable transactions. Apply as a recurring drag on EBITDA or as a reduction to enterprise value.
- **Management fee extraction**: For sponsor-backed companies, model management fees, monitoring fees, and transaction fees as a separate line item reducing FCF available for debt service.

### 3.3 Compensation Misalignment

When management incentives favor EBITDA growth over deleveraging:

- **Leverage re-up probability**: Increase the probability of an acquisition-driven re-leveraging scenario by 15-25 percentage points
- **Dividend recap risk**: For PE-backed credits, model a dividend recap scenario if documentation permits and sponsor has a history of distributions within 18-24 months of closing

---

## 4. Integration Framework

For each material ESG factor identified by the `due-diligence-and-assessment` skill:

1. **Classify** the ESG factor into one of the categories above
2. **Quantify** the financial impact using the parameter ranges provided
3. **Integrate** into existing scenarios by adjusting assumptions or probabilities rather than creating a separate ESG scenario
4. **Disclose** which ESG factors were incorporated into which scenario assumptions, so the IC can evaluate the materiality and calibration of each adjustment
5. **Sensitivity test** the most material ESG factor by running the model with and without the ESG adjustment to isolate its impact on leverage, coverage, and valuation

ESG factors that do not have a quantifiable financial pathway within the projection period should be disclosed as qualitative risk factors in the credit memo rather than forced into the financial model.

---

## 5. Cap Rate Adjustment for CRE

Climate-exposed properties require a cap rate premium based on hazard zone classification:

| Hazard Zone | Cap Rate Premium | Basis |
|---|---|---|
| FEMA Zone X (minimal flood risk) | 0 bps | Baseline |
| FEMA Zone B/C (moderate flood risk) | 25 bps | Moderate insurance cost and marketability impact |
| FEMA Zone A/AE (high flood risk) | 50-75 bps | Elevated insurance costs, potential value impairment, reduced buyer pool |
| Wildfire risk (WUI zone) | 25-50 bps | Insurance availability constraints, evacuation risk |
| Hurricane zone (Category 3+ exposure) | 25-50 bps | Business interruption, insurance cost, structural damage risk |

Insurance cost trends should be modeled as a separate line item in NOI projections rather than embedded in the cap rate, to allow for transparent sensitivity analysis. Historical insurance cost growth of 8-15% annually in high-risk zones should be projected forward unless policy changes provide relief.

---

## 6. Cross-References

- `due-diligence-and-assessment` skill: ESG integration framework and materiality assessment
- `cre-analysis-underwriting` skill: Sensitivity analysis and property-level risk assessment
- `references/stress-scenario-framework.md`: Asset-class-specific stress parameters for scenario construction
- `skills/memo-generator/references/analytical-limitations.md`: Framework reliability guidance for ESG quantification
