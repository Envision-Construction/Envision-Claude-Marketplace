# Full Engagement Playbook — materials review / feasibility / indication-report critique

Use when the ask spans multiple specialist domains (e.g. "review these broker captive materials", "critique the indication report", "should we form, rent a cell, or stay conventional").

## 1. Gather (orchestrating session only)

- Retrieve source materials via envision-mcp (Gmail/Drive) **in the main session** — specialists never get gateway access.
- Save raw documents under a gitignored path (`memory/private/<engagement>-sources/`), one manifest file listing: filename, origin ID (Gmail msg / Drive file), date, one-line description, fetch status.
- Gotcha: `parse_document_on_demand` accepts only `gs://` URIs. The reliable path for email attachments is: `gmail_get_attachment` → save locally → native `Read` (PDF supported, use `pages`).
- Fold in internal context (prior memos, tax-counsel opinions, related memory files) by path.

## 2. Analyze (one parallel dispatch)

Dispatch all relevant specialists in a single message. **Synchronization contract** (a 2026-07-04 eval run hit this race): specialists may finish Writing their section files after their return message arrives, or return before the Write lands. Before synthesizing, the orchestrator verifies each expected section file EXISTS on disk (ls/Glob) and re-checks once after a short wait for any missing file — never conclude a section "never landed" from return-message timing alone. Each prompt carries:
- The section assignment (e.g. tax agent → Regulatory; structures agent → Legal-structural + domicile matrix; coverage-counsel → program mechanics / premium-finance exposure).
- **Pointers**: manifest path + the specific local file paths it must Read. Never paste document bodies into prompts.
- An output path to Write its full section, and an instruction to return a distilled summary under 500 words.
- The reminder: two-source rule, pinpoint + URL + verified-on citations, indexed figures re-verified, not-found is an answer.

## 3. Synthesize (main session)

- Read the section files, reconcile conflicts (note where specialists disagree and why).
- Run `Skill(pe-executive:pe-executive-mindset)` for the Strategy section — value creation, cash/EBITDA impact, risk-adjusted comparison of the structural options, negotiation leverage with brokers.
- Author the recommendation memo: cites all sections + `references/current-legislation.md`; separates Regulatory / Legal / Strategy; ends with the counsel/actuary escalation line.
- Deliverables live in `memory/projects/<engagement>/` with a MEMORY.md index and a source-manifest; update the top-level memory index.
