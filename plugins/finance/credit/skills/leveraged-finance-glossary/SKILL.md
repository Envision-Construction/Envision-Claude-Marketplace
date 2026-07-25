---
name: Leveraged Finance Glossary
version: "1.5.0"
last_modified: "2026-03-22"
description: |
  Use this skill when the user needs definitions, distinctions, or quick orientation on leveraged finance terms, capital structure, bond and loan mechanics, syndication, or documentation basics. Prefer domain skills when the question is really about CRE, structured finance, distressed situations, portfolio construction, or full underwriting.
category: reference
related_skills:
  - modeling-and-valuation
  - debt-structure-covenants
  - trading-pricing-mechanics
  - events-distressed
  - industry-sector-analysis
  - portfolio-investment-process
triggers:
  - leveraged finance
  - high yield
  - leveraged loan
  - bank loan
  - revolver
  - term loan
  - bond pricing
  - yield
  - spread
  - OAS
  - covenant-lite
  - capital structure
  - senior secured
  - pari passu
  - syndication
  - bookrunner
  - lead arranger
  - assignment
  - participation
  - market flex
  - ratings
  - fallen angel
disambiguation: |
  Prefer this skill for "what does this term mean?" and market-mechanics orientation questions.
  Use modeling-and-valuation for issuer financial analysis, debt-structure-covenants for covenant interpretation, trading-pricing-mechanics for security valuation and relative value, cre-analysis-underwriting for property terms, securitization-and-clos or specialized-asset-finance for structured-credit terms, and portfolio-investment-process or surveillance-monitoring for portfolio process terminology.
---
# Leveraged Finance Glossary

This skill is a compact reference layer for language that recurs across leveraged loans, high-yield bonds, capital structure work, and primary-market execution. Use it to define the term, explain why it matters, distinguish it from adjacent concepts, and route to a deeper skill when the question becomes analytical rather than definitional.

## Core Workflow

1. **Identify the domain first**: Confirm whether the question is really leveraged finance, or whether it belongs to CRE, structured finance, distressed, portfolio, or sector analysis.
2. **Define the term precisely**: Give the plain-language meaning before adding formulas, examples, or legal nuance.
3. **Explain underwriting relevance**: State why the term matters to a credit investor, lender, or underwriter.
4. **Distinguish adjacent terms**: Clarify commonly confused pairs such as leverage vs. coverage, yield vs. spread, assignment vs. participation, or secured vs. unsecured.
5. **Route to the right skill if depth is needed**: Use this glossary for orientation, then hand off when the question requires modeling, documentation analysis, or asset-class-specific underwriting.

## Reference Map

Read the narrowest reference that answers the question instead of loading the full reference set.

### Core Market Structure
- `references/market-overview-participants.md` - Market definition, participant roles, and primary-vs-secondary-market framing.
- `references/ratings-agencies-credit-assessment.md` - Rating scales, split ratings, outlooks, and how ratings fit into credit work.

### Instruments, Documentation, and Execution
- `references/bond-loan-fundamentals.md` - Revolvers, term loans, bond vs. loan structures, core documentation, and transfer mechanics.
- `references/loan-syndication-process.md` - Primary-market loan launch, syndication roles, flex, and allocation mechanics.

### Pricing and Term Lookup
- `references/bond-pricing-yields.md` - Price, accrued interest, yields, spreads, duration, and return language.
- `references/comprehensive-glossary-of-key-terms.md` - Quick thematic lookup for recurring leveraged-finance vocabulary.

### Domain Handoffs
- Use `debt-structure-covenants` when a term question turns into document interpretation, basket leakage, lien priority, or LME vulnerability.
- Use `trading-pricing-mechanics` when the user wants security valuation, relative value, settlement mechanics, or market color.
- Use `modeling-and-valuation` when the term question becomes issuer-level ratio analysis, projections, or scenario work.
- Use `events-distressed` when terms involve restructurings, recoveries, fulcrum securities, DIP financing, or Chapter 11 process.
- Use `cre-analysis-underwriting` for property, NOI, cap rate, lease, and mortgage-specific terms.
- Use `securitization-and-clos` or `specialized-asset-finance` for securitization, project finance, and asset-finance terminology.

## Output Deliverables

When the user asks for definitions or concept explanations, produce:

1. **Source citations**: Explicitly cite the skill-local reference used, plus any root reference used for current market data.
   - When a stable direct URL exists, include it inline with the citation and keep any page, slide, filing-date, report-date, or access-date detail in the same citation.
2. **Definition**: A concise explanation in plain language.
3. **Why it matters**: The underwriting, documentation, or investing relevance of the term.
4. **Related or confused terms**: Brief distinctions from adjacent concepts.
5. **Example or formula when helpful**: Add only when it improves clarity.
6. **Domain tag or routing note**: State when the term belongs to a more specialized skill.
7. **Grouped presentation for multiple terms**: Organize large term lists by theme rather than alphabet soup.

## Limitations

- This skill explains language and market mechanics; it does not replace full underwriting, covenant reading, or valuation work.
- Many terms have domain-specific meanings. The same word can mean different things in corporate credit, CRE, project finance, or securitization.
- Documentation terms are only as precise as the governing credit agreement, indenture, or offering memo. Definitions in actual documents override shorthand market usage.
- Do not treat glossary language as current market evidence. Pricing, covenant aggression, and rating calibration change over time and belong in root references.

## Data Quality

- If the question touches current spread levels, pricing, rating thresholds, or deal norms, read the appropriate root reference first.
- Keep skill-local references focused on durable concepts; do not rest answers on old "typical" ranges if the question is time-sensitive.
- When a term depends on sector-specific accounting or asset structure, route to the relevant sector or asset-class skill rather than improvising.
- If information is incomplete, use `skills/memo-generator/references/incomplete-data-guidance.md` rather than filling gaps silently.

