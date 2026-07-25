---
name: Credit Surveillance Monitoring
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  This skill applies when monitoring an existing credit position after underwriting or approval. It covers thesis-based surveillance, early warning detection, watchlist and escalation governance, quarterly review workflow, asset-class-specific monitoring lenses, and post-mortem learning for corporate, private credit, CRE, and structured finance positions.
category: portfolio-management
related_skills:
  - portfolio-investment-process
  - modeling-and-valuation
  - events-distressed
  - memo-generator
  - industry-sector-analysis
  - debt-structure-covenants
triggers:
  - covenant compliance monitoring
  - credit deterioration
  - credit monitoring
  - credit surveillance
  - credit watch
  - downgrade risk
  - early warning
  - ongoing credit review
  - portfolio monitoring
  - post-investment monitoring
  - quarterly review
  - rating migration
  - refi risk monitoring
  - spread widening alert
  - surveillance report
  - watchlist
disambiguation: |
  Prefer this skill after a position has already been underwritten, approved, or purchased and the task is to monitor thesis drift, escalation triggers, or required actions.
  For initial underwriting, use the relevant domain skill first.
  For recovery, restructuring, workout, or default analysis, hand off to events-distressed.
---

# Credit Surveillance & Monitoring

Credit surveillance is thesis-based, not a full re-underwrite every cycle: start from the original investment case, test whether the key assumptions still hold, identify what changed, and escalate when deterioration becomes material or governance action is required.

## Core Workflow

1. **Restate the original thesis**: Identify the few assumptions that justified the investment and convert them into measurable monitoring points.
2. **Refresh core evidence**: Update financials, liquidity, covenant status, market signals, ratings, and material qualitative developments.
3. **Separate noise from thesis drift**: Distinguish temporary variance, cyclical pressure, technical market moves, and true structural deterioration.
4. **Classify status consistently**: Assign a surveillance color and governance tier using the current root threshold files rather than embedding local numbers.
5. **Escalate when required**: Link watchlist status, PM notification, IC governance, and downstream distressed work to the severity of the trigger.
6. **Recommend an action, not just a diagnosis**: Monitoring should end with a clear view on hold, reduce, hedge, exit, engage, or gather more information.
7. **Capture lessons**: If a name exits through stress, default, or a major thesis break, convert the outcome into a post-mortem and process improvement.

## Reference Map

Read the most relevant local reference for the question rather than loading the full library.

### Core Surveillance Framework
- `references/monitoring-framework.md` - Philosophy, surveillance scope, and portfolio-level framing.
- `references/early-warning-indicators.md` - Timeless categories of financial, market, qualitative, structural, and asset-class-specific warning signals.
- `references/escalation-framework.md` - Escalation tiers, governance chain, required documentation, condition tracking, de-escalation, and post-mortem linkage.

### Analytical Methodologies
- `references/quarterly-review-process.md` - Principle-based quarterly review workflow and report construction.
- `references/lme-early-warning.md` - LME precursor signals, documentation vulnerability review, and response framework.
- `references/rating-migration-tracking.md` - Rating action interpretation, downgrade leading indicators, and fallen-angel / rising-star workflow.
- `references/data-pipeline-methodology.md` - Data sourcing hierarchy, metric methodology, lineage, stale-data handling, and quality control.
- `references/portfolio-level-ic-review.md` - Rolling position-level surveillance into portfolio-level IC review.

### Asset-Class Lenses
- `references/asset-class-surveillance-lenses.md` - Corporate, CRE, private credit, and structured finance surveillance lenses.

### Tools and Operating Templates
- `references/surveillance-checklist.md` - Monitoring checklist by review depth and cadence.
- `references/watchlist-criteria.md` - Watchlist framing, category logic, and documentation expectations.
- `references/thesis-kill-trigger-standards.md` - Standards for turning investment theses into measurable monitoring triggers.
- `references/post-mortem-framework.md` - Structured review after credit events, losses, or near-misses.

## Interactive Wizard Workflow

If the user explicitly requests an "interactive review", "wizard", or "guided surveillance", or if they do not provide sufficient initial context to conduct a meaningful review, prompt them with the following interactive questionnaire *before* generating output:

1. **Review Scope**: "What is the review scope?"
   - Single credit name
   - Sector review
   - Full portfolio review

2. **Review Period**: "What is the review period?"
   - Quarterly (standard surveillance cycle)
   - Ad-hoc (triggered by specific event or concern)
   - Event-driven (M&A, downgrade, covenant breach, maturity approaching)

3. **Specific Concerns**: "Are there specific concerns or triggers to check?" (open text)

4. **Prior Reference**: "Is there a prior review to reference for comparison?"
   - Yes (ask for prior review date or reference)
   - No (first review or standalone)

Once these inputs are collected, proceed to the **Output Deliverables** workflow using the collected context to assess early warning indicators, classify status, and set next review dates.

## Output Deliverables

When asked to produce a surveillance review, quarterly update, watchlist memo, or escalation summary, produce:

1. **Source citations**: Explicitly cite every filing, transcript, rating action, market data source, and qualitative source used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Current status**: Surveillance color and governance tier, each with a one-line rationale.
3. **Thesis check**: What was the original thesis, what still holds, and what has changed.
4. **Key metric bridge**: Prior period, current period, and underwriting comparison for leverage, coverage, liquidity, covenant cushion, and market signals.
5. **Trigger assessment**: Which early warning indicators or thesis-kill triggers were approached or breached.
6. **Watchlist and escalation view**: Additions, removals, tier changes, and any required PM or IC action.
7. **Recommended action**: Hold, add, reduce, hedge, exit, engage, or gather more information, with rationale.
8. **Forward monitoring plan**: Next review date, pending catalysts, and the few things that would change the recommendation.

## Limitations

- Surveillance is partly lagging by construction because financial statements and compliance certificates arrive after performance has already moved.
- Market signals can lead fundamentals, but they can also reflect technical flow, illiquidity, or broader risk-off moves rather than issuer-specific deterioration.
- Ratings are useful external signals but usually confirm deterioration later than the market.
- Rule-based escalation frameworks improve consistency but cannot capture every idiosyncratic risk; analyst judgment still matters.

## Data Quality

- Never silently fill missing data with assumptions. If reporting is incomplete, delayed, or unreliable, use `skills/memo-generator/references/incomplete-data-guidance.md` and state the gap explicitly.
- Use local references for methodology and root references for current cutoffs. Do not restate mutable thresholds from memory.
- Keep underwriting assumptions, current actuals, and stress-case assumptions separate; blending them hides thesis drift.
- When a standard surveillance framework is unreliable for a given structure or event, consult `skills/memo-generator/references/analytical-limitations.md` and disclose the limitation directly.

## Examples

- `examples/worked-quarterly-review-escalation-example.md`: Multi-period surveillance example showing thesis drift, watchlist escalation, and IC notification.
