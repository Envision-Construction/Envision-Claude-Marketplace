---
type: index
title: General Counsel shared contracts
description: Map of the four contract files every GC surface (deployed service, plugin skills, specialist agents) binds to.
resource: plugin/skills/_shared/
tags: [legal, contracts, zero-fabrication]
timestamp: 2026-07-04
---

# _shared/ — binding contracts (OKF-style index)

| Doc | type | What it binds |
|---|---|---|
| [zero-fabrication.md](zero-fabrication.md) | policy | No fabricated authorities, docket numbers, or rule text — ever. Unverifiable ⇒ "ASSUMPTION (unverified)". |
| [output-format.md](output-format.md) | policy | Conclusion-first memo shape: verdict, badged citations, RISK/CONFIDENCE, limitations. |
| [ontology.md](ontology.md) | reference | Business-dimension layer (first-principles / PE lens) and its grounding rules. |
| [supervisor.md](supervisor.md) | prompt | The GENERAL_COUNSEL supervisor: classify → fan-out → synthesis routing table. |

These four files are read by `app/agents/prompts.py` at import — they ARE the
production prompts. This index is inert to the loader (it reads only the four
named files) and exists so knowledge consumers (Claude Code, OKF-compatible
catalogs) can discover the contracts. Frontmatter follows Google's Open
Knowledge Format v0.1 draft (type/title/description/resource) — compatible,
not dependent.
