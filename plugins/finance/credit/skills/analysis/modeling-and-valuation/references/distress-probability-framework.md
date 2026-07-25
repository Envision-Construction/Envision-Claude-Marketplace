---
last_updated: "2026-03-22"
---

# Unified Distress Probability Framework

This framework integrates three cross-skill risk dimensions into a composite distress score that informs default probability estimates and scenario analysis weighting. Each dimension captures a distinct source of credit risk that traditional single-metric analysis may miss.

---

## Risk Dimension 1: Silent Debt Capacity Risk

**Source skill:** `debt-structure-covenants` (see `skills/debt-structure-covenants/references/silent-debt-capacity.md`)

Silent debt capacity measures how much additional debt the borrower can raise without lender consent through builder baskets, incremental facilities, unrestricted subsidiary designations, ratio-based debt carve-outs, and other permitted indebtedness provisions. Higher silent capacity represents greater structural risk because the borrower's actual leverage at the time of stress may significantly exceed the leverage at underwriting.

### Scoring

| Score | Silent Debt Capacity (as multiple of EBITDA) | Description |
|---|---|---|
| 1 | <0.5x EBITDA | Minimal incremental capacity. Tight credit agreement with limited builder basket, no ratio debt, no unrestricted subsidiary capacity. |
| 2 | 0.5x - 1.0x EBITDA | Modest capacity. Standard builder basket with reasonable starter amount, limited incremental facility. |
| 3 | 1.0x - 2.0x EBITDA | Moderate capacity. Meaningful builder basket, incremental facility up to 1.0x, some ratio debt capacity. |
| 4 | 2.0x - 3.0x EBITDA | Significant capacity. Large builder basket, generous incremental provisions, ratio debt available at current leverage. Sponsor likely to use capacity for bolt-on M&A or distribution. |
| 5 | >3.0x EBITDA | Extensive capacity. Aggressive documentation with large unrestricted subsidiary capacity, uncapped ratio debt, or combinations that allow near-doubling of current debt. |

### Assessment Notes

- Calculate silent capacity at current EBITDA levels, not at underwriting EBITDA — capacity may have grown with EBITDA growth
- Include capacity from all sources: builder baskets, incremental facilities, ratio debt, unrestricted subsidiary debt, and permitted liens
- When silent capacity exceeds 2.0x turns, flag as elevated structural risk per CLAUDE.md cross-skill handoff rules (reduce maximum position size by 25% or require additional IC condition)

---

## Risk Dimension 2: Covenant Monitoring Risk

**Source skill:** `surveillance-monitoring` (see `skills/surveillance-monitoring/references/escalation-framework.md`)

Covenant monitoring risk assesses the quality of early warning coverage provided by the credit documentation. Credits with maintenance covenants provide regular checkpoints that surface deterioration early. Cov-lite credits with only incurrence-based tests may not provide any financial warning until the borrower attempts a transaction that requires compliance — by which time deterioration may be severe.

### Scoring

| Score | Covenant Protection Level | Description |
|---|---|---|
| 1 | Strong maintenance covenants | Multiple financial maintenance covenants (leverage + coverage + capex) tested quarterly. Tight cushion (<15% headroom). EBITDA equity cure limited to 2 uses. |
| 2 | Standard maintenance covenants | 1-2 financial maintenance covenants tested quarterly. Standard cushion (15-25% headroom). Equity cure provisions present. |
| 3 | Springing covenants only | Financial covenant springs only upon revolver draw >35%. No regular financial testing absent revolver usage. Incurrence tests for restricted payments. |
| 4 | Cov-lite with incurrence tests | No maintenance covenants. Incurrence tests only (tested when borrower initiates a restricted action). Limited negative covenants. |
| 5 | Cov-lite with weak incurrence | No maintenance covenants. Incurrence tests with generous baskets and addbacks. Weak negative covenants. Significant permitted actions without compliance testing. |

### Assessment Notes

- Consider the practical enforceability of covenants — a maintenance covenant with unlimited addbacks or a 50% headroom cushion provides limited early warning despite technically being a "maintenance" test
- Springing covenants scored at 3 assume the revolver is not regularly drawn; if the borrower routinely draws >35%, treat as score 2
- For private credit, covenant protection is typically stronger (scores 1-2) — this is a structural advantage that should be reflected in the composite score

---

## Risk Dimension 3: Sector Cyclicality Risk

**Source skill:** `industry-sector-analysis` (see sector-specific framework references)

Sector cyclicality risk captures the current position in the industry cycle and the sensitivity of the borrower's sector to economic downturns. Late-cycle positions with declining leading indicators carry materially higher default risk than early-cycle positions with improving fundamentals.

### Scoring

| Score | Cycle Position | Description |
|---|---|---|
| 1 | Early recovery | Sector emerging from trough. Order books improving, capacity utilization rising from lows, credit metrics improving sequentially. Default risk declining. |
| 2 | Mid-cycle expansion | Sector in stable growth. Balanced supply-demand dynamics, stable margins, manageable competitive intensity. Default risk at or below historical average. |
| 3 | Late-cycle expansion | Sector showing late-cycle signals. Peak margins, aggressive capacity additions, rising inventory levels, new entrant activity. Default risk rising from lows. |
| 4 | Early downturn | Sector entering contraction. Declining order books, margin compression beginning, inventory builds, peer downgrades. Default risk above historical average and rising. |
| 5 | Deep recession / structural decline | Sector in severe contraction or facing structural disruption. Revenue declines >10% across peers, widespread margin compression, liquidity stress in weaker names. Default risk at or near peak. |

### Assessment Notes

- Cycle assessment should reference objective data: order book trends, capacity utilization, inventory-to-sales ratios, peer revenue growth rates, and leading indicators specific to the sector
- For sectors with low cyclicality (utilities, regulated healthcare), scores typically range from 1-3 unless structural disruption applies
- Technology and consumer discretionary sectors can move rapidly through cycle stages — reassess at least quarterly
- When the sector score is 4 or 5, the sector-stress scenario per `references/stress-scenario-framework.md` must be applied per CLAUDE.md cross-skill handoff rules

---

## Composite Distress Score Calculation

The composite distress score is calculated as a weighted average of the three risk dimensions:

| Dimension | Weight | Rationale |
|---|---|---|
| Silent Debt Capacity Risk | 30% | Structural risk — determines how much worse leverage can get without lender consent |
| Covenant Monitoring Risk | 30% | Detection risk — determines how early deterioration will be identified |
| Sector Cyclicality Risk | 40% | Fundamental risk — determines the probability that the business environment causes deterioration |

**Formula:** Composite Score = (Silent Debt Score x 0.30) + (Covenant Score x 0.30) + (Sector Score x 0.40)

### Score Interpretation

| Composite Score Range | Risk Category | Description |
|---|---|---|
| >=1.0 and <2.0 | Low | Strong structural protections, adequate monitoring, favorable sector conditions. Standard surveillance cadence appropriate. |
| >=2.0 and <3.0 | Moderate | Some risk factors present but manageable. Enhanced monitoring recommended. Watch for deterioration in any single dimension. |
| >=3.0 and <4.0 | Elevated | Multiple risk factors active. Increased surveillance frequency required. Position size should reflect elevated risk. Downside scenario probability weighting must be increased. |
| >=4.0 and <=5.0 | High | Significant risk across multiple dimensions. Maximum surveillance frequency. Position reduction or hedging should be actively considered. |

---

## Default Probability Mapping

The composite distress score maps to an implied 3-year cumulative default probability range, calibrated against historical default rate data from `references/default-recovery-rates.md`.

| Risk Category | Composite Score | Implied 3-Year Cumulative Default Probability |
|---|---|---|
| Low | >=1.0 and <2.0 | 1% - 3% |
| Moderate | >=2.0 and <3.0 | 3% - 8% |
| Elevated | >=3.0 and <4.0 | 8% - 15% |
| High | >=4.0 and <=5.0 | 15% - 30% |

### Calibration Notes

- Default probability ranges are indicative and should be compared against market-implied default probabilities (from CDS spreads or loan pricing) as a reasonableness check
- The mapping is calibrated to broadly rated B/B- credits — for BB-rated credits, shift the probability range down by approximately 50%; for CCC-rated credits, shift up by approximately 100%
- Probability ranges represent the central tendency — actual default probability for any individual credit depends on idiosyncratic factors not captured by these three dimensions alone

---

## Integration with Scenario Analysis

The composite distress score directly influences scenario analysis in `references/scenario-analysis-framework.md`:

- **Composite score >= 3.0 (Elevated or High):** The downside scenario probability weighting must be increased by 10 percentage points relative to the standard probability distribution. For example, if the standard framework assigns 25% probability to the downside scenario, an elevated distress score requires 35% probability weighting.
- **Composite score >= 4.0 (High):** In addition to the 10 percentage point increase, a severe stress scenario (using parameters from `references/stress-scenario-framework.md`) must be modeled as a distinct fourth scenario with at least 10% probability weighting.
- **Composite score < 2.0 (Low):** No adjustment to standard probability weighting. The analyst may optionally reduce downside probability weighting by up to 5 percentage points with documented justification.

---

## Cross-Skill Integration

This framework requires inputs from three separate skills. When assembling the distress probability assessment:

1. **Request silent debt capacity analysis** from `debt-structure-covenants` — specifically the output from the silent debt capacity assessment methodology in `skills/debt-structure-covenants/references/silent-debt-capacity.md`
2. **Request covenant quality assessment** from `surveillance-monitoring` — specifically the escalation framework in `skills/surveillance-monitoring/references/escalation-framework.md` which defines the monitoring infrastructure quality
3. **Request sector cycle assessment** from `industry-sector-analysis` — specifically the sector-specific analytical frameworks that include cycle positioning indicators
4. **Validate composite score** against the cross-skill validation checklist in `skills/memo-generator/references/cross-skill-validation-checklist.md` before incorporating into the credit memo

When any individual dimension score changes by 1 or more points during surveillance, recalculate the composite score and reassess whether the current position size and monitoring cadence remain appropriate.
