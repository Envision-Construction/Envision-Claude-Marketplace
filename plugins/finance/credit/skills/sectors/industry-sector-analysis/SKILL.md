---
name: Industry Sector Analysis
version: "1.5.1"
last_modified: "2026-03-22"
description: |
  Use when assessing industry dynamics, cyclicality, sector-specific KPIs, competitive structure, or sector-adjusted credit risk before detailed issuer modeling. This skill frames what metrics matter, what a sector can support through the cycle, and which structural or documentation issues deserve extra scrutiny.
category: sector-analysis
related_skills:
  - memo-generator
  - modeling-and-valuation
  - surveillance-monitoring
  - debt-structure-covenants
  - due-diligence-and-assessment
  - portfolio-investment-process
  - trading-pricing-mechanics
triggers:
  - industry analysis
  - sector analysis
  - sector risk
  - industry dynamics
  - sector benchmarks
  - cyclical credit
  - defensive credit
  - industry-specific metrics
  - sector-specific red flags
disambiguation: |
  Use this skill when the question is primarily about industry structure, sector behavior, peer context, or what operating metrics matter most.
  Use modeling-and-valuation for issuer-specific forecasting, ratio analysis, and scenario mechanics.
  Use debt-structure-covenants for documentation analysis when the core issue is baskets, liens, leakage, or amendment risk.
  Use trading-pricing-mechanics for current spreads, market levels, or secondary pricing context.
  Use cre-analysis-underwriting when the asset is a property, real estate portfolio, or CRE loan rather than a corporate issuer.
---

# Industry & Sector Analysis

Sector analysis provides the context around cyclicality, competitive structure, pricing power, regulation, and sector KPIs that determine what a credit can support through the cycle. Use it to frame the issuer before detailed modeling, documentation review, or surveillance work.

## Core Workflow

1. **Define the sector and value chain**: Identify where the issuer sits in the value chain, which customers and inputs matter most, and whether the business behaves like the headline sector or a narrower sub-segment.
2. **Place the sector in cycle context**: Separate cyclical pressures from secular change and decide whether current performance reflects peak, mid-cycle, trough, or structural transition conditions.
3. **Identify the 3-5 KPIs that actually drive credit quality**: Focus on the operating metrics that explain revenue visibility, margins, working capital intensity, capital needs, and refinancing resilience.
4. **Translate sector traits into credit implications**: Convert cyclicality, pricing power, regulation, customer concentration, and capex intensity into leverage tolerance, downside severity, and likely recovery behavior.
5. **Check rating and documentation pressure points**: Note how agencies and lenders usually adjust for the sector, including lease treatment, addback risk, backlog quality, reserve assumptions, or regulated returns.
6. **Stress the sector-specific risks**: Pressure test the few variables that really matter rather than applying only generic top-line and margin shocks.
7. **Hand off clear sector context**: Pass cycle position, KPI interpretation, peer framing, and key red flags into modeling, covenant review, surveillance, or memo-writing work.

## Reference Map

Read the narrowest relevant reference rather than loading the full library.

### Default reading order

1. **`references/cross-asset-sector-framework.md`** — Start here: the five-dimension universal scaffold for cross-sector and cross-asset comparisons (corporate, private credit, CRE, infrastructure, structured finance).
2. **`references/sector-toolkit.md`** — Compact overlays: cyclical and secular framing, pricing power and pass-through, cross-sector comparison shortcuts, leverage calibration prompts, documentation watchpoints, and supply-chain vulnerability.
3. **`references/technology-disruption-timeline.md`** — **Timing and debt-life lens:** disruption horizons, maturity alignment, and refinancing-risk framing across industries. This is **not** a substitute for `references/industry/technology.md`, which holds the technology-sector operating detail, KPIs, and sub-sector deep dives. For property-type digital infrastructure, use `references/industry/real-estate-data-centers.md` for data centers and `references/industry/real-estate-alternative.md` for towers and related alternative real-estate digital infrastructure.
4. **`references/industry/*.md`** — Sector-specific files as needed (for example agribusiness-protein-fertilizer, aerospace-defense, automotive, banks, business-services, building-construction, capital-markets-asset-management, chemicals, consumer-finance, energy-midstream, environmental-services-waste, financial-services, food-beverage, gaming-leisure-hospitality, healthcare, household-personal-care-consumer-products, industrials-manufacturing, insurance, media, metals-mining, packaging, paper-forest-products, payments-fintech, pharma-biotech-medtech, power-generation-renewables, real-estate-alternative, real-estate-data-centers, real-estate-hotels, real-estate-industrial-logistics, real-estate-office, real-estate-residential, real-estate-retail, retail-consumer, specialty-finance-leasing, technology, telecom, tobacco, transportation-logistics, and utilities-infrastructure).

## Output Deliverables

When asked to analyze a sector or provide industry context for a credit, produce:

1. **Source citations**: Explicitly cite all data, qualitative claims, and benchmark inputs.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Sector framing**: Market structure, cycle position, and whether the key issue is cyclical, secular, regulatory, or company-specific.
3. **Key credit metrics**: The sector-specific KPIs that matter most and how to interpret them.
4. **Sector-adjusted leverage view**: What the sector can generally support, using `references/rating-agency-thresholds.md` for any current numerical calibration.
5. **Agency and structural watchpoints**: What agencies and lenders usually focus on for this sector.
6. **Common red flags**: The operating or structural warning signs that most often precede credit deterioration.
7. **Stress implications**: The few downside scenarios most likely to break the thesis.
8. **Handoff inputs**: Clear takeaways for modeling, covenant review, surveillance, or memo writing.

## Limitations

- Sector labels can hide more than they reveal; some issuers behave like a niche sub-sector rather than the headline industry.
- Sector heuristics are starting points, not rating outcomes; issuer-specific positioning, financial policy, and documentation still dominate final credit judgment.
- Benchmark ranges are least useful at cyclical peaks, during structural transition, or when accounting treatment materially distorts reported EBITDA.
- For broader framework limitations, consult `skills/memo-generator/references/analytical-limitations.md`.

## Data Quality

- When data is incomplete or unavailable, consult `skills/memo-generator/references/incomplete-data-guidance.md` for gap disclosure templates. Never silently fill gaps with assumptions.
- If the answer depends on current spread levels, current rating calibration, or current documentation conditions, use the relevant root reference rather than relying on timeless sector notes.
- When applying standard analytical frameworks, consult `skills/memo-generator/references/analytical-limitations.md` to identify when the framework may produce unreliable results. Disclose limitations proactively rather than presenting framework outputs as authoritative.

## Examples
- `examples/worked-sector-analysis-example.md`: Sector analysis for business services showing market structure, cycle framing, key KPIs, sector risks, and sector-adjusted credit interpretation.
