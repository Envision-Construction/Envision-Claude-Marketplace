---
name: Deep Research
description: Deep research harness. Decompose a question into complementary search angles, run fan-out web searches, fetch sources, extract falsifiable claims, adversarially verify every claim, and synthesize a confidence-ranked cited report. Use whenever the user asks for deep research, a multi-source fact-checked report, due diligence, or market / technical / competitive / scientific research on ANY topic. Before starting, if the question is underspecified (e.g. "what car should I buy" without budget/use-case/region), ask 2-3 clarifying questions to narrow scope.
---

# Deep Research

Execute a rigorous multi-phase research pipeline: Scope, Search, Fetch & Extract, Verify, Synthesize. Every load-bearing claim in the final report must have survived adversarial verification. Never skip the Verify phase: unverified web claims are the primary failure mode this skill exists to prevent.

## Budgets (defaults; scale up only if the user asks for exhaustive coverage)

- 5 search angles (min 3, max 6)
- Top 4-6 results per angle, ranked by relevance to the ORIGINAL question
- Fetch at most 15 unique sources (dedup URLs first; prefer high-relevance)
- 2-5 falsifiable claims extracted per source
- Verify the top 25 claims (ranked central > supporting > tangential, then by source quality)
- 3 independent adversarial checks per claim; 2 or more refutations kill the claim

## Phase 1: Scope

Decompose the research question into 5 distinct web-search angles that together cover it from different directions. Pick angles that suit the domain, e.g.:

- General: broad/primary · academic/technical · recent news · contrarian/skeptical · practitioner/implementation
- Medical: anatomy · common causes · serious differentials · authoritative references · red flags
- Tech: state-of-art · benchmarks · limitations · industry adoption · cost/tradeoffs

Make each query specific enough to surface high-signal results. Avoid redundancy between angles. State the decomposition strategy in 1-2 sentences before searching.

## Phase 2: Search (fan out)

Run one web search per angle (refine the query if the first pass is weak). Keep the top 4-6 results per angle. Rank by relevance to the ORIGINAL question, not just the angle's query. Skip obvious SEO spam and content farms.

Then dedup across angles by normalized URL (ignore scheme, `www.`, port, trailing slash, query strings). Respect the 15-source fetch budget: when over budget, drop medium/low-relevance results first and note what was dropped. Silent truncation reads as "covered everything" when it didn't.

## Phase 3: Fetch & Extract

For each surviving source, fetch the page and:

1. **Assess source quality**: `primary` (original research, official docs, institutions) · `secondary` (reputable reporting) · `blog` (opinion) · `forum` (speculation) · `unreliable`.
2. **Extract 2-5 FALSIFIABLE claims** that bear on the research question. Each claim must:
   - be a concrete, checkable statement (not vague generalities),
   - include a direct supporting quote from the source,
   - be rated `central` / `supporting` / `tangential` to the question.
3. **Note the publish date** if available.

If a fetch fails or the page is irrelevant/paywalled, record the source as `unreliable` with zero claims and move on.

## Phase 4: Adversarial Verify (the heart of the skill)

Rank all claims (importance, then source quality) and verify the top 25. For EACH claim, run 3 independent adversarial checks. In each check, be SKEPTICAL and actively try to REFUTE the claim:

1. Is the claim actually supported by its quote, or is it an overreach/misread?
2. Search the web for contradicting evidence: does any credible source dispute or heavily qualify it?
3. Is the source quality sufficient for the claim's strength? (Extraordinary claims need primary sources.)
4. Is the claim outdated? (Check dates: old claims about fast-moving fields are suspect.)
5. Is this a marketing claim / press release / cherry-picked benchmark / forum speculation?

Verdict per check: **refuted** if unsupported by the quote, contradicted, low-quality source for a strong claim, outdated, or marketing fluff. **Not refuted** ONLY if well-supported, current, and source quality matches claim strength. Default to refuted when uncertain. Evidence must be specific (name the counter-source or the exact overreach).

Tally: a claim **survives** with fewer than 2 refutations out of 3; it is **killed** at 2 or more. Track the vote (e.g. 3-0, 2-1) per claim.

## Phase 5: Synthesize

1. Merge claims that say the same thing; combine their sources.
2. Group related surviving claims into coherent findings that directly address the research question.
3. Assign confidence per finding: **high** (multiple primary sources, unanimous votes) · **medium** (secondary sources or split votes) · **low** (single source or blog-quality).
4. Write a 3-5 sentence executive summary answering the question.
5. Note caveats: what is uncertain, which sources were weak, what time-sensitivity applies.
6. List 2-4 open questions that emerged but were not answered.

## Report format

- **Executive summary** (3-5 sentences, answers the question directly)
- **Findings**: each with confidence, supporting sources (linked), one-line evidence, and the verification vote
- **Refuted claims** (for transparency): the claim, its source, and why it died
- **Caveats & open questions**
- **Source table**: URL · quality rating · claims contributed

## Hard rules

- Never present a killed or unverified claim as a finding.
- Never cite a source you did not actually fetch.
- Distinguish what a product DOES vs what it ENABLES vs what a vendor CLAIMS.
- Can't find it? Say "not found". Don't hedge with "may exist".
- If every claim dies in verification, say the research was inconclusive and explain why (low-quality sources vs genuine contradiction). That is a valid result.
