---
name: Due Diligence and Assessment
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  Use when evaluating data rooms, third-party diligence materials, management teams, PE sponsors, ESG risks, or sustainability-linked structures in credit underwriting. Prefer this skill for information-quality assessment, diligence scoping, qualitative risk translation, and identifying gaps that must be resolved before committing capital.
category: due-diligence
related_skills:
  - memo-generator
  - modeling-and-valuation
  - debt-structure-covenants
  - portfolio-investment-process
  - private-credit-middle-market
disambiguation: |
  Prefer this skill when the task is evaluating information quality, reviewing data rooms, assessing management or sponsors, or identifying diligence gaps.
  For financial modeling and ratio analysis, use modeling-and-valuation.
  For covenant and document interpretation, use debt-structure-covenants.
  For assembling findings into a memo deliverable, use memo-generator.
triggers:
  - due diligence
  - data room
  - virtual data room
  - document request
  - information gap
  - CIM review
  - QoE
  - quality of earnings
  - third-party report
  - management assessment
  - sponsor assessment
  - governance
  - ESG risk
  - sustainability-linked loan
  - greenwashing
---

# Due Diligence & Assessment

Due diligence is an exercise in prioritization under incomplete information. The goal is not to read every page in the room; it is to separate confirmed facts from advocacy, identify what still matters to the downside case, and translate unresolved issues into modeling adjustments, structural asks, or explicit memo flags.

## Core Workflow

1. **Define the diligence question**: What must be true for the credit to work, and what evidence is needed to verify it?
2. **Prioritize the highest-value materials**: Start with the items that can change the downside case quickly, such as financial statements, QoE, major contracts, draft credit documents, management history, and key third-party reports.
3. **Test source quality before conclusions**: Identify who prepared each document, what was independently verified, what was excluded, and where incentives may bias the presentation.
4. **Translate findings into credit consequences**: Convert diligence observations into cash flow, liquidity, leverage, covenant, collateral, governance, or refinancing implications.
5. **Separate facts from sponsor case**: Distinguish in-place performance and documented evidence from pro forma claims, anticipated synergies, or unverified management assertions.
6. **Document gaps explicitly**: Record missing materials, unanswered questions, alternate sources, and what assumption range is required if the gap remains unresolved.
7. **Hand off the right outputs**: Pass validated diligence findings into modeling, covenant review, surveillance setup, and memo writing.

## Reference Map

Read the most relevant reference for the question at hand rather than loading the full library.

### Core Diligence Design
- `references/due-diligence-workflow.md` - Triage order, sequencing, and information-gap handling across deal types.
- `references/document-request-lists.md` - What to request by transaction type and where to focus first.
- `references/third-party-report-assessment.md` - How to read externally prepared diligence materials skeptically and translate them into credit implications.

### Financial Quality and Information Reliability
- `references/qoe-report-interpretation.md` - QoE report review, adjustment discipline, and translation to model inputs.
- `references/sell-side-bias-assessment.md` - How to de-bias CIMs, management decks, and sponsor projections.
- `references/red-flags-by-document.md` - Fast scan of recurring warning signs by document type.

### Management, Governance, and Sponsor Assessment
- `references/management-key-person-assessment.md` - Management evaluation, key person risk, succession planning, and management diligence checklist.
- `references/pe-sponsor-assessment.md` - Sponsor incentives, support capacity, behavioral patterns (dividend recaps, add-ons, LMEs, restructuring), and sponsor diligence checklist.
- `references/governance-board-assessment.md` - Board oversight, auditor quality, and creditor-relevant governance signals.
- `references/conflict-of-interest-checklist.md` - Pre-investment conflict of interest identification, MNPI protocols, cross-fund exposure, and sign-off requirements.

### ESG and Sustainability-Linked Structures
- `references/esg-credit-integration.md` - ESG-to-credit-risk framework, practical diligence workflow, greenwashing checks, and ESG due diligence checklist.
- `references/sll-structure-mechanics.md` - Timeless SLL design principles, documentation logic, credit framing, and SLL evaluation checklist.

## Output Deliverables

When asked to evaluate diligence materials, management, sponsors, governance, ESG issues, or SLL features, produce:

1. **Source citations**: Explicitly cite each material source, including filings, presentations, data-room items, and third-party reports.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Diligence status matrix**: What was received, what was reviewed, what remains missing, and which items are critical versus nice-to-have.
3. **Source-quality assessment**: Who prepared each key document, what scope or caveats apply, and where the bias or blind spots are most likely to sit.
4. **Management, sponsor, and governance view**: Experience, alignment, board quality, key-person dependency, and evidence of supportive versus extractive behavior.
5. **ESG or SLL assessment**: Only where relevant, identify the material factors, transmission to credit risk, KPI/SPT quality, and any greenwashing concerns.
6. **Risk translation**: Show how diligence findings change cash flow assumptions, leverage tolerance, covenant asks, collateral view, liquidity analysis, or refinancing confidence.
7. **Open items and required actions**: The missing information or follow-up requests that could still change the recommendation.

## Limitations

- Management assessment is inherently subjective; document the basis for judgments explicitly.
- Sponsor track record is informative but not dispositive; incentives can change with fund age, mark pressure, and deal context.
- ESG materiality evolves as regulation, litigation, and technology change; use the framework to organize risk, not to imply false precision.
- Data room completeness is itself a signal; missing documents may indicate intentional withholding rather than simple oversight.
- For broader framework limitations, consult `skills/memo-generator/references/analytical-limitations.md`.

## Data Quality

- Never silently bridge missing information with unsupported assumptions. If data is incomplete, use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose the gap and its analytical consequence.
- Keep reported performance, QoE-adjusted performance, and sponsor or management case assumptions distinct.
- When a conclusion depends on market convention or a changing external benchmark, use the relevant root reference rather than hard-coding the assumption into the diligence narrative.
- When standard analytical frameworks may be unreliable, consult `skills/memo-generator/references/analytical-limitations.md` and state the limitation directly.

## Examples
- `examples/worked-management-sponsor-assessment-example.md`: Management team and PE sponsor evaluation for a PE-backed diagnostics company, including key-person risk, sponsor behavior assessment, ESG materiality, and covenant handoff flags
