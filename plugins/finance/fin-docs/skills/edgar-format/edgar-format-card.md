## Description: <br>
Restyle any document (xlsx, docx, csv, md, txt, html, pdf, json) so it looks forensically like a modern SEC EDGAR 10-K / 10-Q filing, emitting output in the same format as the input. <br>

This skill is ready for commercial/non-commercial use. <br>

## Third-Party Community Consideration
This skill is not owned or developed by NVIDIA. This skill has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Envision Construction Agent Card](https://github.com/Envision-Construction/claude-code-memory). <br>

### License/Terms of Use: <br>
## Use Case: <br>
Internal Envision / Prometheus Ventures staff use it to style mock filings, prospectus drafts, and investor memos so they visually match real SEC EDGAR filings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Requirements / Dependencies: <br>
**Requires API Key or External Credential:** [Not Specified] <br>
**Credential Type(s):** [None identified] <br>  

Do not include secrets in prompts/logs/output; use least-privilege credentials; rotate keys as appropriate. See skill body for more details. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [financial-statements.md](references/financial-statements.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files] <br>
**Output Format:** [Restyled document emitted in the same format as the input (xlsx, docx, pdf, html, etc.)] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [If extract.py cannot infer fields (e.g., a bare CSV has no registrant name), it leaves them null.] <br>

## Skill Version(s): <br>
6a559120 (source: git SHA, committed 2026-07-25) <br>


