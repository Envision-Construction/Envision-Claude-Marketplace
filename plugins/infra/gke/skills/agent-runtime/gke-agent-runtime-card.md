## Description: <br>
Run AI agents on GKE — K8s-native sandboxing (SandboxWarmPool/SandboxClaim CRDs), 5-agent autonomous pipelines (speccer→planner→builder→workers→reviewer), and memory-enabled ADK agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Third-Party Community Consideration
This skill is not owned or developed by NVIDIA. This skill has been developed and built to a third-party's requirements for this application and use case; see link to Non-NVIDIA [Envision Construction Agent Card](https://github.com/Envision-Construction/claude-code-memory). <br>

### License/Terms of Use: <br>
## Use Case: <br>
Developers and platform engineers deploying AI agents to GKE, setting up agent sandboxes, or building multi-agent systems on Kubernetes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Requirements / Dependencies: <br>
**Requires API Key or External Credential:** [Yes] <br>
**Credential Type(s):** [API key, Cloud Credentials] <br>  

Do not include secrets in prompts/logs/output; use least-privilege credentials; rotate keys as appropriate. See skill body for more details. <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Kubernetes SIGs agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) <br>
- [Agent Development Kit (ADK)](https://adk.dev/) <br>
- [ADK GKE deployment guide](https://adk.dev/deploy/gke/) <br>
- [Vertex AI Agent Engine Memory Bank overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank/overview) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Code] <br>
**Output Format:** [Markdown with inline bash and YAML code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
6a559120 (source: git SHA, committed 2026-07-25) <br>


