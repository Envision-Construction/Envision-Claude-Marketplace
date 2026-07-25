# Getting Started with the Credit Investment Analysis Plugin

This plugin is a professional credit analysis toolkit designed for asset managers, credit analysts, and institutional investors. It covers leveraged finance, private credit, commercial real estate, structured finance, and portfolio management through 14 specialized skills, each backed by deep reference material on frameworks, methodologies, and market data.

---

## Which Skill Do I Use?

| If You Need To... | Use This Skill | Domain |
|---|---|---|
| Spread financials, calculate EBITDA, build projections, run scenarios | `modeling-and-valuation` | Corporate Credit |
| Analyze capital structure, covenants, or intercreditor agreements | `debt-structure-covenants` | Corporate Credit |
| Price a loan or bond, assess relative value, understand settlement mechanics | `trading-pricing-mechanics` | Markets |
| Analyze a default, restructuring, LME, or recovery scenario | `events-distressed` | Special Situations |
| Size a position, check risk limits, assess portfolio-level risk | `portfolio-investment-process` | Portfolio Mgmt |
| Look up a leveraged finance term or concept | `leveraged-finance-glossary` | Reference |
| Analyze a direct lending deal, unitranche, or BDC | `private-credit-middle-market` | Private Credit |
| Build a DCF, run comps, or model an LBO | `modeling-and-valuation` | Valuation |
| Underwrite a CRE loan or analyze a property | `cre-analysis-underwriting` | Real Estate |
| Analyze a project finance or infrastructure deal | `specialized-asset-finance` | Structured |
| Evaluate an ABS, RMBS, or CMBS deal | `securitization-and-clos` | Structured |
| Analyze equipment finance, aircraft, shipping, or leasing | `specialized-asset-finance` | Structured |
| Evaluate a CLO structure, manager, or tranche | `securitization-and-clos` | Structured |
| Write a formal IC credit memo | `memo-generator` | Workflow |
| Assess industry-specific credit dynamics and sector metrics | `industry-sector-analysis` | Sector |
| Evaluate management team quality or PE sponsor track record | `due-diligence-and-assessment` | Due Diligence |
| Assess ESG risks or sustainability-linked loan terms | `due-diligence-and-assessment` | Due Diligence |
| Set up ongoing credit monitoring and early warning systems | `surveillance-monitoring` | Post-Investment |
| Organize a data room review or due diligence workflow | `due-diligence-and-assessment` | Due Diligence |

---

## Common Workflows

The canonical multi-skill workflow order lives in `CLAUDE.md`. Use that file as the source of truth for full sequencing and handoff rules.

Quick routing shortcuts:

- New corporate or private-credit underwriting: start with `industry-sector-analysis`, then follow the relevant `CLAUDE.md` workflow.
- IC memo drafting: use `memo-generator` after the domain analysis is complete.
- Existing position monitoring: start with `surveillance-monitoring`.
- Term lookup or orientation: use `leveraged-finance-glossary`.
- CLO / ABS / RMBS / CMBS analysis: use `securitization-and-clos`.
- CRE underwriting: use `cre-analysis-underwriting`.
- Distressed / restructuring analysis: use `events-distressed`.

---

## Reference Data

The plugin maintains two categories of reference material:

### Root-Level References (Time-Sensitive Market Data)

These root reference files contain market benchmarks and statistical data that are updated periodically. The assistant automatically consults them when relevant:

| File | Contains | Consulted When Discussing |
|---|---|---|
| `references/market-benchmarks.md` | Current spreads, yields, index levels, new issue volumes | Market conditions, pricing, or relative value |
| `references/default-recovery-rates.md` | Historical default and recovery statistics by rating, seniority, and sector | Default probabilities or recovery assumptions |
| `references/rating-agency-thresholds.md` | Rating criteria, upgrade/downgrade thresholds, and rating transition matrices | Rating actions or rating-contingent analysis |
| `references/typical-deal-parameters.md` | Market terms and structural conventions for leveraged loans, high yield bonds, and private credit | Deal structuring or market convention questions |
| `references/private-credit-performance.md` | Direct lending returns, default rates, and spread data | Private credit market performance |
| `references/credit-agreement-trends-documentation-risk.md` | Trends in covenant erosion, borrower-friendly terms, and documentation risk | Covenant analysis or documentation risk |
| `references/cross-asset-relative-value.md` | Current benchmark inputs for comparing returns across loans, bonds, CLO tranches, CRE debt, and private credit | Cross-asset relative value comparisons |

For the full root-reference inventory and default-behavior rules, use `CLAUDE.md`.

For cross-skill methodology caveats rather than root-level market data, use `skills/memo-generator/references/analytical-limitations.md`.

### Skill-Level References (Domain Knowledge)

Each skill contains its own reference library stored flat in `references/` — concepts, methodologies, checklists, and templates alongside each other with descriptive filenames.

---

## Tips for Getting the Best Results

1. **Be specific about the instrument.** "Analyze this credit" is less useful than "Analyze the first lien term loan for Company X, rated B2/B by Moody's/S&P." The more context you provide about the instrument type, seniority, and rating, the more targeted the analysis.

2. **Provide financial data when available.** If you have specific financial metrics (revenue, EBITDA, leverage, coverage), include them in your request. The plugin can work with partial data but produces better output with concrete numbers.

3. **Specify the credit type.** The same term can mean different things in different contexts. "DSCR" in a corporate context routes to financial modeling; in a CRE context, it routes to property underwriting. Tell the assistant whether you are working on a corporate credit, CRE loan, structured product, or project finance deal.

4. **Use the workflow sequences for complex analysis.** For a full investment review, follow the multi-skill sequences listed above rather than trying to accomplish everything in a single request. Each skill is optimized for its specific domain.

5. **Ask for structured output.** The plugin is designed to produce tables, bullet lists, and formatted sections. Requesting a "comparison table" or "risk/mitigant list" will yield better-organized results than open-ended questions.

6. **Reference the glossary for unfamiliar leveraged-finance terms.** If you encounter a bond, loan, capital structure, pricing, or syndication term you do not recognize, ask the `leveraged-finance-glossary` skill for a definition. For specialized CRE, structured-finance, or distressed terms, use the domain skill instead.

7. **Cite your sources.** The assistant is configured to cite sources for all data and qualitative claims. When a stable direct URL exists, it should appear inline with the citation so links can be collected later; page numbers, slide numbers, and dates should stay in the same citation. If a response does not include source citations, ask for them explicitly.

---

## Harness Compatibility

This plugin has been tested across multiple Claude deployment surfaces. For details on which features are available in each environment (agents, hooks, slash commands, MCP dependencies), see **`docs/harness-compatibility.md`**.
