# Legislation Refresh — canonical deep-research question + staleness rule

## When to refresh

- `references/current-legislation.md` as-of date is older than **90 days**, OR
- the user asks about "current / latest / this year's" captive legislation, OR
- a specialist hits a fact the snapshot dates before a known pending change.

## How

Invoke `Skill(deep-research)` with the canonical question below (adjust the trailing year window to the run date). Distill the verified findings into `references/current-legislation.md` — do **not** paste the full research dump (keep the snapshot under ~450 lines). Archive the full report under `memory/private/` if needed. Append a dated entry to the snapshot's changelog section: what changed, what was checked and found unchanged. The changelog persists across snapshot replacements.

## Canonical question

> As of [RUN DATE], what is the current state of captive-insurance law and enforcement relevant to a US middle-market operating group evaluating captive formation? Cover, with primary-source citations and effective dates:
> 1. **Federal**: status and any litigation/amendment of the micro-captive final regulations (T.D. 10029, Jan 2025) — current listed-transaction and transaction-of-interest definitions (loss-ratio thresholds, financing factors, computation periods), disclosure duties under sections 6011/6111/6112, and section 6700 promoter-penalty enforcement; the current inflation-indexed section 831(b) premium cap (cite the Rev. Proc.); any 831(b)/831(a) statutory amendments enacted or pending in the current Congress; IRS settlement-initiative status; significant Tax Court / appellate captive decisions in the last 24 months.
> 2. **State domiciles** — Georgia (O.C.G.A. Title 33 Ch. 41), Vermont, Tennessee, South Carolina, North Carolina, Delaware, Utah: captive-statute amendments in the last 24 months (new cell provisions, capital requirements, premium-tax changes, redomestication rules), plus each domicile's current minimum capital for pure and cell captives.
> 3. **Offshore** — Bermuda and Cayman: regulatory changes affecting US-owned captives (BMA / CIMA rules, economic-substance requirements), and the current mechanics/considerations of the IRC 953(d) election.
> 4. **Premium finance**: any recent state or federal changes to premium-finance-company regulation that affect captive or conventional program funding.
> Rank findings by relevance to a formation decision being made now; flag anything effective within the next 12 months.

## Snapshot format contract

`references/current-legislation.md` must keep:
- Line 1 header, then `> As of: YYYY-MM-DD — methodology: deep-research run, primary sources, two-source verified.`
- Sections: Federal / per-domicile (GA, VT, TN, SC, NC, DE, UT) / Offshore (Bermuda, Cayman, 953(d)) / Premium finance.
- Every claim: pinpoint cite + canonical URL + verified-on date.
- `## Re-audit changelog` at the bottom — append-only, dated entries.
