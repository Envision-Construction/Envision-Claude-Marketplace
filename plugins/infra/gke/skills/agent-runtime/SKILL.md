---
name: GKE Agent Runtime
description: Run AI agents on GKE — K8s-native sandboxing (SandboxWarmPool/SandboxClaim CRDs), 5-agent autonomous pipelines (speccer→planner→builder→workers→reviewer), and memory-enabled ADK agents. Use when deploying agents to GKE, setting up agent sandboxes, or building multi-agent systems on Kubernetes.
---

# GKE Agent Runtime

Three patterns for running AI agents on GKE, from isolated sandbox pods to full
autonomous development pipelines with persistent memory. All target GKE in
project `claude-mcp-457317`.

Source repos:
- `~/GitHub/ai-on-gke/ai-factory/` (sandbox CRDs, multi-agent pipeline)
- `~/GitHub/generative-ai/agents/gke/agents_with_memory/` (ADK + Memory Bank)

---

## Part 1: Agent Sandbox — Isolated K8s Execution

Deploy isolated, Kubernetes-native agent execution environments using the
`kubernetes-sigs/agent-sandbox` CRDs. Each agent runs in its own sandboxed pod
with network isolation, resource limits, and optional warm pools.

### Installation

```bash
# 1. cert-manager (required by sandbox controller)
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml
kubectl wait --for=condition=Available deployment/cert-manager -n cert-manager --timeout=120s

# 2. Agent sandbox controller + CRDs
TMP_DIR=$(mktemp -d)
git clone https://github.com/kubernetes-sigs/agent-sandbox.git "$TMP_DIR"
cd "$TMP_DIR"
PROJECT_ID="claude-mcp-457317"
./dev/tools/push-images --image-prefix="gcr.io/${PROJECT_ID}/" --controller-only
./dev/tools/deploy-to-kube --image-prefix="gcr.io/${PROJECT_ID}/" --extensions
cd - && rm -rf "$TMP_DIR"

# 3. (Optional) Service portals for in-cluster LLM API access
TMP_DIR=$(mktemp -d)
git clone https://github.com/gke-labs/service-portals.git "$TMP_DIR"
cd "$TMP_DIR"
IMAGE_PREFIX="gcr.io/claude-mcp-457317" go run github.com/gke-labs/gke-labs-infra/ap@latest deploy //...
cd - && rm -rf "$TMP_DIR"
```

### CRD Reference

**Sandbox** — single isolated agent pod:

```yaml
apiVersion: agents.x-k8s.io/v1alpha1
kind: Sandbox
metadata:
  name: my-agent-sandbox
spec:
  podTemplate:
    spec:
      containers:
      - name: agent
        image: gcr.io/claude-mcp-457317/ai-on-gke-agent:latest
        env:
        - name: AGENT_NAME
          value: my-agent
        resources:
          requests:
            cpu: "500m"
            memory: "512Mi"
          limits:
            cpu: "2"
            memory: "2Gi"
      restartPolicy: Always
```

**SandboxWarmPool** — pre-warmed pods for near-instant startup:

```yaml
apiVersion: agents.x-k8s.io/v1alpha1
kind: SandboxWarmPool
metadata:
  name: agent-warm-pool
spec:
  replicas: 3
  template:
    spec:
      podTemplate:
        spec:
          containers:
          - name: agent
            image: gcr.io/claude-mcp-457317/ai-on-gke-agent:latest
            resources:
              requests:
                cpu: "500m"
                memory: "512Mi"
```

**SandboxClaim** — request a sandbox from a warm pool (PVC/PV pattern):

```yaml
apiVersion: agents.x-k8s.io/v1alpha1
kind: SandboxClaim
metadata:
  name: build-task-claim
spec:
  warmPoolRef:
    name: agent-warm-pool
  env:
  - name: TASK_ID
    value: "task-42"
```

**SandboxTemplate** — reusable sandbox configuration:

```yaml
apiVersion: agents.x-k8s.io/v1alpha1
kind: SandboxTemplate
metadata:
  name: standard-agent
spec:
  podTemplate:
    spec:
      containers:
      - name: agent
        image: gcr.io/claude-mcp-457317/ai-on-gke-agent:latest
        resources:
          requests: { cpu: "1", memory: "1Gi" }
          limits: { cpu: "4", memory: "4Gi" }
      securityContext:
        runAsNonRoot: true
```

### Operations

```bash
kubectl apply -f sandbox.yaml          # Create sandbox
kubectl get sandboxes                   # List all
kubectl logs -l agent=builder -f       # Stream logs
kubectl patch sandboxwarmpool agent-warm-pool -p '{"spec":{"replicas":10}}'  # Scale pool
kubectl delete sandbox my-agent-sandbox # Clean up
```

### Integration with gke-dispatch

1. Create a `SandboxWarmPool` sized to parallelism level
2. Each task gets a `SandboxClaim` from the pool
3. Artifacts collected via shared PVC or GCS bucket
4. Sandboxes released back to pool on completion

### Security

- Each sandbox runs in its own pod with its own network namespace
- Use `NetworkPolicy` to restrict sandbox-to-sandbox communication
- Service portals provide controlled API access without direct egress
- `securityContext.runAsNonRoot: true` prevents root execution

---

## Part 2: AI Factory — 5-Agent Autonomous Pipeline

A self-assembling multi-agent system: speccer → planner → builder → workers → reviewer.
Extracted from Google's AI Factory experiment.

### Architecture

```
top-level (orchestrator)
  │
  ▼
speccer ──specs/──► planner ──plans/──► builder ──► worker(s) ──PR──► reviewer
                                                                       │
                                                               ┌───────┴────────┐
                                                               spec-format    plan-format
                                                               (guard sub-agents)
```

### Agent Definitions

Each agent lives in `.agents/<name>/agent.md` with YAML frontmatter:

```markdown
---
name: speccer
description: Translates ideas into structured specs
model: gemini-3.1-pro  # or claude-opus-4-7
tools: [Read, Write, Edit, Grep]
---
```

**Speccer** writes specs to `specs/` with frontmatter (`name`, `deps`), goals,
non-goals, design, tests. **Planner** reads specs and produces `plan.yaml` —
a DAG of tasks with `deps` and `out` file lists. **Builder** topologically sorts
the DAG and spawns workers in parallel where dependencies allow. **Workers**
execute individual tasks. **Reviewer** auto-reviews PRs using guard-conditioned
sub-agents (spec-format, plan-format validators).

### Spec Template

```markdown
---
name: my-feature
deps: [prerequisite-spec]
---
# Feature Title
## Overview / Goals / Non-Goals / Design / Tests
```

### Plan Template (plan.yaml)

```yaml
name: create-api-routes
spec: api-design
deps: []
out:
  - src/routes/api.ts
---
name: add-tests
spec: api-design
deps: [create-api-routes]
out:
  - tests/api.test.ts
```

### SOUL.md and AGENTS.md

`SOUL.md` at repo root defines project-level values (self-assembly, K8s-native,
continuous evolution, resilience). `AGENTS.md` is shared knowledge — architecture
decisions, component locations, event triggers. Agents MUST update AGENTS.md
when making architectural decisions.

### Reviewer Guard Pattern

```markdown
---
name: spec-format
guard: The PR includes new specs in the specs/ directory
success: The specs pass
---
- Validate each spec with `tool spec validate [name]`
- Output JSON: { name, result: "PASS"|"FAIL", summary }
```

### Claude Code Adaptation

1. Change `model` to `claude-opus-4-7` or `claude-sonnet-4-6`
2. Replace Gemini Service Portal with `ANTHROPIC_API_KEY`
3. Use Claude Code's `Agent` tool for worker dispatch
4. Keep the spec/plan/build/review cycle — it's model-agnostic

---

## Part 3: ADK Agents with Memory on GKE

Deploy Google ADK agents with Vertex AI Sessions (short-term) and Memory Bank
(long-term) on GKE. Agents remember across sessions without managing your own DB.

### Step 1: Register Agent Engine (for Sessions + Memory Bank only)

```python
import vertexai

PROJECT_ID = "claude-mcp-457317"
LOCATION = "us-central1"

client = vertexai.Client(project=PROJECT_ID, location=LOCATION)
agent_engine = client.agent_engines.create(config={
    "display_name": "my_agent",
    "context_spec": {
        "memory_bank_config": {
            "generation_config": {
                "model": f"projects/{PROJECT_ID}/locations/{LOCATION}"
                         f"/publishers/google/models/gemini-2.5-flash"
            }
        }
    },
})
agent_engine_id = agent_engine.api_resource.name.split("/")[-1]
```

### Step 2: Agent Code with Memory

```python
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

async def add_session_to_memory(callback_context: CallbackContext):
    if hasattr(callback_context, "_invocation_context"):
        ctx = callback_context._invocation_context
        if ctx.memory_service:
            await ctx.memory_service.add_session_to_memory(ctx.session)

root_agent = Agent(
    name="my_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful agent. Use memories from prior sessions.",
    tools=[PreloadMemoryTool()],
    after_agent_callback=add_session_to_memory,
)
```

### Step 3: Deploy to GKE

```bash
# IAM for Workload Identity
PROJECT_NUMBER=$(gcloud projects describe claude-mcp-457317 --format="value(projectNumber)")
gcloud projects add-iam-policy-binding claude-mcp-457317 \
  --role=roles/aiplatform.user \
  --member="principal://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/claude-mcp-457317.svc.id.goog/subject/ns/default/sa/default"

# Deploy
adk deploy gke \
  --project claude-mcp-457317 --region us-central1 \
  --cluster_name my-agent-cluster --service_name my-agent \
  --session_service_uri=agentengine://${AGENT_ENGINE_ID} \
  --memory_service_uri=agentengine://${AGENT_ENGINE_ID} \
  --app_name my_agent --with_ui .

kubectl get pods -l=app=my-agent
```

Cloud Run alternative:

```bash
adk deploy cloud_run \
  --project claude-mcp-457317 --region us-central1 \
  --service_name my-agent \
  --session_service_uri=agentengine://${AGENT_ENGINE_ID} \
  --memory_service_uri=agentengine://${AGENT_ENGINE_ID} \
  --app_name my_agent --with_ui . \
  -- --no-allow-unauthenticated
```

### Memory Tools

| Tool | Behavior |
|---|---|
| `PreloadMemoryTool` | Auto-fetches memories each turn (system instructions) |
| `LoadMemoryTool` | Agent decides when to fetch (on-demand tool call) |

### Session Services

| Service | Persistence | Use case |
|---|---|---|
| `InMemorySessionService` | None | Dev/testing |
| `DatabaseSessionService` | SQL | Self-hosted prod |
| `VertexAiSessionService` | Managed | Production |

### Cleanup

```python
client.agent_engines.delete(
    name=f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{agent_engine_id}",
    force=True,
)
```

---

## References

- [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
- [ADK documentation](https://adk.dev/)
- [Vertex AI Memory Bank](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank/overview)
- [Deploy ADK to GKE](https://adk.dev/deploy/gke/)
- Source: `~/GitHub/ai-on-gke/ai-factory/`, `~/GitHub/generative-ai/agents/gke/`
