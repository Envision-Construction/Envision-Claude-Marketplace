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
| construction | `buildr` | Buildr CRM | 6 skills (pipeline, deals, accounts, activity, handoff) | first-party (ex claude-code-memory) |
| construction | `rabbet` | Rabbet | 1 skill + sync command (draws, budgets, pay apps) | first-party (ex claude-code-memory) |
| marketing | `brand` | Envision Brand | 3 skills (standard, design-system, pdf) | first-party (ex claude-code-memory) |
| finance | `fin-docs` | Finance Docs | 3 skills (EDGAR, earnings, venture-council) | first-party (ex claude-code-memory) |
| infra | `gke` | GKE AI Platform | 3 skills (dispatch, ai-platform, agent-runtime) | first-party (ex claude-code-memory) |
| legal | `general-counsel` | General Counsel | 11 skills + 14 agents | vendored from Envision-Construction/general-counsel |
| generative | `nano-banana-2` | Nano Banana 2 | Gemini image generation via MCP | fork of daveremy/nano-banana-2-mcp |

## Layout

```
plugins/
├── finance/
│   ├── credit/            skills/{analysis,process,sectors,reference}/…
│   ├── private-equity/    skills/{deals,portfolio}/…
│   └── fin-docs/          skills/{edgar-format,earnings-analysis,venture-council}
├── real-estate/
│   └── cre/               skills/{acquisition,transaction,ownership,sectors}/…
├── construction/
│   ├── buildr/            skills/{crm,account-360,activity-logging,deal-lifecycle,deal-to-project,pipeline-review}
│   └── rabbet/            skills/rabbet + commands/rabbet-sync
├── marketing/
│   └── brand/             skills/{standard,design-system,pdf}
├── infra/
│   └── gke/               skills/{dispatch,ai-platform,agent-runtime}
├── legal/
│   └── general-counsel/   skills/ (9 practice areas + insurance suite) + agents/
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
