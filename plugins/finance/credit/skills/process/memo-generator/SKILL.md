---
name: Credit Memo Generator
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  Orchestration skill that produces structured Investment Committee (IC) credit memos. Guides the analyst through a complete credit analysis workflow, pulling from other skills to assemble a comprehensive memo covering business overview, financial analysis, capital structure, relative value, risks, and recommendation. Supports multiple credit types: corporate (IG/HY), private credit, CRE, and structured finance. Use this skill aggressively for any request to write a credit memo, IC memo, investment memo, credit write-up, credit summary, investment recommendation, or any structured credit analysis deliverable.
category: workflow
related_skills:
  - modeling-and-valuation
  - debt-structure-covenants
  - due-diligence-and-assessment
  - industry-sector-analysis
  - portfolio-investment-process
  - trading-pricing-mechanics
disambiguation: |
  Prefer this skill when the deliverable is a structured IC memo, credit write-up, or investment recommendation document.
  For issuer-level financial analysis and modeling, use modeling-and-valuation.
  For covenant and documentation review, use debt-structure-covenants.
  For sector context, use industry-sector-analysis.
  For diligence scoping and information-quality assessment, use due-diligence-and-assessment.
triggers:
  - credit memo
  - IC memo
  - investment memo
  - credit write-up
  - investment committee
  - credit recommendation
  - investment recommendation
  - credit analysis write-up
  - credit summary report
  - new investment analysis
  - credit proposal
  - deal memo
  - investment thesis
  - credit opinion
  - buy recommendation
  - sell recommendation
---

# Credit Memo Generator

Orchestration skill for producing structured IC memos. This skill coordinates across other domain-specific skills to assemble comprehensive credit analysis deliverables.

## Available References
When the user asks about specific topics within this domain, you MUST read the corresponding reference document from the `references/` directory before proceeding:

### Core Fundamentals
- `references/memo-structure-and-writing-guide.md`: Read this for IC Memo Structure & Standards, Section-by-Section Writing Guide, and Quality Checklist.
- `references/memo-by-credit-type.md`: Read this for Memo Templates by Credit Type (Corporate, Private Credit, CRE, Structured).
- `references/incomplete-data-guidance.md`: Read this for handling missing data and information gaps in credit analysis.

### Analytical Methodologies
- `references/conflict-resolution-guide.md`: Read this for resolving conflicting signals across analytical dimensions.
- `references/conviction-calibration.md`: Read this for calibrating recommendation conviction levels.
- `references/cross-skill-validation-checklist.md`: Read this before finalizing any multi-skill memo so cross-domain conclusions, benchmark usage, and escalation rules stay consistent.

### Tools & Summaries
- `references/common-pitfalls.md`: Read this for Common Memo Pitfalls to Avoid.

## Interactive Wizard Workflow

If the user explicitly requests an "interactive memo", "wizard", or "guided creation", or if they do not provide sufficient initial context to generate a meaningful memo, prompt them with the following interactive questionnaire *before* generating output:

1. **Credit Type**: "What type of credit is this?"
   - Corporate (IG/HY)
   - Private Credit / Direct Lending
   - Commercial Real Estate
   - Structured Finance (CLO/ABS/CMBS)
   
2. **Target**: "What is the issuer or deal name?"

3. **Data Sources**: "What data sources are available?" (multi-select)
   - 10-K / Annual Report
   - Credit Agreement / Indenture
   - Quality of Earnings (QoE) Report
   - Rent Roll / Property Appraisal
   - Rating Agency Report
   - Management Presentation
   
4. **Scope**: "What is the analysis scope?"
   - Full IC Memo
   - Quick Credit Summary
   - Update to Existing Memo

Once these inputs are collected, proceed to the **Output Deliverables** workflow using the collected context.

## Output Deliverables

1. **Source Citations**: You MUST explicitly cite your sources for all data and information provided (e.g., website URL, 10K page number, company presentation page, data provider for market data, statistics provider for economic/trend data).
   - When a stable direct URL exists, include that URL inline with the citation so downstream workflows can collect all source links for a consolidated appendix.
   - Keep locator detail in the same citation when available (for example: filing page number, presentation slide, report date, or access date).
   - Prefer canonical primary-source links over search results or aggregator URLs.
   - If no stable URL exists, retain the normal non-URL citation rather than inventing a link.

When asked to produce a credit memo, follow this structure:
1. Read the appropriate memo template from `references/memo-by-credit-type.md`
2. For each section, use the relevant domain skill to generate analysis:
   - Business & Industry → `industry-sector-analysis`
   - Financial Analysis → `modeling-and-valuation`
   - Capital Structure → `debt-structure-covenants`
   - Relative Value → `trading-pricing-mechanics`
   - Management/Sponsor → `due-diligence-and-assessment`
   - Risk Assessment → compile from all sections
   - Recommendation → `portfolio-investment-process`
3. Assemble sections into the standard memo format
4. Validate against `references/memo-structure-and-writing-guide.md` (Pre-Submission Final Check)
5. If conflicting signals emerge across sections, consult `references/conflict-resolution-guide.md` to frame the tension explicitly in the memo
6. Calibrate recommendation conviction using `references/conviction-calibration.md`
7. For any data gaps, flag them using the templates in `references/incomplete-data-guidance.md` — never silently fill gaps with assumptions
8. Run `references/cross-skill-validation-checklist.md` before finalizing the draft so internal conflicts, benchmark mismatches, and missing handoffs are resolved.
9. If the memo is headed to formal IC review, send the completed draft to the `credit-committee` agent as a post-assembly challenge step. Incorporate any substantiated findings back into the final memo before submission.

## Limitations

- Memo quality is bounded by the quality and completeness of upstream skill outputs — gaps in sector analysis, financial modeling, or structure analysis propagate into the memo
- Orchestration across multiple skills may surface inconsistencies between analytical outputs — always run `skills/memo-generator/references/cross-skill-validation-checklist.md` before finalizing
- Memo format standardization aids comparability but may not capture all nuances of unusual or hybrid credit structures — supplement standard sections as needed
- For broader framework limitations, consult `skills/memo-generator/references/analytical-limitations.md`

## Data Quality

- When data is incomplete or unavailable, consult the memo-generator's `references/incomplete-data-guidance.md` for gap disclosure templates. Never silently fill gaps with assumptions.
- When applying standard analytical frameworks, consult `skills/memo-generator/references/analytical-limitations.md` to identify when the framework may produce unreliable results. Disclose limitations proactively rather than presenting framework outputs as authoritative.

## Examples
- `examples/worked-corporate-bb-memo.md`: Complete IC memo for BB-rated corporate credit (MedTech Holdings) demonstrating how outputs from credit-modeling, debt-structure, and trading-pricing skills assemble into a structured memo
