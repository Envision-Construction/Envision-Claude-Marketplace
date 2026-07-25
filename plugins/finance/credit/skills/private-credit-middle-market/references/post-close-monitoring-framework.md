---
last_updated: "2026-03-22"
---

## Private Credit Post-Close Monitoring Framework

This framework provides a structured approach to monitoring private credit positions from funding through exit. It complements the broader surveillance framework in the `surveillance-monitoring` skill with private credit-specific workflows.

### Phase 1: First 90 Days Post-Close

**Objective:** Validate deployment assumptions and establish monitoring baseline.

| Activity | Timeline | Deliverable |
|---|---|---|
| Confirm financial reporting cadence | Week 1 | Documented reporting schedule |
| Validate first compliance certificate | Day 45 | Covenant baseline comparison |
| Verify board observer access | First board meeting | Confirm materials received |
| Establish covenant baseline | Day 45 | Baseline spreadsheet with actuals vs. model |
| Validate deployment use-of-proceeds | Day 30 | Funds flow confirmation |
| First revenue flash review | Day 30 | Revenue vs. model comparison |

**Key Question:** Does the first quarter's performance validate the underwriting assumptions? Investigate any miss that breaches the position's agreed monitoring tolerances or the repo-wide escalation standards in `references/escalation-trigger-thresholds.md`.

### Phase 2: Quarterly Review (Ongoing)

**Standard Quarterly Review Checklist:**

1. **Financial Performance vs. Model:**
   - Revenue actual vs. model (compare to the position's monitoring tolerances)
   - EBITDA actual vs. model (compare to the position's monitoring tolerances)
   - CapEx vs. budget (over/under-investment risk)
   - Working capital changes (cash conversion cycle trend)

2. **Covenant Compliance:**
   - Current leverage vs. covenant limit and headroom %
   - FCCR vs. minimum and trend
   - Addback analysis: are addbacks growing as % of EBITDA? (creep = red flag)
   - Forward projection: will covenants be met next 2 quarters?

3. **Sponsor Engagement Quality:**
   - Board meeting cadence maintained?
   - Management reporting on time and complete?
   - Sponsor responsiveness to lender inquiries
   - Any amendment/waiver discussions?

4. **Market Context:**
   - Industry/sector developments affecting borrower
   - Comparable public company performance (if applicable)
   - Rate environment impact on coverage

### Phase 3: Annual Review

**Full Credit Update (Annual):**

| Component | Scope | Reference Skill |
|---|---|---|
| Financial model update | Full re-spread with LTM actuals, refresh projections | `modeling-and-valuation` |
| Fair value reassessment | Mark-to-market using current market data | Internal valuation methodology |
| Thesis re-validation | Do original investment thesis drivers still hold? | Original IC memo |
| Covenant capacity analysis | Forward leverage/coverage with updated projections | `debt-structure-covenants` |
| Sponsor assessment update | Fund lifecycle, portfolio company performance | `due-diligence-and-assessment` |
| Surveillance classification | Green/Yellow/Orange/Red based on cumulative indicators | `surveillance-monitoring` |

### Phase 4: Event-Driven Reviews

Trigger an ad-hoc review (outside quarterly cadence) when:

| Event | Required Actions |
|---|---|
| M&A by borrower (add-on acquisition) | Re-underwrite pro forma leverage; assess integration risk; review incremental debt capacity |
| Management change (CEO/CFO) | Assess new management capability; review compensation alignment; update management scorecard |
| Sponsor fund lifecycle event | Assess follow-on capacity; evaluate exit timeline pressure; monitor for extractive behavior |
| Amendment/waiver request | Full covenant analysis; assess if structural or temporary; negotiate fee and tightening |
| Material litigation | Quantify exposure vs. enterprise value; assess insurance coverage; evaluate business impact |
| Regulatory change | Assess revenue/margin impact; update scenario analysis; review covenant adequacy |

### Cross-Reference: Escalation Governance

For escalation tiers, response times, and governance process, reference:
- `surveillance-monitoring` skill — monitoring framework and escalation tiers
- `references/escalation-trigger-thresholds.md` — numeric thresholds for each tier
- `credit-committee` agent — IC notification and emergency review process
