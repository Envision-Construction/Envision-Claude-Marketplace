# GKE Cluster Setup — Remediation Reference

This file is NOT a prerequisite checklist. The dispatch scripts auto-detect what's available
and only fail with actionable errors. This file exists as a fix-it reference — consult it
only when a script tells you something is missing.

## Error: "kubectl: command not found" or cluster unreachable

```bash
gcloud container clusters get-credentials <CLUSTER_NAME> \
  --zone <ZONE> \
  --project claude-mcp-457317
```

## Error: namespace "gke-dispatch" not found

```bash
kubectl create namespace gke-dispatch
```

## Error: GCS bucket does not exist

```bash
gsutil mb -p claude-mcp-457317 -l us-central1 gs://gke-dispatch-claude-mcp-457317
gsutil lifecycle set <(cat <<'EOF'
{"rule": [{"action": {"type": "Delete"}, "condition": {"age": 30}}]}
EOF
) gs://gke-dispatch-claude-mcp-457317
```

## Error: permission denied writing to GCS from pod

Set up Workload Identity so pods can write results:

```bash
gcloud iam service-accounts create gke-dispatch-sa \
  --display-name="GKE Dispatch Worker" \
  --project claude-mcp-457317

gcloud projects add-iam-policy-binding claude-mcp-457317 \
  --member="serviceAccount:gke-dispatch-sa@claude-mcp-457317.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"

kubectl create serviceaccount gke-dispatch-worker -n gke-dispatch
gcloud iam service-accounts add-iam-policy-binding \
  gke-dispatch-sa@claude-mcp-457317.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:claude-mcp-457317.svc.id.goog[gke-dispatch/gke-dispatch-worker]"
kubectl annotate serviceaccount gke-dispatch-worker -n gke-dispatch \
  iam.gke.io/gcp-service-account=gke-dispatch-sa@claude-mcp-457317.iam.gserviceaccount.com
```

## Optional: resource quotas

Only if you want to cap what gke-dispatch can consume:

```bash
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: ResourceQuota
metadata:
  name: gke-dispatch-quota
  namespace: gke-dispatch
spec:
  hard:
    requests.cpu: "64"
    requests.memory: 128Gi
    limits.cpu: "128"
    limits.memory: 256Gi
    count/jobs.batch: "100"
EOF
```

## Optional: pre-warmed pod pool (high-frequency mode)

Only needed if dispatching waves faster than 1/min:

```bash
kubectl apply -f - <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: task-runner-pool
  namespace: gke-dispatch
spec:
  replicas: 4
  selector:
    matchLabels:
      app: gke-dispatch-runner
  template:
    metadata:
      labels:
        app: gke-dispatch-runner
    spec:
      serviceAccountName: gke-dispatch-worker
      containers:
      - name: runner
        image: gcr.io/claude-mcp-457317/gke-dispatch-runner:latest
        env:
        - name: GCS_BUCKET
          value: gke-dispatch-claude-mcp-457317
        - name: QUEUE_TYPE
          value: pubsub
        resources:
          requests:
            cpu: "2"
            memory: 4Gi
          limits:
            cpu: "4"
            memory: 8Gi
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: task-runner-hpa
  namespace: gke-dispatch
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: task-runner-pool
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: External
    external:
      metric:
        name: pubsub.googleapis.com|subscription|num_undelivered_messages
      target:
        type: AverageValue
        averageValue: "5"
EOF
```
