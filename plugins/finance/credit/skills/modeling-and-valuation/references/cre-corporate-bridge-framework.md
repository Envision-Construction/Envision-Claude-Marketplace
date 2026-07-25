---
last_updated: "2026-03-22"
---

# CRE-Corporate Bridge Framework

This framework bridges property-level CRE analysis (`cre-analysis-underwriting`) with corporate financial analysis (`modeling-and-valuation`) for borrowers where real estate is a material component of value, revenue, or cost structure.

---

## 1. When to Apply

Use this framework when analyzing a corporate borrower where any of the following conditions are met:

| Trigger | Threshold | Examples |
|---|---|---|
| Real estate as % of total assets | >15% | REITs, hospitality, gaming, healthcare facilities |
| Revenue from owned properties | >20% of total revenue | Hotel operators, self-storage, senior living |
| Lease obligations as % of EBITDA | >10% of EBITDA (annual rent / EBITDA) | Retail chains, restaurant groups, healthcare services |
| Sale-leaseback transactions | Material completed or pending | LBO targets, asset-heavy industrials |
| Owned property as collateral | Secured credit with RE collateral | Secured loans with mortgage liens on operating facilities |

When none of these thresholds are met, standard corporate credit analysis is sufficient without property-level CRE overlay.

---

## 2. Property-Level Analysis

For each material owned property or property portfolio, apply `cre-analysis-underwriting` frameworks:

### 2.1 Standalone Property Assessment

- **Net Operating Income (NOI)**: Calculate property-level NOI using actual rent rolls, occupancy, and operating expenses. Distinguish between properties leased to third parties and properties used in the borrower's own operations.
- **Valuation**: Apply cap rate methodology appropriate to the property type and market. For owner-occupied properties, estimate fair market value based on comparable sales or replacement cost.
- **Marketability**: Assess time-to-sale and potential buyer universe. Specialized facilities (manufacturing plants, data centers, hospitals) have narrower buyer pools and longer marketing periods than general-purpose properties (office, warehouse, retail).

### 2.2 Portfolio-Level Aggregation

When a borrower owns multiple properties, aggregate property-level analysis into a portfolio view:

- **Geographic concentration**: Identify markets representing >20% of portfolio value and assess market-specific risks
- **Property type mix**: Diversification across property types provides some downside protection but complicates valuation
- **Age and condition**: Estimate deferred maintenance and near-term capital expenditure requirements
- **Lease rollover profile**: Map lease expirations by year to identify refinancing or re-leasing risk concentrations

---

## 3. Sale-Leaseback Assessment

Many leveraged companies use sale-leasebacks to monetize real estate value. Analyze the following dimensions:

### 3.1 Value Extraction vs. Preservation

- **Fair market value vs. proceeds**: Was the property sold at, above, or below appraised value? Below-market sales suggest urgency or weak negotiating position.
- **Gain/loss recognition**: Accounting treatment (ASC 842) affects reported earnings but not cash flow. Focus on the economic terms.

### 3.2 Lease Terms Analysis

- **Rent reasonableness**: Compare annual rent to market rents for comparable properties. Above-market rents represent a hidden cost that depresses true EBITDA.
- **Lease term and renewal options**: Longer initial terms provide stability but may lock in above-market rates. Analyze renewal option pricing.
- **Escalation provisions**: Fixed escalators (1.5-2.5% annually) are preferable to CPI-linked escalators in inflationary environments from a credit perspective.
- **Operating flexibility**: Assess sublease rights, co-tenancy provisions, and early termination options. Restricted flexibility limits the borrower's ability to rationalize its footprint.

### 3.3 Credit Impact

- **EBITDA vs. EBITDAR analysis**: Sale-leasebacks convert depreciation and interest (in EBITDA) to rent (excluded from EBITDA but included in EBITDAR). Always compare leverage on both bases.
- **Capitalized lease obligation**: Apply 6-8x annual rent as a quick capitalization factor for leverage comparison. Refine using the weighted-average remaining lease term if available.
- **Fixed charge coverage**: Include rent payments in fixed charge coverage ratios (EBITDAR / [interest + rent]) to capture the true debt service burden.

---

## 4. Owned Real Estate as Recovery Backstop

For secured credits where owned real estate provides collateral support:

### 4.1 Collateral Value Assessment

- **Appraised value vs. book value**: Book value may significantly lag or lead market value. Require third-party appraisals no more than 12 months old for material properties.
- **Encumbrances**: Identify existing mortgages, tax liens, environmental liens, and mechanic's liens that reduce available equity.
- **Liquidation timeline**: Assume 12-18 months for orderly disposition of general-purpose properties, 18-36 months for specialized facilities. Apply a 15-25% discount for forced or accelerated sales.

### 4.2 Recovery Contribution

- **Use-specific vs. general-purpose**: Specialized facilities (chemical plants, custom manufacturing) typically recover 30-50% of replacement cost in liquidation. General-purpose properties (office, warehouse) recover 50-75% of market value.
- **Going-concern vs. liquidation**: If the business is viable as a going concern, owned RE contributes to enterprise value. In liquidation, owned RE is valued on a standalone basis with appropriate discounts.
- **Environmental liability**: For industrial properties, environmental remediation obligations can materially reduce or eliminate recovery value. Flag properties with known contamination or CERCLA exposure.

---

## 5. Lease Obligations in Corporate Credit Analysis

### 5.1 Leverage Comparison

Present leverage on both an EBITDA and EBITDAR basis for any company where annual rent exceeds 5% of EBITDA:

| Metric | Formula | Use Case |
|---|---|---|
| Total Debt / EBITDA | Standard leverage | Companies with minimal lease exposure |
| (Total Debt + Capitalized Leases) / EBITDAR | Lease-adjusted leverage | Companies with material operating leases |
| Capitalization factor | 6-8x annual rent (quick) or PV of lease payments (precise) | Converting rent to debt-equivalent |

### 5.2 Rating Agency Treatment

Rating agencies capitalize operating leases when assessing leverage, though methodologies differ. When comparing to rating benchmarks in `references/rating-agency-thresholds.md`, ensure the leverage calculation matches the agency's methodology for the relevant sector.

---

## 6. CRE Market Risk and Corporate Credit Impact

When owned properties are in markets experiencing stress:

- **Vacancy increases**: Model potential vacancy loss if the borrower's own space requirements shrink (store closures, office consolidation). Vacant owned properties generate zero revenue but still incur carrying costs (taxes, insurance, maintenance).
- **Rent declines**: For properties leased to third parties, model mark-to-market risk on lease expirations using current market rents vs. in-place rents.
- **Impairment charges**: If property market values decline below book value, model potential impairment charges. While non-cash, impairments can trigger covenant issues and signal balance sheet deterioration.
- **Liquidity impact**: Properties generating negative cash flow (carrying costs exceed income) create a liquidity drag. Quantify the monthly or quarterly cash burn from underperforming properties.

---

## 7. Sector-Specific CRE Exposure

| Sector | Key CRE Considerations |
|---|---|
| Retail | Store fleet as a real estate portfolio: sales per square foot, lease rollover, dark store risk, co-tenancy clauses. Distinguish between owned and leased locations. |
| Healthcare | Hospital and outpatient facility values tied to certificates of need, payor mix, and regulatory environment. Specialized assets with limited alternative use. |
| Gaming | Resort properties include hotel, casino floor, convention, and entertainment. Difficult to separate RE value from operating business value. License-dependent. |
| Restaurants | Franchise vs. corporate-owned locations create different RE exposure profiles. Corporate-owned stores have RE value; franchise locations typically do not. |
| Industrials | Manufacturing facilities may have environmental legacy costs. Assess brownfield vs. greenfield value and alternative use potential. |
| Senior Living | Demographic tailwinds but regulatory complexity. Certificate of need requirements and state-specific licensing create barriers to alternative use. |

---

## 8. Analytical Workflow

When this framework applies, follow this sequence:

1. **Identify material RE holdings** from the 10-K property schedule, supplemental disclosures, and management commentary. Classify each property by type, ownership status (owned/leased/ground lease), and materiality.
2. **Apply cre-analysis-underwriting** for property-level analysis on all material owned properties. Produce standalone NOI, valuation, and marketability assessments.
3. **Integrate property-level findings** into the corporate financial model: adjust EBITDA for above/below-market lease costs, adjust asset value for property market conditions, and add property-specific capex requirements to the capital expenditure forecast.
4. **Stress test property market scenarios** as an additional downside variant: model a property market downturn with 10-20% value decline, 200-500bps cap rate expansion, and 10-15% rent decline on lease rollovers. Assess the impact on leverage, liquidity, and covenant compliance.

---

## 9. Cross-References

- `cre-analysis-underwriting` skill: Property-level analysis frameworks, cap rate methodology, loan sizing
- `modeling-and-valuation` skill: Corporate financial modeling, scenario analysis, leverage calculation
- `debt-structure-covenants` skill: Covenant definitions (EBITDA vs. EBITDAR), collateral packages, permitted liens
- `references/market-benchmarks.md`: Current CRE cap rates and spread benchmarks
- `skills/memo-generator/references/analytical-limitations.md`: Framework reliability guidance for cap rate and property valuation models
