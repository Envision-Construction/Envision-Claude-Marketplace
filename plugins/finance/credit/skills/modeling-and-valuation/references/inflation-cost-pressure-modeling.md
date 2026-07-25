---
last_updated: "2026-03-22"
---

# Inflation & Cost Pressure Modeling

Framework for modeling the impact of input cost inflation on EBITDA, margins, and credit metrics. Applicable across corporate credit, private credit, and leveraged finance analysis.

## Cost Structure Classification

Before modeling inflation impact, classify the issuer's cost base:

| Cost Category | Description | Inflation Sensitivity | Examples |
|---|---|---|---|
| Raw Materials | Physical inputs to production | HIGH — direct commodity exposure | Steel, resin, agricultural inputs |
| Energy | Electricity, natural gas, fuel | HIGH — volatile, correlated with macro | Chemicals, metals, transportation |
| Labor | Wages, benefits, contract labor | MEDIUM-HIGH — sticky, lagging | Healthcare, staffing, food service |
| Rent/Occupancy | Facility leases, property costs | LOW-MEDIUM — contractual escalators | Retail, restaurants, warehousing |
| Technology/SaaS | Software licenses, IT infrastructure | LOW — deflationary long-term trend | All sectors (typically <5% of cost base) |
| Transportation/Logistics | Freight, shipping, distribution | MEDIUM-HIGH — fuel and labor driven | Consumer goods, e-commerce, food |

**Fixed vs. Variable Cost Mix**: Higher fixed-cost businesses (>60% fixed) experience operating leverage — margin expansion in growth, but accelerated margin compression when revenue declines. Variable-cost businesses have more natural inflation pass-through but lower operating leverage.

## Pass-Through Mechanisms

### Pricing Power Assessment

Evaluate the issuer's ability to pass through cost increases to customers:

| Pass-Through Mechanism | Lag Period | Reliability | Examples |
|---|---|---|---|
| Contractual escalators (CPI-linked) | Immediate to quarterly | HIGH — automatic | Waste management, utilities, long-term service contracts |
| Commodity surcharges | Immediate to monthly | HIGH — transparent mechanism | Chemicals, metals, packaging |
| Annual contract repricing | 6-12 months | MEDIUM — subject to negotiation | Business services, food distribution |
| Competitive spot pricing | 1-3 months | LOW-MEDIUM — depends on market structure | Generic pharma, commodity staffing |
| Menu/list price increases | 3-6 months | MEDIUM — consumer elasticity risk | Restaurants, retail, consumer products |
| Long-term fixed contracts | Contract term (1-5 years) | NONE until renewal | Government contracts, defense, some healthcare |

### Key Questions for Pass-Through Assessment

1. Does the issuer have contractual escalation clauses? What index? What cap/floor?
2. What is the competitive structure? Price leader or price taker?
3. How essential is the product/service to the customer? (Essential = higher pass-through)
4. What is the customer concentration? High concentration reduces pricing power.
5. Are there viable substitutes? If yes, pass-through capacity is constrained.

## Sector-Specific Inflation Sensitivity

| Sector | Input Cost Sensitivity | Pass-Through Ability | Net Margin Impact |
|---|---|---|---|
| Chemicals (commodity) | HIGH — feedstock driven | HIGH — formula pricing | LOW — effective pass-through |
| Chemicals (specialty) | MEDIUM — diverse inputs | HIGH — differentiated products | LOW |
| Metals & Mining | HIGH — energy, labor | HIGH — commodity pricing | MEDIUM — lag effects |
| Staffing/Labor Services | HIGH — labor is the product | MEDIUM — competitive repricing | MEDIUM-HIGH |
| Healthcare Services | HIGH — labor (60-70% of costs) | LOW-MEDIUM — payer mix constraints | HIGH — margin compression risk |
| Food & Beverage | HIGH — agricultural inputs | MEDIUM — brand-dependent | MEDIUM |
| Technology/SaaS | LOW — minimal physical inputs | HIGH — subscription pricing | LOW — natural hedge |
| Utilities (regulated) | MEDIUM — fuel, labor | HIGH — rate case recovery | LOW — regulatory pass-through |
| Transportation | HIGH — fuel, labor, equipment | MEDIUM — competitive market | MEDIUM-HIGH |
| Retail (discretionary) | MEDIUM — COGS, labor | LOW — price-sensitive consumers | HIGH |

## Margin Impact Modeling Framework

### Step-by-Step Process

1. **Identify cost categories** and their share of total costs (use most recent 10-K cost breakdown)
2. **Assign inflation sensitivity** (high/medium/low) to each category based on table above
3. **Model cost inflation** by category using scenario assumptions (see stress table below)
4. **Assess pass-through capability** by category — what percentage of cost increase can be recovered through pricing?
5. **Calculate net margin impact** = Cost Increase - Price Recovery = Margin Compression
6. **Translate to EBITDA impact** and recalculate leverage/coverage ratios

### Stress Scenario Matrix

| Input Cost Inflation | Pass-Through: 0% | Pass-Through: 50% | Pass-Through: 100% |
|---|---|---|---|
| 3% (mild) | EBITDA margin -150 to -200bps | EBITDA margin -75 to -100bps | Margin neutral |
| 5% (moderate) | EBITDA margin -250 to -350bps | EBITDA margin -125 to -175bps | Margin neutral |
| 8% (severe) | EBITDA margin -400 to -550bps | EBITDA margin -200 to -275bps | Margin neutral |

*Note: Actual impact depends on cost structure composition and gross margin level. Lower-margin businesses (e.g., distribution, staffing) experience proportionally larger EBITDA impact from the same percentage cost increase.*

### Worked Example

Company with $500M revenue, 20% EBITDA margin ($100M EBITDA), 60% variable costs:
- 5% input cost inflation on variable costs = $15M cost increase
- 50% pass-through = $7.5M price recovery
- Net EBITDA impact = -$7.5M (new EBITDA = $92.5M)
- If leverage was 5.0x ($500M debt), new leverage = 5.4x — a meaningful deterioration

## Credit Implications

- **Nominal vs. Real EBITDA**: Revenue and EBITDA may grow nominally during inflation while real (inflation-adjusted) EBITDA declines. A company reporting 3% EBITDA growth with 5% cost inflation is actually deteriorating.
- **Leverage Denominator Effect**: Inflation that cannot be passed through compresses EBITDA, increasing leverage ratios even without additional debt. This is the primary credit risk from inflation.
- **Working Capital Drag**: Inflation increases the dollar value of receivables and inventory, consuming cash. Model working capital as a use of cash in inflationary scenarios.
- **Interest Rate Correlation**: Inflation typically leads to higher interest rates, creating a double hit for floating-rate borrowers — margin compression (lower EBITDA) combined with higher debt service (higher interest expense).
- **Covenant Implications**: Model whether inflation-driven EBITDA compression breaches maintenance covenants. Companies with tight covenant headroom (<15%) are most vulnerable.

## Red Flags

- Cost structure >50% exposed to high-sensitivity categories without contractual pass-through
- Historical evidence of margin compression during prior inflationary periods (2021-2023 data is informative)
- Customer contracts with fixed pricing and remaining terms >12 months during rising input costs
- Management guidance projecting margin stability without articulating specific pass-through mechanisms
- Labor-intensive business in tight labor market without wage escalation provisions in customer contracts
