---
last_updated: "2026-03-22"
---

# Thesis-Kill Trigger Standards

Thesis-kill triggers are the measurable conditions that would invalidate the investment thesis and require immediate reassessment or exit. Every approved investment must have at least three thesis-kill triggers defined before trade date. These triggers form the backbone of post-investment surveillance — without measurable triggers, monitoring degenerates into subjective opinion.

---

## Required Trigger Format

Every thesis-kill trigger must be documented using the following template. Triggers that cannot be expressed in this format are not sufficiently specific for surveillance purposes.

| Trigger | Measurable Threshold | Detection Method | Monitoring Frequency | Escalation Tier |
|---|---|---|---|---|
| [What could go wrong] | [Specific numeric or event threshold] | [How we will detect it] | [How often we check] | [Tier 1-4 per escalation framework] |

Each column is mandatory. A trigger missing any column is incomplete and must be revised before IC submission.

---

## Examples of Good Triggers

Good triggers are quantitative, measurable, and detectable through available data sources.

| Trigger | Measurable Threshold | Detection Method | Monitoring Frequency | Escalation Tier |
|---|---|---|---|---|
| Loss of top customer (>15% revenue) | >15% revenue customer announces switch or non-renewal | 10-Q revenue concentration disclosure, press releases, management commentary | Quarterly + real-time news monitoring | Tier 3 |
| Leverage exceeds 6.5x | Total Debt / EBITDA > 6.5x | Quarterly financial statements, compliance certificate | Quarterly | Tier 2 |
| Liquidity below $50M | Cash + undrawn revolver < $50M | Quarterly balance sheet + agent report | Quarterly, monthly if on watchlist | Tier 3 |
| EBITDA margin compression | EBITDA margin declines >400bps from underwriting base case | Quarterly income statement, segment reporting | Quarterly | Tier 2 |
| Loan price decline | Secondary market price declines >10 points from entry | Market data (LCD, Bloomberg) | Daily (automated alert) | Tier 2 |

---

## Examples of Bad Triggers (with Corrections)

Bad triggers use qualitative language that cannot be objectively measured or monitored. Each example below shows the bad trigger and its corrected version.

### Bad: "Sponsor dividend recap pre-deleveraging"

This trigger is unmeasurable — it does not define what constitutes "pre-deleveraging" or what size distribution is material.

**Corrected:**

| Trigger | Measurable Threshold | Detection Method | Monitoring Frequency | Escalation Tier |
|---|---|---|---|---|
| Sponsor-initiated distribution while levered | Sponsor dividend or distribution >$10M while Net Leverage >5.0x | Agent bank amendment notice, 8-K filing, quarterly compliance certificate | Quarterly + real-time alerts | Tier 3 |

### Bad: "Material deterioration in competitive position"

This trigger is purely qualitative — "material" and "competitive position" are undefined.

**Corrected:**

| Trigger | Measurable Threshold | Detection Method | Monitoring Frequency | Escalation Tier |
|---|---|---|---|---|
| Market share erosion | Market share loss >300bps over trailing 4 quarters per industry data | Industry reports (IBISWorld, Gartner), company 10-K competitive disclosures | Quarterly | Tier 2 |

### Bad: "Adverse regulatory change"

This trigger is too vague — nearly any regulation could be characterized as "adverse."

**Corrected:**

| Trigger | Measurable Threshold | Detection Method | Monitoring Frequency | Escalation Tier |
|---|---|---|---|---|
| Regulatory impact on addressable market or cost base | Final regulation published that reduces addressable market by >10% or increases compliance costs by >$20M annually | Federal Register, industry association alerts, company 8-K/10-Q risk factor updates | Real-time monitoring + quarterly review | Tier 2 |

---

## Common Trigger Patterns by Credit Type

### Corporate Credit

| Trigger Category | Typical Threshold | Notes |
|---|---|---|
| Leverage breach | Total Debt / EBITDA exceeds underwriting case + 1.0x turn | Calibrate to sector norms |
| Coverage deterioration | Interest coverage < 1.5x or FCF coverage < 1.0x | Liquidity-critical for cash-pay instruments |
| Customer concentration loss | Top customer (>10% revenue) lost or announces transition | Especially relevant for B2B industrials and services |
| Management turnover | >2 C-suite departures within 12 months | Invoke enhanced documentation risk assessment per CLAUDE.md handoff rules |
| Liquidity runway | <6 months of cash burn coverage | Tier 3 minimum |

### Commercial Real Estate

| Trigger Category | Typical Threshold | Notes |
|---|---|---|
| Occupancy decline | Physical or economic occupancy drops >15% from underwriting | Weight by tenant credit quality |
| DSCR breach | DSCR < 1.10x (stabilized) or < 1.00x (transitional) | Distinguish in-place vs. pro forma |
| Appraisal shortfall | Appraised value decline >20% from origination | LTV recalculation required |
| Major tenant non-renewal | Tenant representing >20% of NRI does not renew | Track lease expiration schedule |
| Cap rate expansion | Market cap rate widens >75bps from underwriting assumption | Monitor comparable sales |

### Private Credit

| Trigger Category | Typical Threshold | Notes |
|---|---|---|
| Covenant breach | Actual or anticipated breach of financial maintenance covenant | Private credit typically has tighter covenants than BSL |
| Revenue decline | Revenue decline >15% from trailing twelve months at underwriting | Earlier detection than leverage-based triggers |
| Sponsor support withdrawal | Sponsor declines to fund equity cure or support amendment | Behavioral signal — monitor sponsor communication |
| PIK toggle activation | PIK toggle exercised for >2 consecutive quarters | Cash flow stress indicator |
| Fair value markdown | Internal fair value marked down >10% from par | BDC and fund reporting trigger |

### Structured Finance

| Trigger Category | Typical Threshold | Notes |
|---|---|---|
| OC test cushion erosion | OC test cushion < 200bps | CLO-specific — triggers cash diversion risk |
| IC test breach | IC ratio falls below test threshold | Triggers interest diversion to senior tranches |
| Collateral quality deterioration | CCC bucket > 7.5% or WARF increase > 10% from closing | CLO portfolio quality metrics |
| Delinquency spike | 60+ day delinquencies > 2x historical average | ABS and RMBS pools |
| Servicer performance | Servicer placed on watchlist by rating agency | CMBS and ABS — operational risk |

---

## Integration with Surveillance Escalation Tiers

Thesis-kill triggers must map to the escalation tier framework defined in `references/escalation-trigger-thresholds.md`. The mapping determines the response speed and governance level when a trigger is breached.

| Escalation Tier | Response Time | Governance | Typical Trigger Severity |
|---|---|---|---|
| Tier 1 — Analyst Watch | Next scheduled review | Analyst discretion | Early warning indicators trending adversely but not yet at threshold |
| Tier 2 — Team Review | Within 5 business days | Team discussion, update surveillance memo | Thesis assumption under pressure, trigger approaching threshold |
| Tier 3 — IC Notification | Within 2 business days | Formal IC notification, recovery analysis initiated | Trigger breached, thesis materially impaired |
| Tier 4 — Emergency IC | Immediate (same business day) | Emergency IC convened, position action required | Payment default, bankruptcy, fraud, or multiple simultaneous trigger breaches |

When defining thesis-kill triggers for a new investment:

1. **Minimum 3 triggers required** — covering financial performance, structural/documentation risk, and sector/market conditions
2. **At least 1 trigger must be Tier 2 or lower** — providing early warning before thesis is fully broken
3. **At least 1 trigger must be Tier 3** — defining the point at which IC must be notified
4. **Each trigger must have a named data source** — if the data source is unavailable or unreliable, the trigger is ineffective
5. **Triggers must be independent** — correlated triggers (e.g., leverage breach and coverage breach driven by the same EBITDA decline) count as one trigger for minimum-count purposes
