# Envision Skill Repo

Envision-Construction's Claude Code plugin registry (marketplace id: `envision-skill-repo`). Org-owned plugins grouped by domain; forked plugins carry upstream lineage in their descriptions and are decoupled from upstream merge timing.

## Install

```bash
claude plugin marketplace add Envision-Construction/Envision-Skill-Repo
claude plugin install credit@envision-skill-repo     # or pe, cre, insurance, deep-research, nano-banana-2
```

## Catalog

| Category | Plugin | Display Name | Contents | Lineage |
|---|---|---|---|---|
| finance | `credit` | Credit Investment Analysis | 14 skills (analysis / process / sectors / reference), 2 agents, 1 hook | jeickmeier/credit-investment-analysis-plugin v1.3.0 (MIT) |
| finance | `pe` | Private Equity | 10 skills (deals / portfolio) | anthropics/financial-services v0.1.2 (Apache-2.0) |
| real-estate | `cre` | CRE Dealmaking | 9 skills (acquisition / transaction / ownership / sectors) with knowledge bases | Envision-Construction/CRE-Dealmaking-Skills, orig. ahacker-1 (Apache-2.0) |
| risk | `insurance` | Envision Insurance | 1 orchestrator skill, 4 specialist agents | first-party |
| research | `deep-research` | Deep Research | 1 skill (adversarially-verified research pipeline) | first-party |
| generative | `nano-banana-2` | Nano Banana 2 | Gemini image generation via MCP | fork of daveremy/nano-banana-2-mcp |

## Layout

```
plugins/
├── finance/
│   ├── credit/            skills/{analysis,process,sectors,reference}/…
│   └── private-equity/    skills/{deals,portfolio}/…
├── real-estate/
│   └── cre/               skills/{acquisition,transaction,ownership,sectors}/…
├── risk/
│   └── insurance/         skills/specialist + agents/
├── research/
│   └── deep-research/     skills/deep-research
└── generative/
    └── nano-banana-2/     MCP image generation
```

Skill ids are `plugin:leaf-dir` — the group folders organize the tree without lengthening ids (e.g. `credit:memo-generator`, `pe:ic-memo`, `cre:underwriting`, `insurance:specialist`).

## Conventions

- Plugin `name` = short kebab-case id (it prefixes every skill id — keep it short).
- `displayName` (plugin.json + marketplace entry) carries the Title Case title.
- `SKILL.md` frontmatter `name:` = Title Case display name; the directory name is the invocation id.
- Grouped skills are declared explicitly via the `skills` array in plugin.json (group dirs are not auto-discovered).
- Forked plugins keep upstream LICENSE in the plugin dir and upstream attribution in `author`/`homepage`.
