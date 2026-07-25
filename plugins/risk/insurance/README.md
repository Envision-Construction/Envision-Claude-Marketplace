# insurance

Forensic insurance-industry research plugin: the `specialist` orchestrator skill plus four dispatchable specialist agents (`captive-tax`, `captive-structures`, `coverage-counsel`, `statute-researcher`).

- Evergreen references verified against primary sources 2026-07-04; the dated snapshot `skills/specialist/references/current-legislation.md` carries its own as-of header and a refresh protocol (`workflows/legislation-refresh.md`) — refresh if older than 90 days.
- Web research is firecrawl-first with WebFetch/WebSearch fallback; agents degrade gracefully if firecrawl MCP is absent.
- Outputs are compliance-risk decision support, never legal/tax advice; every deliverable ends with a licensed-counsel escalation line.
- NOTE for machines running the claude-code-memory config repo: the canonical copy lives repo-native at global/skills + global/agents. Do NOT also enable this plugin there — skill-id dedup would shadow the canonical copy.
