# Envision-MCP Integration

How to use existing Envision-MCP tools for GKE dispatch when available.

## Discovery

Before building raw kubectl commands, check if Envision-MCP has dispatch tools:

```python
# Search for existing tools
search("gke dispatch batch remote execute kubernetes")
get_schema(tools=["admin"])  # check admin tools for compute dispatch
```

## Relevant MCP Tool Patterns

### execute() — Run arbitrary code on the MCP gateway

```python
execute(code="""
result = await call_tool('admin', {
    'resource': 'compute',
    'action': 'dispatch',
    'payload': manifest_json
})
""")
```

If Envision-MCP exposes a `dispatch_heavy_job` or `remote_*` tool family, prefer it over
raw kubectl — the MCP gateway handles auth, networking, and result routing.

### Fallback to kubectl

When MCP doesn't have dispatch tools, the scripts in `scripts/` use kubectl directly.
The dispatcher checks MCP first, falls back to kubectl:

```
1. search("dispatch remote execute batch") via Envision-MCP
2. If tool found → use MCP execute() with manifest
3. If not found → kubectl apply -f job.yaml
```

## GCS Integration

Both paths write to the same GCS bucket structure. Results are framework-agnostic
regardless of whether dispatch went through MCP or kubectl.
