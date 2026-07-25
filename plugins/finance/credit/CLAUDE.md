# Credit Investment Analysis Plugin

Professional credit analysis toolkit for asset managers and institutional investors. 14 skills covering leveraged finance, private credit, CRE, structured finance, portfolio management, and credit surveillance.

## How This Plugin Works

### Two types of reference material

1. **Root `/references/`** — Shared root reference files hold reusable benchmarks, market inputs, deal-parameter guides, documentation trend notes, and other cross-skill reference material. Always consult `references/market-benchmarks.md` when discussing current pricing, spreads, or market conditions.

2. **Skill-level `references/`** — Domain knowledge (concepts, methodologies, checklists, templates) stored flat in each skill's `references/` directory.

### Path Resolution

Use these path rules consistently:

- Root reference files use explicit project-root paths such as `references/market-benchmarks.md` and `references/typical-deal-parameters.md`.
- Skill-local references use paths relative to the owning skill, so `references/foo.md` means `<project-root>/skills/<skill-name>/references/foo.md`.
- Cross-skill references use explicit project-root paths such as `skills/<owner-skill>/references/foo.md`.

Do not treat bare `references/foo.md` as a skill-local path; within this repository it refers to a project-root file only when written as an explicit project-root path like `references/foo.md`.

### Skill Selection

When the user's request maps to a single domain, use that skill. When a request spans multiple domains (common for real analysis), use multiple skills in sequence.

**Routing hints for ambiguous terms:**

| Term | Corporate context | CRE context | Structured Finance context |
|---|---|---|---|
| DSCR | `modeling-and-valuation` | `cre-analysis-underwriting` | `specialized-asset-finance` (project finance) or `securitization-and-clos` |
| Leverage | `modeling-and-valuation` | `cre-analysis-underwriting` (LTV) | `securitization-and-clos` (OC tests) |
| Coverage | `modeling-and-valuation` | `cre-analysis-underwriting` | `securitization-and-clos` (OC/IC tests) |
| Recovery | `events-distressed` | `cre-analysis-underwriting` | `securitization-and-clos` |
| Spread | `trading-pricing-mechanics` | `cre-analysis-underwriting` (cap rate) | `securitization-and-clos` |
| Covenant | `debt-structure-covenants` | `cre-analysis-underwriting` | `specialized-asset-finance` (project finance) |

Use the user's context (property type → CRE, SPV/tranche → structured, company/issuer → corporate) to disambiguate.

### Orchestration for Common Workflows

**New investment review (corporate credit):**
1. `industry-sector-analysis` — Understand sector dynamics and key metrics
2. `modeling-and-valuation` — Spread financials, build projections, run scenarios
3. `debt-structure-covenants` — Map capital structure, analyze documentation
4. `trading-pricing-mechanics` — Relative value, pricing, comp analysis
5. `due-diligence-and-assessment` — Evaluate management team, sponsor, ESG (if PE-backed)
6. `portfolio-investment-process` — Position sizing, risk limits, investment decision
7. `memo-generator` — Assemble findings into structured IC memo

**New investment review (CRE):**
1. `cre-analysis-underwriting` — Property analysis, valuation, loan sizing
2. `modeling-and-valuation` — Pro forma cash flows, scenario analysis
3. `debt-structure-covenants` — CRE loan terms, cash management
4. `portfolio-investment-process` — Position sizing, concentration limits by property type
5. `memo-generator` — Assemble into CRE credit memo

**New investment review (structured finance):**
1. Relevant sector skill (`securitization-and-clos` for CLO/ABS/RMBS/CMBS, or `specialized-asset-finance` for project finance/ABL/leasing)
2. `modeling-and-valuation` — Cash flow modeling, scenario analysis
3. `trading-pricing-mechanics` — Pricing, relative value
4. `portfolio-investment-process` — Position sizing, mandate compliance, and portfolio fit
5. `memo-generator` — Assemble into structured credit memo

**New investment review (private credit):**
1. `industry-sector-analysis` — Understand sector dynamics and key metrics (same frameworks apply to BSL, HY, and private credit)
2. `private-credit-middle-market` — Direct lending structure, unitranche mechanics, BDC considerations
3. `modeling-and-valuation` — Spread financials, build projections, run scenarios
4. `debt-structure-covenants` — Analyze credit agreement, covenant protections
5. `due-diligence-and-assessment` — Sponsor evaluation, management assessment, ESG (if applicable)
6. `portfolio-investment-process` — Position sizing, mandate compliance, risk limits
7. `memo-generator` — Assemble into private credit IC memo

**Distressed / special situations:**
1. `industry-sector-analysis` — Sector context for distress drivers and recovery comps
2. `events-distressed` — Identify situation type, recovery framework
3. `modeling-and-valuation` — Liquidity analysis, enterprise valuation
4. `debt-structure-covenants` — Documentation review for LME exposure
5. `trading-pricing-mechanics` — Distressed trading mechanics

**Ongoing surveillance:**
1. `industry-sector-analysis` — Check for sector-level changes affecting monitored credits
2. `surveillance-monitoring` — Quarterly review, early warning check
3. `modeling-and-valuation` — Update model with new financials
4. `portfolio-investment-process` — Portfolio-level risk assessment

**IC challenge (post-memo):**
1. `credit-committee` agent — Structured challenge, risk identification, conditions
2. `portfolio-investment-process` — Mandate compliance check, position sizing validation
3. `surveillance-monitoring` — Set up monitoring framework, map thesis-kill triggers to escalation tiers

**Escalation (during holding period):**
1. `surveillance-monitoring` — Detect early warning, classify escalation tier
2. `modeling-and-valuation` — Update model with new data
3. `credit-committee` agent — Ad-hoc IC review if Tier 3+ trigger breached
4. `portfolio-investment-process` — Reassess position, hedge, or exit decision

**Post-IC through Trade Settlement:**
1. `credit-committee` agent — IC decision with conditions, dissent records, portfolio impact metrics
2. `surveillance-monitoring` — Condition monitoring handoff, initial surveillance parameter setup, thesis-kill trigger mapping
3. `portfolio-investment-process` — Final position sizing confirmation, trade execution parameters, risk system entry
4. `trading-pricing-mechanics` — Execution strategy, settlement mechanics

**Portfolio review (monthly/quarterly):**
1. `surveillance-monitoring` — Roll up position-level surveillance, compile watchlist changes
2. `portfolio-investment-process` — Concentration analysis, risk metrics, stress test results
3. `credit-committee` agent — IC-level portfolio discussion, strategic allocation decisions

### Cross-Skill Handoff Rules

This CLAUDE.md section is the single authoritative source for all cross-skill handoff rules. Individual skills do not carry their own handoff sections.

These rules define automatic escalation between skills based on analytical findings:

**Surveillance → Distressed:**
- When `surveillance-monitoring` classifies a credit as Tier 3 (IC Notification) or Red, automatically invoke `events-distressed` for recovery analysis
- Trigger: EBITDA decline >20% LTM, leverage increase >1.0x, liquidity runway <6 months, or loan price decline >10 points

**Covenant Analysis → Portfolio Risk:**
- When `debt-structure-covenants` identifies silent debt capacity >2.0x turns, flag in `portfolio-investment-process` position sizing as elevated structural risk
- Impact: Reduce maximum position size by 25% or require additional IC condition

**Sector Analysis → Credit Modeling:**
- When `industry-sector-analysis` identifies sector entering cyclical decline (declining order books, rising inventory, margin compression across peers), `modeling-and-valuation` must add a sector-stress scenario (apply sector-specific downside from `references/stress-scenario-framework.md`)

**Surveillance → Portfolio:**
- When `surveillance-monitoring` escalates any position to Tier 3+, `portfolio-investment-process` must reassess portfolio concentration impact: does forced exit or hedging of this position breach other risk limits?

**Private Credit → Surveillance:**
- When `private-credit-middle-market` completes an underwriting, automatically map thesis-kill triggers to `surveillance-monitoring` escalation tiers. Every approved private credit position must have a monitoring handoff before trade date.

**Due Diligence → Covenants:**
- When `due-diligence-and-assessment` identifies management turnover >2 C-suite changes in 12 months or sponsor behavioral red flags (dividend recap within 18 months), `debt-structure-covenants` analysis must include enhanced documentation risk assessment with specific focus on restricted payment baskets and sponsor value extraction mechanisms.

**Securitization → Portfolio:**
- When `securitization-and-clos` identifies OC test cushion declining below 200bps or IC test cushion below 50bps, flag in `portfolio-investment-process` for portfolio impact assessment

**Project Finance → Surveillance:**
- When `specialized-asset-finance` identifies DSCR breach below 1.0x, escalate to `surveillance-monitoring` Tier 3

**Memo Generator → Distressed:**
- When `memo-generator` analysis reveals imminent default/restructuring signals during memo assembly (EBITDA interest coverage <1.0x, liquidity runway <3 months, loan price <80, or Red/Tier 4 classification), invoke `events-distressed` before completing memo

**Distress Probability → Portfolio:**
- When `modeling-and-valuation` distress probability framework composite score is at or above 3.0 (Elevated), `portfolio-investment-process` must apply correlation-adjusted position sizing per `skills/portfolio-investment-process/references/correlation-adjusted-position-sizing.md` and reduce maximum position size proportionally to the distress score

**ESG Findings → Scenario Analysis:**
- When `due-diligence-and-assessment` identifies material ESG risks (environmental fines, climate exposure, governance deficiencies), `modeling-and-valuation` must integrate these findings into scenario analysis per `skills/modeling-and-valuation/references/esg-scenario-integration.md` — ESG factors modify existing scenario probabilities rather than creating separate ESG-only scenarios

**CRE → Surveillance/Distressed:**
- When `cre-analysis-underwriting` finds refinance proceeds appear insufficient, recurring DSCR trends below 1.0x, or occupancy/tenancy loss makes repayment depend on asset sale/amendment/sponsor cure capital, hand off to `surveillance-monitoring` for escalation framing and `events-distressed` if recovery/restructuring analysis is required

**Covenant Documentation → Distressed:**
- When `debt-structure-covenants` identifies restructuring-sensitive documentation risk (repeated amendments, high LME vulnerability, or near-term maturities with weak refinancing path), escalate to `events-distressed` and `surveillance-monitoring`

**Trading Dislocation → Distressed:**
- When `trading-pricing-mechanics` identifies price decline, spread move, or settlement friction driven by impending default/restructuring rather than technicals, escalate to `events-distressed` and `surveillance-monitoring`

**Due Diligence → Conditional Recommendation:**
- When `due-diligence-and-assessment` finds material diligence gaps remain unresolved (missing QoE, absent recent financials, missing draft debt documents, or unresolved litigation/environmental exposure), recommendation must remain conditional or defer commitment until the gap is resolved

### Default Behaviors

- **Source Citations:** The assistant MUST explicitly cite sources for all data, metrics, and qualitative information provided (e.g., website URLs, 10-K page numbers, company presentation slides, data providers).
- When a stable direct URL exists, include that URL inline with the citation so source links remain available for downstream collection into a consolidated appendix.
- Keep locator detail with the same citation when available (for example: filing page number, slide number, report date, or access date).
- Prefer canonical primary-source URLs over search-result links or secondary aggregators. If no stable URL exists, keep the citation without inventing a link.
- When discussing **current market conditions, pricing, or spreads**, always read `references/market-benchmarks.md` first
- When discussing **default or recovery rates**, always read `references/default-recovery-rates.md` first
- When discussing **rating thresholds or rating actions**, always read `references/rating-agency-thresholds.md` first
- When discussing **deal terms or market conventions**, always read `references/typical-deal-parameters.md` first
- When discussing **private credit performance**, always read `references/private-credit-performance.md` first
- When discussing **covenant trends or documentation risk**, always read `references/credit-agreement-trends-documentation-risk.md` first
- When discussing **portfolio risk limits, position sizing, or concentration limits**, always read `references/portfolio-risk-parameters.md` first
- When discussing **escalation triggers, surveillance thresholds, or watchlist criteria**, always read `references/escalation-trigger-thresholds.md` first
- When discussing **BDC regulations or BDC-specific private credit constraints**, always read `skills/private-credit-middle-market/references/bdc-regulatory.md` first
- When discussing **private debt performance benchmarks, portfolio KPIs, or private credit performance**, always read `references/private-credit-performance.md` first
- When performing **stress testing or scenario analysis**, always read `references/stress-scenario-framework.md` first for asset-class-specific stress parameters
- When producing analysis, use structured formats: tables for comparisons, bullet lists for risks/mitigants, clear headers for sections
- **Data Freshness:** Root reference files include `last_updated`, `update_cadence`, and `next_review` YAML frontmatter. Before citing market data, check these fields. If the current date exceeds `next_review`, warn the user that the reference data may be stale and should be verified against current market conditions.
- When **data is incomplete or unavailable**, consult `skills/memo-generator/references/incomplete-data-guidance.md` for how to flag gaps transparently — never silently fill gaps with assumptions
- When applying **standard analytical frameworks** (EBITDA leverage, cap rate valuation, OC tests, comps), consult `skills/memo-generator/references/analytical-limitations.md` to identify when the framework may produce unreliable results — disclose limitations proactively rather than presenting framework outputs as authoritative
- When comparing investments **across asset classes** (e.g., loan vs. CLO tranche vs. CRE debt vs. private credit), read `skills/portfolio-investment-process/references/cross-asset-relative-value-framework.md` for the normalization framework and `references/cross-asset-relative-value.md` for current benchmark inputs
- When completing **multi-skill analysis**, run `skills/memo-generator/references/cross-skill-validation-checklist.md` before finalizing output
- When IC produces a **Conditional Pass**, the condition monitoring handoff block must map each condition to a `surveillance-monitoring` escalation tier with deadline and verification method
- When IC decision includes **dissent**, produce dissent register entry per `skills/portfolio-investment-process/references/ic-governance-framework.md`
- When discussing **monitoring data sources, measurement methodology, or data pipelines**, read `skills/surveillance-monitoring/references/data-pipeline-methodology.md` for sourcing and calculation method, and `references/data-pipeline-specification.md` for current cadence, escalation, and tolerance parameters
- When defining or evaluating **thesis-kill triggers**, always read `skills/surveillance-monitoring/references/thesis-kill-trigger-standards.md` first — every trigger must have a measurable threshold, detection method, monitoring frequency, and escalation tier mapping
- When analyzing **companies with significant real estate holdings** or comparing CRE and corporate credit for the same borrower, always read `skills/modeling-and-valuation/references/cre-corporate-bridge-framework.md` first for the integration framework
- When evaluating **post-investment actions** (covenant amendments, add-ons, position increases, dividend recaps), consult the materiality thresholds in `skills/portfolio-investment-process/references/ic-governance-framework.md` Section 9 to determine the required governance level (PM authority vs. IC notification vs. full IC)

## Skill Directory

| Skill | Domain | Use For |
|---|---|---|
| `modeling-and-valuation` | Corporate Credit | Financial spreading, EBITDA, FCF, ratios, scenarios, projections, DCF, comps, LBO modeling |
| `debt-structure-covenants` | Corporate Credit | Capital structure, covenants, documentation, intercreditor, refinancing risk analysis |
| `trading-pricing-mechanics` | Markets | Loan/bond pricing, spreads, relative value, settlement |
| `events-distressed` | Special Situations | Bankruptcy, restructuring, LMEs, recovery analysis, DIP financing, post-restructuring monitoring |
| `portfolio-investment-process` | Portfolio Management | Investment process, risk limits, hedging, position sizing, stress testing |
| `surveillance-monitoring` | Portfolio Management | Ongoing monitoring, early warnings, watchlists, quarterly reviews, escalation, LME early warning, rating migration tracking |
| `leveraged-finance-glossary` | Reference | Leveraged-finance terminology, bond and loan mechanics, capital structure language, and syndication orientation |
| `private-credit-middle-market` | Private Credit | Direct lending, unitranche, BDCs, fund structures, PIK mechanics, NAV lending, amendment/waiver analysis |
| `cre-analysis-underwriting` | Real Estate | Property analysis, CRE valuation, loan sizing |
| `securitization-and-clos` | Structured Finance | CLO structure/equity/tranches, ABS, RMBS, CMBS, tranching, prepayment, waterfalls, OAS methodology, servicer evaluation |
| `specialized-asset-finance` | Structured Finance | Project finance, ABL, equipment finance, aircraft, shipping, leasing, debt sculpting |
| `memo-generator` | Workflow | Orchestrates other skills into structured IC memos |
| `industry-sector-analysis` | Sector Analysis | Industry-specific credit frameworks and metrics, technology sub-sector frameworks (SaaS, semiconductors, IT services) |
| `due-diligence-and-assessment` | Due Diligence | Management/sponsor evaluation, ESG/SLL, data room review, document checklists |
