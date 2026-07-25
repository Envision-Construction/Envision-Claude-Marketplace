---
name: Credit Events Distressed
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  This skill applies when analyzing bankruptcy, restructuring, liability management exercises, recovery value, or event-driven credit situations where a transaction or legal process can materially change downside, priority, or repayment outcomes.
category: special-situations
related_skills:
  - cre-analysis-underwriting
  - memo-generator
  - modeling-and-valuation
  - surveillance-monitoring
  - debt-structure-covenants
  - industry-sector-analysis
  - trading-pricing-mechanics
triggers:
  - distressed credit
  - restructuring
  - bankruptcy
  - Chapter 11
  - recovery analysis
  - liability management exercise
  - LME
  - DIP financing
  - fulcrum security
  - event-driven credit
  - M&A impact on bonds
  - change of control
  - refinancing risk
  - loan-to-own
  - special situations
disambiguation: |
  Prefer this skill when a transaction, capital structure change, legal process, or distress dynamic can alter recovery, priority, or downside outcomes.
  For pre-distress monitoring and watchlist escalation, use surveillance-monitoring.
  For covenant interpretation and basket analysis, use debt-structure-covenants.
  For property-level workout and collateral analysis in CRE, pair with cre-analysis-underwriting.
---

# Special Situations & Distressed Credit

Special situations credit work is downside-first and process-aware: identify the trigger, map the legal and structural consequences, determine who controls value, and only then translate that into recovery, risk/reward, and portfolio action.

## Core Workflow

1. **Classify the situation**: Distinguish event-driven, liquidity-driven, documentation-driven, and formal restructuring situations before jumping into valuation.
2. **Map the legal and structural position**: Identify claim priority, lien package, guarantees, entity structure, covenant flex, and any mechanisms that can subordinate or prime existing creditors.
3. **Determine timing pressure**: Build a liquidity runway and maturity wall view to understand whether the company has negotiating time or is approaching a forced process.
4. **Frame the resolution set**: Compare amend-and-extend, exchange, LME, prepack, freefall Chapter 11, asset sale, or liquidation based on feasibility rather than preference.
5. **Value the business or collateral conservatively**: Use enterprise value, asset value, or collateral value consistent with the actual resolution path.
6. **Run the recovery waterfall**: Deduct administrative claims, DIP effects, and senior claims before assigning value to the fulcrum and junior classes.
7. **Translate into an investor view**: Summarize catalysts, path dependency, probability-weighted outcomes, and where the market price implies a different view from the underwriting.

## Reference Map

Read the most relevant reference for the question at hand rather than loading the full library.

### Core Restructuring Concepts
- `references/bankruptcy-legal-framework.md` - U.S. bankruptcy fundamentals: Chapter 7 vs. Chapter 11, claim definitions, class formation, voting, blocking positions, cramdown, and subordination.
- `references/modern-restructuring-pathways.md` - Compare out-of-court, prepack, pre-arranged, and freefall paths.
- `references/liability-management-exercises-lmes.md` - LME types, documentary vulnerabilities, and creditor positioning.
- `references/dip-financing-framework.md` - DIP types, lender protections, and recovery impact.

### Analytical Frameworks
- `references/distress-diagnosis-and-liquidity.md` - Root-cause diagnosis and forensic liquidity analysis for distressed credits.
- `references/valuation-and-recovery-waterfall.md` - Enterprise valuation, recovery waterfall methodology, and present-value recovery framework.
- `references/litigation-risk-bankruptcy.md` - Avoidance actions, equitable subordination, consolidation, and litigation drag.
- `references/loan-to-own-strategy.md` - Control investing, credit bidding, and fulcrum positioning.
- `references/event-driven-credit-framework.md` - Timeless framework for M&A, change-of-control, IPO, refinancing, and ownership events.
- `references/m-a-process-mechanics.md` - Process stages and certainty drivers for transaction-driven credits.
- `references/post-restructuring-monitoring.md` - Re-baselining an emerged credit and handing off into surveillance.
- `references/tax-implications-restructuring.md` - Tax issues that can affect value distribution, cash leakage, and post-emergence earnings power.

### Instruments & Asset Classes
- `references/distressed-loan-investing-lsta-standards.md` - Loan trading and settlement context for distressed situations.
- `references/cre-distressed-situations-workouts.md` - Pair when the distress question is property-backed or workout-driven.

### Tools & Summaries
- `references/practical-checklist-for-distressed-credit-analysis.md` - Reusable checklists for distressed situations and event-driven credits.
- `references/recovery-analysis-cross-reference.md` - Route recovery questions to the right asset-class skill and method.

## Output Deliverables

When asked to analyze a distressed, restructuring, or event-driven credit situation, produce:

1. **Source citations**: Explicitly cite all filings, legal documents, market data, and third-party sources.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Situation framing**: Event type, timeline, key parties, legal context, and why the situation matters for creditors.
3. **Capital structure and priority map**: Claims by entity, lien, guarantee, and effective seniority.
4. **Liquidity and path assessment**: Runway, maturity pressure, and the most plausible restructuring or resolution paths.
5. **Valuation and recovery range**: Enterprise or collateral value range, waterfall allocation, fulcrum identification, and present-value recovery where relevant.
6. **Scenario comparison**: Range of outcomes, probability framing, and the drivers that move recovery between scenarios.
7. **Investor conclusion**: Price versus underwriting, key catalysts, documentary or litigation risk, and what would change the view.

## Limitations

- Distressed valuation is path-dependent: the right framework differs for consensual exchanges, going-concern reorganizations, and forced liquidations.
- Recovery estimates are highly sensitive to legal outcomes, administrative costs, and the timing of resolution; always show ranges and key sensitivities.
- Market price is not the same as recovery value; secondary prices embed liquidity, positioning, and optionality.
- Creditor rights may differ materially from headline labels such as "secured," "senior," or "pari passu"; confirm with documentation and entity structure.

## Data Quality

- Never silently fill missing information with assumptions. Use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose gaps explicitly.
- Keep legal fact, valuation judgment, and market pricing separate. Blending them obscures what is known versus inferred.
- Use `references/default-recovery-rates.md` and `references/typical-deal-parameters.md` to calibrate judgment, not replace bottoms-up underwriting.
- When the framework may be unreliable, consult `skills/memo-generator/references/analytical-limitations.md` and state the limitation directly.

## Examples

- `examples/worked-recovery-waterfall-example.md`: Recovery waterfall example showing claim mapping, DIP impact, fulcrum identification, and pro forma post-restructuring capitalization.
