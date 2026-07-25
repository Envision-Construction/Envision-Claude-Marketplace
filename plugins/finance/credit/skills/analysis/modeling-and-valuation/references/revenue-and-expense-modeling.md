---
last_updated: "2026-03-21"
---

## Revenue Modeling

### Foundation
Start with one of these approaches:
- **Company guidance** for public companies or clear analyst consensus
- **Your own analysis** if guidance is unavailable or unreliable
- **Historical trends + peer data** for private companies or going-private scenarios

### By Business Model

**Product Businesses (Volume x Price)**
```
Revenue = Unit Volume x Average Selling Price
- Model volume drivers: market demand, capacity, penetration rate
- Model pricing power: inflationary pressures, competitive dynamics
- Consider mix shift: premium vs. standard product skews both volume and ASP
```

**Subscription Businesses (Subscribers x ARPU)**
```
Revenue = Subscriber Count x Average Revenue Per User
- Model subscriber growth: new customer acquisition + churn
- Model ARPU expansion: price increases + upsell/cross-sell
- Cohort analysis: different vintage cohorts grow/contract at different rates
```

**Mixed or Organic + Acquisition**
```
Revenue = Organic Growth x (1 + Growth Rate) + Acquired Revenue
- Organic: assume stable growth rate or model customer-by-customer
- Acquisition: model purchase multiples, integration risk, retention
- Use historical add-on acquisition margins (often ~20-30% EBITDA initially)
```

**Segment-Level Build-Up**
When possible, model each major business segment separately:
- Different growth rates, margins, and working capital needs
- Easier to stress individual segments in downside scenarios
- Reveals concentration risk if one segment dominates

### Special Case: Going Private
- Company may stop issuing guidance; rely on:
  - Last 3-5 years of actual results (identify trends)
  - Peer company growth rates (same industry, similar size)
  - Management commentary if available
  - Market research on end-market growth
  - Conservative: use slower of historical or peer growth in base case

---

## Expense Modeling

### Cost of Goods Sold (COGS)
**Key principle: Gross Margin assumption**
```
COGS = Revenue x (1 - Gross Margin %)
```

- **Manufacturing/Product**: model material, labor, and manufacturing overhead
  - Material: unit cost x volume, or % of revenue
  - Labor: headcount growth aligned with volume growth
  - Overhead: semi-fixed, step with capacity
- **Service/Software**: mostly personnel + hosting/infrastructure
  - Personnel: per-customer or per-unit costs
  - Hosting: often scales with usage or customer count

**Margin expansion/compression**: In upside, margins typically expand (operating leverage). In downside, margins compress (fixed costs absorb lower revenue).

### SG&A (Selling, General & Administrative)
**Structure: some fixed + some variable**

Separate components when possible:
- **Sales & Marketing**: typically variable (% of revenue), scales with growth
- **G&A (corporate)**: largely fixed — salary, rent, insurance, professional fees
  - Rule of thumb: 5-10% of revenue in mature companies, 10-20% in growth-stage
- **Tech/Product Development**: semi-fixed; some leverages with scale, but core team is fixed

```
SG&A = Fixed Component + Variable Component (% of Revenue)
```

### Operating Leverage
- **Fixed costs**: rent, core management salaries, tech infrastructure create leverage
- **Variable costs**: commissions, packaging, delivery scale with revenue
- **Implication**: In upside cases, margins expand significantly. In downside, they compress if fixed costs are not reduced.

### One-Time Items
- **Exclude from run-rate**: restructuring charges, asset write-downs, litigation settlements
- **Model separately**: one-time synergies from acquisition, non-recurring debt paydown, tax benefits from NOLs
- **Pro forma adjustments**: add-back actual or expected one-time charges to normalize EBITDA

### Depreciation & Amortization (D&A)
```
D&A = Existing Asset Base x Depreciation Rate + New CapEx x Future Depreciation Rate
```

- **Fixed assets** (PP&E): useful life 5-40 years depending on asset type
- **Intangible assets** (goodwill, customer lists, other acquired intangibles): 5-20 years
- **Historical D&A**: typically 3-8% of revenue; use as check on forward projections
- **Link to CapEx**: increases in CapEx will drive D&A increases in future years

---
