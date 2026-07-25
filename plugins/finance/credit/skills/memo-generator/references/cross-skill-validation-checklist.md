---
last_updated: "2026-03-22"
---

# Cross-Skill Validation Checklist

When multiple skills contribute to a single investment recommendation, outputs can diverge due to different assumptions, data snapshots, or analytical conventions. This checklist ensures internal consistency across all skill outputs before the credit memo is finalized and submitted to the Investment Committee. Each item should be verified sequentially within its workflow stage.

---

## Checklist Governance

### Ownership

The lead analyst is responsible for completing all Pre-Memo Assembly and IC Submission checks before circulating the memo for IC review. The PM is responsible for verifying all Position Sizing checks before approving the recommended size. Post-IC checks are jointly owned by the analyst (surveillance setup) and operations (risk system entry).

### Gate Mechanism

No credit memo may be submitted to the IC without documented completion of items 1-15. The analyst must include a signed checklist appendix with the memo package confirming each item has been verified. If any item fails verification, the analyst must either (a) resolve the inconsistency before submission, or (b) document the exception with PM sign-off. Items 16-18 must be completed before trade date; failure to complete by T+5 triggers a Tier 2 escalation.

### Documentation

Each checklist item requires a one-line verification note documenting how it was confirmed (e.g., "Item 1: Leverage of 4.8x confirmed in both model output tab B3 and capital structure map Section 2.1"). These notes are archived with the credit file and reviewed during annual governance audits.

---

## Pre-Memo Assembly

These checks ensure that the analytical building blocks produced by individual skills are internally consistent before they are assembled into a unified credit memo.

### 1. Model-Structure Consistency

Model leverage from `modeling-and-valuation` matches the capital structure map in `debt-structure-covenants`. Verify that the total debt quantum, EBITDA definition (including the same addback treatment), and resulting leverage ratio are identical across both outputs. Discrepancies typically arise from different handling of revolving facility draws, capital leases, or preferred equity classification.

### 2. Spread-Benchmark Alignment

The spread used in `trading-pricing-mechanics` relative value analysis matches current levels in `references/market-benchmarks.md`. If the market-benchmarks data is stale (current date exceeds `next_review`), flag the staleness explicitly and use the data with a caveat noting the vintage date. Spreads can move materially within a single quarter, particularly in HY and leveraged loan markets.

### 3. Recovery-Default Consistency

Recovery assumptions used in stress scenarios align with `references/default-recovery-rates.md` by seniority and asset type. Verify that first lien, second lien, and unsecured recovery assumptions fall within historical ranges for the relevant industry and collateral type. If recovery assumptions deviate from historical medians, document the rationale (e.g., asset-light business model, jurisdictional differences, or structural subordination effects).

### 4. Sector Benchmark Alignment

Leverage ranges and key operating metrics used in model scenarios align with `industry-sector-analysis` benchmarks for the relevant sector and rating tier. Base case assumptions should not exceed top-quartile sector performance without explicit justification, and downside scenarios should reflect at least trough-cycle sector conditions.

### 5. Covenant-Surveillance Consistency

Covenant headroom calculated in `debt-structure-covenants` matches the monitoring thresholds set in `surveillance-monitoring`. Verify that covenant levels, test dates, compliance measurement methodology, and headroom percentages are consistent across both outputs. Misalignment here leads to false comfort on early warning triggers.

---

## Position Sizing

These checks ensure that the recommended position is compliant with all applicable risk limits, fund constraints, and stress parameters before the investment is sized.

### 6. Risk Parameter Compliance

The recommended position size complies with all limits in `references/portfolio-risk-parameters.md`, including single-name concentration (both soft and hard caps), sector concentration, rating bucket allocation, and instrument type limits. Verify compliance at both the individual fund level and any aggregate portfolio level where applicable.

### 7. Vehicle-Specific Compliance

Vehicle-specific compliance is satisfied using the governing mandate documents and the relevant skill reference. For BDC-backed private credit positions, verify asset coverage ratio compliance and qualifying asset percentage using `skills/private-credit-middle-market/references/bdc-regulatory.md`. For other vehicles, confirm that the position fits the applicable indenture, prospectus, IMA, or fund guidelines. Binding vehicle constraints can limit position size below the general risk parameter maximum.

### 8. Stress Survival

Stress test results (per `references/stress-scenario-framework.md`) confirm that the position survives the severe scenario without breaching portfolio-level risk limits. Verify that the stress scenario uses the correct asset-class-specific parameters, that the position-level loss estimate is consistent with the recovery assumptions in item 3, and that the portfolio-level impact assessment reflects accurate correlations with existing holdings.

The stress test output must be embedded in the position sizing recommendation — not referenced separately. The Position Sizing Output deliverable must include: (a) the stress scenario applied, (b) position-level loss estimate, (c) portfolio-level impact including correlation with existing holdings, and (d) confirmation that no portfolio-level risk limit is breached under stress. A position sizing recommendation without an embedded stress test is incomplete and should not be submitted to IC.

### 9. Cross-Asset Normalization

If the investment recommendation involves comparing opportunities across asset classes (e.g., leveraged loan vs. CLO tranche vs. CRE debt vs. private credit), verify that normalized metrics have been applied per `skills/portfolio-investment-process/references/cross-asset-relative-value-framework.md`, using current benchmark inputs from `references/cross-asset-relative-value.md`. Key normalizations include duration-adjusted spread, loss-adjusted yield, and liquidity-adjusted return. Relative value conclusions drawn without normalization across asset classes are unreliable.

---

## IC Submission

These checks ensure that the credit memo meets IC presentation standards for transparency, completeness, and intellectual honesty before submission.

### 10. Data Gap Disclosure

All material data gaps are explicitly flagged per the memo-generator's `references/incomplete-data-guidance.md`. Verify that no silent assumptions fill material gaps. Every data gap should state what is missing, why it matters, what assumption was used in its place, and how the conclusion would change if the assumption is wrong.

### 11. Framework Limitation Disclosure

Analytical framework limitations are disclosed per `skills/memo-generator/references/analytical-limitations.md` and the relevant skill-specific Limitations section. Proactive disclosure of where standard frameworks may produce unreliable results is required rather than authoritative presentation of framework outputs. Common triggers include small comp sets, near-zero EBITDA, and stale cap rate markets.

### 12. Source Citation Completeness

Source citations are provided for all data, metrics, and qualitative assertions throughout the memo. Acceptable citations include website URLs, 10-K/10-Q page numbers, company presentation slide references, rating agency report dates, and data provider references (e.g., LCD, Bloomberg, Intex). When a stable direct URL exists, it must be included inline with the citation so the final memo package can collect a comprehensive linked source appendix downstream. Locator detail such as page numbers, slide numbers, filing dates, report dates, and access dates should remain in the same citation. Unsourced quantitative claims are not acceptable for IC submission.

### 13. Conviction Calibration

The recommendation conviction level is calibrated per `skills/memo-generator/references/conviction-calibration.md`. Verify that the stated conviction (High/Medium/Low) is aligned with the underlying information quality, degree of analytical uncertainty, and strength of supporting evidence. A high-conviction recommendation with material data gaps or untested assumptions signals a calibration failure.

### 14. Thesis-Kill Triggers Defined

Specific, measurable metrics or events that would invalidate the investment thesis are defined and mapped to `surveillance-monitoring` escalation tiers. Each thesis-kill trigger must include a quantitative threshold (not directional language like "significant decline"), a measurement frequency, and a data source. Vague or unmeasurable triggers defeat the purpose of post-investment monitoring.

### 15. Condition Monitoring Handoff

If a Conditional Pass recommendation is anticipated, the memo includes a condition monitoring handoff block specifying: the verification method for each condition, the responsible party, the deadline for satisfaction, and the surveillance tier escalation if the condition is unmet by the deadline. Conditional approvals without a monitoring mechanism are effectively unconditional.

---

## Post-IC

These checks ensure that approved investments are properly integrated into the surveillance and risk management infrastructure on or before trade date.

### 16. Condition-Surveillance Mapping

All approved IC conditions are mapped to the surveillance framework with specific deadlines and verification methods. Each condition should have a clear owner, a defined evidence standard for satisfaction, and an escalation path if the deadline is missed. Conditions should be tracked in the same system as ongoing surveillance to avoid parallel tracking.

### 17. Initial Surveillance Setup

The monitoring framework is established in `surveillance-monitoring` before trade date, including: monitoring cadence (monthly/quarterly), key metrics to track, escalation thresholds by tier, and thesis-kill triggers from item 14. Every approved position must have an active surveillance setup before settlement. Positions that settle without surveillance coverage create unmonitored risk.

### 18. Risk System Entry

The position is entered in the portfolio risk system with the correct instrument classification, risk weights, and fund vehicle allocation. Verify that the instrument type (revolver, TL, bond, CLO tranche, CRE loan, etc.) maps to the correct risk weight, that the fund vehicle allocation matches the IC approval, and that concentration metrics update correctly upon entry. Misclassification at entry propagates errors through all downstream risk reporting.

### 19. Bidirectional Handoff Verification

Verify that all cross-skill handoffs documented in `CLAUDE.md` are reflected bidirectionally in the relevant skill outputs. Specifically: (a) every escalation condition triggered in one skill has a corresponding acknowledgment in the receiving skill's output, (b) upstream data sources cited in one skill's output match the data actually produced by the upstream skill, and (c) numeric thresholds (e.g., silent debt capacity >2.0x, OC cushion <200bps) are applied consistently across both the triggering and receiving skills. This check prevents scenarios where an escalation fires but the receiving skill does not incorporate the finding.
