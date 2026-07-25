# Agents

This repository is multi-harness. For Codex, this `AGENTS.md` file is the primary repository instruction entrypoint. It summarizes the routing, orchestration, and default behavior rules that Codex should follow before loading the underlying agent and skill files.

Professional credit analysis toolkit for asset managers and institutional investors. The repository provides 14 domain skills plus 2 agents covering leveraged finance, private credit, commercial real estate, structured finance, portfolio management, and credit surveillance.

## Codex Routing Guide

### Reference Material Layout

Use these path rules consistently:

- Root reference files live under `references/`.
- Skill-local references live under `skills/<skill-name>/references/`.
- Cross-skill references should use explicit project-root paths such as `skills/<owner-skill>/references/foo.md`.
- Do not treat bare `references/foo.md` as a skill-local path; use it for project-root references only when written explicitly as `references/foo.md`.

### Skill Selection

When the request maps to a single domain, use the matching skill. When it spans multiple domains, sequence multiple skills in the order required by the workflow.

Routing hints for ambiguous terms:

| Term | Corporate context | CRE context | Structured Finance context |
|---|---|---|---|
| DSCR | `modeling-and-valuation` | `cre-analysis-underwriting` | `specialized-asset-finance` or `securitization-and-clos` |
| Leverage | `modeling-and-valuation` | `cre-analysis-underwriting` (LTV) | `securitization-and-clos` (OC tests) |
| Coverage | `modeling-and-valuation` | `cre-analysis-underwriting` | `securitization-and-clos` (OC/IC tests) |
| Recovery | `events-distressed` | `cre-analysis-underwriting` | `securitization-and-clos` |
| Spread | `trading-pricing-mechanics` | `cre-analysis-underwriting` (cap rate) | `securitization-and-clos` |
| Covenant | `debt-structure-covenants` | `cre-analysis-underwriting` | `specialized-asset-finance` |

Use the user's context to disambiguate:

- property type -> CRE
- SPV or tranche -> structured finance
- company or issuer -> corporate credit

### Core Workflows

Corporate new investment review:

1. `industry-sector-analysis`
2. `modeling-and-valuation`
3. `debt-structure-covenants`
4. `trading-pricing-mechanics`
5. `due-diligence-and-assessment`
6. `portfolio-investment-process`
7. `memo-generator`

Private credit new investment review:

1. `industry-sector-analysis`
2. `private-credit-middle-market`
3. `modeling-and-valuation`
4. `debt-structure-covenants`
5. `due-diligence-and-assessment`
6. `portfolio-investment-process`
7. `memo-generator`

CRE new investment review:

1. `cre-analysis-underwriting`
2. `modeling-and-valuation`
3. `debt-structure-covenants`
4. `portfolio-investment-process`
5. `memo-generator`

Structured finance new investment review:

1. `securitization-and-clos` or `specialized-asset-finance`
2. `modeling-and-valuation`
3. `trading-pricing-mechanics`
4. `portfolio-investment-process`
5. `memo-generator`

Distressed or special situations:

1. `industry-sector-analysis`
2. `events-distressed`
3. `modeling-and-valuation`
4. `debt-structure-covenants`
5. `trading-pricing-mechanics`

Ongoing surveillance:

1. `industry-sector-analysis`
2. `surveillance-monitoring`
3. `modeling-and-valuation`
4. `portfolio-investment-process`

IC challenge after memo:

1. `credit-committee` agent
2. `portfolio-investment-process`
3. `surveillance-monitoring`

### Cross-Skill Escalations

- If `surveillance-monitoring` reaches Tier 3 or Red, invoke `events-distressed`.
- If `debt-structure-covenants` identifies silent debt capacity above 2.0x turns, flag elevated structural risk in `portfolio-investment-process`.
- If `industry-sector-analysis` identifies cyclical decline, `modeling-and-valuation` must add a sector-stress scenario using `references/stress-scenario-framework.md`.
- If `private-credit-middle-market` completes underwriting, map thesis-kill triggers into `surveillance-monitoring`.
- If `due-diligence-and-assessment` finds management turnover, sponsor red flags, or unresolved diligence gaps, escalate that risk into documentation analysis and keep the recommendation conditional if the gap is still unresolved.
- If `memo-generator` reveals imminent default or restructuring signals, invoke `events-distressed` before finalizing the memo.
- If `modeling-and-valuation` produces a distress probability score at or above 3.0, apply the correlation-adjusted sizing framework in `skills/portfolio-investment-process/references/correlation-adjusted-position-sizing.md`.
- If `cre-analysis-underwriting`, `debt-structure-covenants`, or `trading-pricing-mechanics` reveal restructuring-driven impairment, escalate to both `events-distressed` and `surveillance-monitoring`.

### Default Behaviors

- Cite every data point, benchmark, and qualitative assertion.
- When a stable direct URL exists, include it inline with the citation and keep locator detail in the same citation.
- Prefer canonical primary-source URLs over search-result or aggregator links.
- Use structured outputs: tables for comparisons, bullets for risks and mitigants, and clear headers for sections.
- Never silently fill missing data with assumptions. Use `skills/memo-generator/references/incomplete-data-guidance.md`.
- Before finalizing multi-skill analysis, run `skills/memo-generator/references/cross-skill-validation-checklist.md`.

Read these root references before discussing their topics:

- Current market conditions, pricing, or spreads -> `references/market-benchmarks.md`
- Default or recovery rates -> `references/default-recovery-rates.md`
- Rating thresholds or rating actions -> `references/rating-agency-thresholds.md`
- Deal terms or market conventions -> `references/typical-deal-parameters.md`
- Private credit performance -> `references/private-credit-performance.md`
- Covenant trends or documentation risk -> `references/credit-agreement-trends-documentation-risk.md`
- Position sizing, risk limits, or concentration limits -> `references/portfolio-risk-parameters.md`
- Escalation triggers or watchlist criteria -> `references/escalation-trigger-thresholds.md`
- BDC regulations or BDC-specific private credit constraints -> `skills/private-credit-middle-market/references/bdc-regulatory.md`
- Stress testing or scenario analysis -> `references/stress-scenario-framework.md`

## Agents

This plugin includes two agents that support credit underwriting and Investment Committee governance.

---

## credit-analyst

**File:** `agents/credit-analyst.agent.md`

An autonomous credit analyst persona that orchestrates the end-to-end IC memo workflow. It sequences the domain skills by asset class, assembles the memo, performs a pre-IC self-challenge, and prepares a recommendation that is ready for committee review.

### When to Use

- When a user wants a full IC memo or credit write-up produced autonomously
- When the workflow spans multiple skills and needs disciplined sequencing
- Before handing a draft memo to `credit-committee` for challenge

### Expected Inputs

- Issuer or deal name
- Credit type or asset class context
- Available source materials such as filings, credit documents, management materials, or market references

### Expected Outputs

- Structured IC memo assembled using `memo-generator`
- Phase-gate notes across the analysis workflow
- Pre-IC self-assessment covering thesis vulnerabilities, recommendation breakpoints, and confidence calibration

### Skill References

The agent follows the workflow order documented in `CLAUDE.md`, invoking the relevant domain skills by credit type before assembling the final memo.

## credit-committee

**File:** `agents/credit-committee.agent.md`

A highly skeptical Credit Committee member persona designed to identify downside risks, structural flaws in debt, and covenant loopholes. Produces structured IC challenge responses with explicit pass/decline decisions, conditions, and monitoring requirements.

### When to Use

- After an IC credit memo is assembled (via `memo-generator`)
- For ad-hoc IC review when a Tier 3+ escalation trigger is breached
- To stress-test an investment thesis before committing capital

### Expected Inputs

- A completed or draft IC credit memo
- Specific investment thesis or recommendation to challenge
- Financial model outputs and scenario analysis

### Expected Outputs

- Structured IC challenge response with:
  - At least 3 critical weaknesses or unanswered questions
  - Explicit pass/conditional-pass/decline decision
  - Conditions for approval (if conditional pass)
  - Required monitoring triggers and review timeline
  - Requests for additional sensitivity analysis

### Skill References

The agent invokes domain skills when challenging each dimension:

| Challenge Dimension | Skill | Focus |
|---|---|---|
| Financial Rigor | `modeling-and-valuation` | Add-back justification, FCF conversion, model breakpoints |
| Documentation & Structure | `debt-structure-covenants` | Silent debt capacity, basket leakage, LME vulnerability |
| Relative Value | `trading-pricing-mechanics` | Spread adequacy, alternative investments, comp analysis |
| Sector / Cyclical Risk | `industry-sector-analysis` | Downturn scenarios, cycle positioning, secular headwinds |
| Management / Sponsor | `due-diligence-and-assessment` | Alignment, track record, distressed behavior patterns |
| Post-Approval Monitoring | `surveillance-monitoring` | Early warning triggers, review cadence, escalation thresholds |

## Skill Directory

| Skill | Domain | Use For |
|---|---|---|
| `modeling-and-valuation` | Corporate Credit | Financial spreading, EBITDA, FCF, ratios, scenarios, projections, DCF, comps, LBO modeling |
| `debt-structure-covenants` | Corporate Credit | Capital structure, covenants, documentation, intercreditor, refinancing risk analysis |
| `trading-pricing-mechanics` | Markets | Loan and bond pricing, spreads, relative value, settlement |
| `events-distressed` | Special Situations | Bankruptcy, restructuring, LMEs, recovery analysis, DIP financing, post-restructuring monitoring |
| `portfolio-investment-process` | Portfolio Management | Investment process, risk limits, hedging, position sizing, stress testing |
| `surveillance-monitoring` | Portfolio Management | Ongoing monitoring, early warnings, watchlists, quarterly reviews, escalation, and rating migration tracking |
| `leveraged-finance-glossary` | Reference | Leveraged-finance terminology and market-mechanics orientation |
| `private-credit-middle-market` | Private Credit | Direct lending, unitranche, BDCs, PIK mechanics, NAV lending, amendment and waiver analysis |
| `cre-analysis-underwriting` | Real Estate | Property analysis, CRE valuation, and loan sizing |
| `securitization-and-clos` | Structured Finance | CLOs, ABS, RMBS, CMBS, waterfalls, coverage tests, and servicer evaluation |
| `specialized-asset-finance` | Structured Finance | Project finance, ABL, equipment finance, aircraft, shipping, leasing, and debt sculpting |
| `memo-generator` | Workflow | Multi-skill orchestration into structured IC memos |
| `industry-sector-analysis` | Sector Analysis | Industry-specific frameworks and sector-adjusted credit risk analysis |
| `due-diligence-and-assessment` | Due Diligence | Management, sponsor, ESG, and data-room quality assessment |

For broader cross-harness packaging notes, see `README.md`, `docs/harness-compatibility.md`, and `CLAUDE.md`.
