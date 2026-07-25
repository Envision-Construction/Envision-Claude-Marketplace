---
name: Securitization and CLOs
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  Use this skill when the analysis centers on pooled collateral, SPVs, tranching, waterfalls, credit enhancement, or manager-driven CLO structures. It covers ABS, RMBS, CMBS, WBS, and CLO underwriting from legal structure through cash flow behavior, test mechanics, collateral quality, servicer or manager assessment, and tranche-level risk.
category: structured-finance
related_skills:
  - cre-analysis-underwriting
  - memo-generator
  - modeling-and-valuation
  - portfolio-investment-process
  - trading-pricing-mechanics
triggers:
  - securitization
  - structured credit
  - structured products
  - ABS
  - RMBS
  - CMBS
  - CLO
  - collateralized loan obligation
  - tranching
  - waterfall analysis
  - credit enhancement
  - OC test
  - IC test
  - prepayment risk
  - OAS
  - WAL
  - servicer
  - special servicer
  - manager evaluation
  - whole business securitization
disambiguation: |
  Prefer this skill when the context involves collateral pools, bankruptcy-remote SPVs, tranche subordination, waterfall mechanics, or structured-finance monitoring.
  For issuer-level leverage, coverage, and operating cash flow, use modeling-and-valuation.
  For property-level underwriting within CMBS or CRE CLO collateral, use cre-analysis-underwriting.
  For project finance and asset-based lending without tranched securitization structures, use specialized-asset-finance.
---

# Securitization & CLOs

Securitization underwriting starts with structure before spread. Confirm the legal isolation of the assets, map the waterfall, understand how collateral can amortize or deteriorate, and only then decide whether the tranche is being paid enough for extension, loss, liquidity, and governance risk.

## Core Workflow

1. **Map the legal structure**: Confirm true sale, bankruptcy remoteness, issuer or servicer dependencies, and where the collateral and cash actually sit.
2. **Understand tranche economics**: Identify attachment and detachment, payment priority, reserve accounts, and the triggers that can redirect cash.
3. **Underwrite collateral behavior**: Focus on default timing, loss severity, prepayment or turnover behavior, and concentration risk by obligor, sector, geography, or collateral type.
4. **Evaluate active agents**: For CLOs, underwrite the manager. For consumer and mortgage deals, underwrite the servicer, special servicer, or originator controls.
5. **Stress the structure**: Test whether the tranche survives slower amortization, faster defaults, weaker recoveries, or test failures that trap cash upstream.
6. **Anchor relative value last**: Use market spreads and current conventions from root references only after the structural and collateral view is clear.

## Reference Map

Read the smallest relevant document rather than loading the full library.

### Core Structure
- `references/securitization-structure-and-risk.md` - Securitization fundamentals (true sale, SPV, tranching), credit enhancement mechanisms, and cross-asset risk analysis.
- `references/clo-structure-and-economics.md` - CLO tranche economics, pool construction, lifecycle, coverage tests, portfolio constraints, deal selection, and secondary execution.
- `references/asset-class-deep-dives.md` - Cross-asset differences in collateral behavior and structural emphasis.

### Structure And Modeling
- `references/cash-flow-metrics-and-prepayment.md` - WAL, CPR, CDR, loss severity, spread measures, prepayment behavior, and waterfall analysis.
- `references/oas-methodology.md` - OAS as a framework for optionality-heavy assets.
- `references/clo-manager-evaluation.md` - How to separate manager skill from cycle or vintage effects.

### Instruments And Vehicles
- `references/asset-class-deep-dives.md` - ABS (auto, credit card, student loan, equipment), RMBS (agency and non-agency), CMBS (conduit, SASB, CRE CLO), and loan fund vehicle structures.
- `references/whole-business-securitization-wbs.md` - Operating-business collateral and covenant-specific issues.
- `references/advanced-mbs-abs-analytics.md` - Advanced MBS, CMO, and optionality analytics.
- `references/abs-servicer-evaluation.md` - Servicer and special-servicer assessment framework.

### Tools And Checklists
- `references/practical-deal-evaluation-checklist.md` - Key structured-credit principles and underwriting/monitoring checklist for a live deal review.

## Output Deliverables

When asked to analyze a securitization, CLO, or structured product, produce:

1. **Source citations**: Explicitly cite every data source, market input, trustee report, and qualitative fact used.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Structure snapshot**: Issuer or manager, deal size, collateral type, tranche stack, enhancement, and key dates.
3. **Collateral and behavior view**: Core collateral metrics, concentration points, default and recovery assumptions, and prepayment or turnover behavior.
4. **Waterfall and test dashboard**: Priority of payments, OC and IC triggers, reserve mechanics, and current or underwritten cushion.
5. **Scenario analysis**: Base, downside, and severe cases showing which tranche protections fail first and how cash is redirected.
6. **Agent assessment**: Manager, servicer, or special-servicer strengths, weaknesses, and governance concerns.
7. **Relative value framing**: Compare spread or price to relevant peers only after structure and collateral quality are established.
8. **Recommendation and monitoring items**: State tranche view, key breakpoints, and the specific metrics that require follow-up.

## Limitations

- Waterfall strength can obscure weak collateral quality; enhancement only helps if loss timing and severity stay within structural assumptions.
- Prepayment and extension models are approximations; modest assumption changes can move WAL, OAS, and tranche cash flows materially.
- CLO and securitization history is regime-dependent; manager or servicer track records can reflect vintage luck as much as repeatable skill.
- Structural test cushions can look healthy while deteriorating in trajectory; trend matters at least as much as current headroom.
- For broader framework limitations, consult `skills/memo-generator/references/analytical-limitations.md`.

## Data Quality

- Never silently backfill missing trustee, servicer, or loan-level data. Use `skills/memo-generator/references/incomplete-data-guidance.md` to disclose gaps explicitly.
- Keep timeless framework separate from current market inputs. Pull live spreads, issuance conditions, and deal conventions from root references instead of embedding them in the analysis.
- When using benchmark inputs from root references, check freshness metadata and warn if those files are past `next_review`.
- When applying standard frameworks mechanically would mislead, consult `skills/memo-generator/references/analytical-limitations.md` and state the limitation directly.

## Examples
- `examples/worked-clo-equity-case-study.md` - CLO equity case showing waterfall behavior, NAV framing, and OC-driven downside.
- `examples/worked-new-issue-clo-analysis.md` - Synthetic new-issue CLO underwriting example with coverage tests, collateral metrics, and scenario analysis.
