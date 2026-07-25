## Description: <br>
Dispatch parallel task waves to GKE (claude-mcp-457317) — idempotent, checkpoint-based, for when 2+ independent tasks need parallel execution on GKE from any framework. <br>

This skill is ready for commercial/non-commercial use. <br>

## Third-Party Community Consideration
This skill is not owned or developed by NVIDIA. This skill has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Envision Construction Agent Card](https://github.com/Envision-Construction/claude-code-memory). <br>

### License/Terms of Use: <br>
## Use Case: <br>
Developers and engineers dispatching parallel work units from any orchestration framework to a GKE cluster with zero-drop guarantees and idempotent replay. <br>

### Deployment Geography for Use: <br>
Global <br>

## Requirements / Dependencies: <br>
**Requires API Key or External Credential:** [Yes] <br>
**Credential Type(s):** [OAuth Token, Cloud Credentials] <br>  

Do not include secrets in prompts/logs/output; use least-privilege credentials; rotate keys as appropriate. See skill body for more details. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [cluster-setup.md](references/cluster-setup.md) <br>
- [envision-mcp-integration.md](references/envision-mcp-integration.md) <br>
- [manifest-schema.md](references/manifest-schema.md) <br>
- [multi-phase-milestone.md](references/multi-phase-milestone.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON wave manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
6a559120 (source: git SHA, committed 2026-07-25) <br>


