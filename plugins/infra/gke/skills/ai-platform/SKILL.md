---
name: GKE AI Platform
description: Production GKE AI platform — cluster provisioning (Terraform), GPU batch scheduling (Kueue), model inference serving (vLLM/TGI), and parallel task dispatch. Use when deploying AI infrastructure, GPU workloads, model serving, or parallel agent execution on GKE.
---

# GKE AI Platform

Unified skill for production AI infrastructure on Google Kubernetes Engine.
Target project: `claude-mcp-457317`. Sources: `~/GitHub/ai-on-gke/`, `~/GitHub/gcp-ai-on-gke/`.

---

## Part 1 — Cluster Provisioning (Terraform)

### Cluster type decision

| Need | Type | Module |
|------|------|--------|
| Full GPU/TPU control | Standard Private | `gke-standard-private-cluster` |
| Managed scaling, no node pool mgmt | Autopilot Private | `gke-autopilot-private-cluster` |
| Dev/test | Standard or Autopilot Public | `gke-*-public-cluster` |

Production AI workloads: **Standard Private**.

### Network foundation

```hcl
resource "google_compute_network" "network" {
  project                 = var.project_id
  name                    = "ai-network"
  auto_create_subnetworks = false
  routing_mode            = "GLOBAL"
}

resource "google_compute_subnetwork" "subnet" {
  name                     = "ai-subnet"
  ip_cidr_range            = "10.128.0.0/20"
  region                   = "us-central1"
  private_ip_google_access = true
  network                  = google_compute_network.network.name
  project                  = var.project_id
}

resource "google_compute_global_address" "psa_range" {
  project       = var.project_id
  name          = "google-managed-services-${google_compute_network.network.name}"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 16
  network       = google_compute_network.network.self_link
}

resource "google_service_networking_connection" "psa" {
  network                 = google_compute_network.network.self_link
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.psa_range.name]
  deletion_policy         = "ABANDON"
}

module "cloud-nat" {
  source        = "terraform-google-modules/cloud-nat/google"
  version       = "5.0.0"
  region        = "us-central1"
  project_id    = var.project_id
  create_router = true
  router        = "ai-network-router"
  name          = "cloud-nat-ai-network-router"
  network       = google_compute_network.network.name
}
```

### GKE cluster

```hcl
module "gke" {
  source  = "terraform-google-modules/kubernetes-engine/google//modules/private-cluster"
  version = "33.0.0"

  project_id  = var.project_id
  name        = "envision-ai"
  region      = "us-central1"
  regional    = true
  zones       = ["us-central1-a", "us-central1-b", "us-central1-c"]
  network     = google_compute_network.network.name
  subnetwork  = google_compute_subnetwork.subnet.name

  enable_private_endpoint = true
  enable_private_nodes    = true
  master_ipv4_cidr_block  = "172.16.0.0/28"
  master_authorized_networks = [{
    cidr_block   = "10.128.0.0/20"
    display_name = "ai-subnet"
  }]

  kubernetes_version                   = "1.34"
  release_channel                      = "REGULAR"
  remove_default_node_pool             = true
  deletion_protection                  = false
  gcs_fuse_csi_driver                  = true
  datapath_provider                    = "ADVANCED_DATAPATH"
  monitoring_enable_managed_prometheus = true
  logging_enabled_components           = ["SYSTEM_COMPONENTS", "WORKLOADS"]

  ray_operator_config = {
    enabled            = true
    logging_enabled    = true
    monitoring_enabled = true
  }

  node_pools = concat(var.cpu_pools, var.gpu_pools)
}
```

### Node pool definitions

```hcl
variable "cpu_pools" {
  default = [{
    name = "cpu-pool", machine_type = "n1-standard-16"
    autoscaling = true, min_count = 1, max_count = 5
    disk_size_gb = 100, disk_type = "pd-standard"
  }]
}

variable "gpu_pools" {
  default = [{
    name = "gpu-pool-l4", machine_type = "g2-standard-24"
    node_locations = "us-central1-a,us-central1-b"
    autoscaling = true, min_count = 0, max_count = 4
    disk_size_gb = 200, disk_type = "pd-ssd"
    accelerator_count = 2, accelerator_type = "nvidia-l4"
    gpu_driver_version = "LATEST", local_ssd_count = 1
    enable_gcfs = true
  }]
}
```

H100 training pool: `a3-highgpu-8g`, `nvidia-h100-80gb`, `accelerator_count = 8`, `spot = true`.
TPU pool: `ct5lp-hightpu-4t`, `tpu-v5-lite-podslice`, `accelerator_count = 4`.

### Quick-start tfvars

```hcl
project_id      = "claude-mcp-457317"
cluster_name    = "envision-ai"
cluster_location = "us-central1"
private_cluster = true
enable_gpu      = true
gcs_fuse_csi_driver = true
ray_addon_enabled   = true
```

### Key patterns

- **GPU zone pinning**: Always set `node_locations` — random zone selection causes quota failures
- **Spot for training**: 60-91% cost savings; use `spot = true` on training pools
- **GCS Fuse CSI**: Mount GCS buckets as volumes for model weights and datasets
- **Progress deadline**: `progressDeadlineSeconds = 1800` for GPU deployments (Autopilot can take 10+ min)

---

## Part 2 — GPU Batch Scheduling (Kueue)

Multi-tenant batch platform with cost-optimized GPU scheduling: **Reserved → On-demand → Spot**.

### ResourceFlavors (one per node pool tier)

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: gpu-l4-reserved
spec:
  nodeLabels:
    cloud.google.com/gke-accelerator: nvidia-l4
    resource-type: reservation
  nodeTaints:
    - effect: NoSchedule
      key: nvidia.com/gpu
      value: "true"
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: gpu-l4-ondemand
spec:
  nodeLabels:
    cloud.google.com/gke-accelerator: nvidia-l4
    resource-type: ondemand
  nodeTaints:
    - effect: NoSchedule
      key: nvidia.com/gpu
      value: "true"
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: gpu-l4-spot
spec:
  nodeLabels:
    cloud.google.com/gke-accelerator: nvidia-l4
    cloud.google.com/gke-provisioning: spot
    resource-type: spot
  nodeTaints:
    - effect: NoSchedule
      key: nvidia.com/gpu
      value: "true"
```

### PriorityClasses

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority-preempting
value: 20
preemptionPolicy: PreemptLowerPriority
---
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: default-priority-nonpreempting
value: 10
preemptionPolicy: Never
globalDefault: true
```

### ClusterQueue (high-priority team queue)

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: cq-team-a-hp
spec:
  cohort: all-teams
  queueingStrategy: StrictFIFO
  preemption:
    reclaimWithinCohort: LowerPriority
    withinClusterQueue: LowerPriority
  namespaceSelector:
    matchLabels:
      kubernetes.io/metadata.name: team-a
  resourceGroups:
    - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
      flavors:
        - name: gpu-l4-reserved
          resources:
            - name: "nvidia.com/gpu"
              nominalQuota: 4
              borrowingLimit: 0
        - name: gpu-l4-ondemand
          resources:
            - name: "nvidia.com/gpu"
              nominalQuota: 4
              borrowingLimit: 4
```

### LocalQueue + namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: team-a
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: LocalQueue
metadata:
  namespace: team-a
  name: lq-team-a-hp
spec:
  clusterQueue: cq-team-a-hp
```

### DWS (all-or-nothing GPU provisioning)

For large training jobs needing all GPUs simultaneously:

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: AdmissionCheck
metadata:
  name: dws-prov
spec:
  controllerName: kueue.x-k8s.io/provisioning-request
  parameters:
    apiGroup: kueue.x-k8s.io
    kind: ProvisioningRequestConfig
    name: dws-config
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ProvisioningRequestConfig
metadata:
  name: dws-config
spec:
  provisioningClassName: queued-provisioning.gke.io
  managedResources:
    - nvidia.com/gpu
```

### Key patterns

- **Reservation-first**: List reserved flavor first in ClusterQueue — Kueue tries in order
- **Cohort borrowing**: Teams share unused quota; `borrowingLimit` caps borrowing
- **Preemption flow**: HP arrives → evicts LP from reserved → LP moves to spot → spot scales up

```bash
kubectl get clusterqueues -o wide
kubectl get workloads -A
```

---

## Part 3 — Model Inference Serving

### TGI deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: model-inference
  namespace: inference
spec:
  replicas: 1
  progressDeadlineSeconds: 1800
  selector:
    matchLabels:
      app: model-inference
  template:
    spec:
      initContainers:
      - name: download-model
        image: google/cloud-sdk:473.0.0-alpine
        command: ["gsutil", "cp", "-r", "gs://your-model-bucket/model/", "/model-data/"]
        volumeMounts:
        - mountPath: /model-data
          name: model-storage
      containers:
      - name: tgi
        image: ghcr.io/huggingface/text-generation-inference:1.4.3
        args: ["--model-id", "/model/model-name"]
        env:
        - name: NUM_SHARD
          value: "2"
        resources:
          requests:
            nvidia.com/gpu: "2"
            ephemeral-storage: "20Gi"
          limits:
            nvidia.com/gpu: "2"
        volumeMounts:
        - mountPath: /dev/shm
          name: dshm
        - mountPath: /model
          name: model-storage
          readOnly: true
      volumes:
      - name: dshm
        emptyDir:
          medium: Memory
      - name: model-storage
        emptyDir: {}
      nodeSelector:
        cloud.google.com/gke-accelerator: nvidia-l4
```

### vLLM alternative

```yaml
containers:
- name: vllm
  image: vllm/vllm-openai:latest
  args: ["--model=/model/model-name", "--tensor-parallel-size=2", "--port=8080"]
  resources:
    requests:
      nvidia.com/gpu: "2"
    limits:
      nvidia.com/gpu: "2"
```

### GCS FUSE (skip init container)

```yaml
volumes:
- name: model-gcs
  csi:
    driver: gcsfuse.csi.storage.gke.io
    readOnly: true
    volumeAttributes:
      bucketName: "your-model-bucket"
```

### Cold-start optimization

| Technique | Impact | Command |
|-----------|--------|---------|
| Image streaming | ~190s → ~30s | `gcloud container clusters update CLUSTER --enable-image-streaming` |
| Local SSD | 3-8x throughput | `--ephemeral-storage-local-ssd count=1` on node pool |
| Preloader DaemonSet | Eliminates pull time | Deploy DaemonSet with `sleep inf` on GPU nodes |
| zstd compression | 3x faster decompression | Build with `--output compression=zstd,compression-level=3` |

### HPA with GPU metrics

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: inference-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: model-inference
  minReplicas: 1
  maxReplicas: 8
  metrics:
  - type: Pods
    pods:
      metric:
        name: inference_requests_per_second
      target:
        type: AverageValue
        averageValue: "50"
```

### Hotswap (high availability)

Apply `priorityClassName: high-priority-inference` (value 2000000) to inference; `low-priority-batch` (value 1000000) to batch. On node failure, GKE reschedules inference pods by preempting batch.

---

## Part 4 — Parallel Task Dispatch

Lossless parallel wave executor for any agentic framework (GSD, Ralph Loop, BMAD, etc.).

### Architecture

```
Framework (GSD/Ralph/any)
  ├─ normalize_wave() → Wave Manifest (JSON)
  ├─ dispatch_wave()  → GKE cluster (claude-mcp-457317)
  │   ├─ Upload inputs to GCS
  │   ├─ Idempotent guard (skip completed tasks)
  │   └─ K8s Indexed Job or pod pool
  ├─ poll_wave()      → Watch GCS for result.json per task
  └─ collect_results()→ Aggregated results back to framework
```

### Quick start

```bash
python3 scripts/normalize_wave.py \
  --wave-id "phase-3-wave-2" \
  --tasks '[{"id": "task-0", "cmd": "python analyze.py", "image": "gcr.io/claude-mcp-457317/analyst:latest"}]' \
  --output /tmp/wave-manifest.json

python3 scripts/dispatch.py \
  --manifest /tmp/wave-manifest.json \
  --bucket gs://gke-dispatch-claude-mcp-457317 \
  --namespace gke-dispatch --mode auto

python3 scripts/collect.py \
  --manifest /tmp/wave-manifest.json \
  --bucket gs://gke-dispatch-claude-mcp-457317 --timeout 900
```

### Compute modes

| Mode | Best for | Cold start |
|------|----------|------------|
| `indexed-job` | < 50 tasks, > 30s each | 3-8s |
| `pod-pool` | > 1 wave/min, < 30s tasks | 0s (pre-warmed) |
| `auto` | Mixed | Adaptive |

### Resource profiles

| Profile | CPU | Memory | GPU |
|---------|-----|--------|-----|
| `light` | 0.5 | 512Mi | — |
| `standard` | 2 | 4Gi | — |
| `heavy` | 8 | 16Gi | — |
| `gpu` | 4 | 16Gi | 1×T4 |

### GSD integration

```python
for plan in wave.independent_plans:
    tasks.append({
        "id": plan.name,
        "cmd": f"claude-code --plan {plan.path} --worktree {plan.branch}",
        "image": "avireddy0/claude-executor:latest",
        "inputs": {"plan_path": plan.path, "git_sha": current_sha},
        "resource_profile": "standard"
    })
```

### Full roadmap execution

```bash
python3 scripts/run_roadmap.py \
  --planning-dir .planning \
  --bucket gs://gke-dispatch-claude-mcp-457317 \
  --auto
```

Phases run sequentially; waves within each phase run in parallel on GKE. `--resume` picks up from checkpoint.

### Lossless guarantees

| Guarantee | Mechanism |
|-----------|-----------|
| No dropped tasks | Manifest tracks every task; orphan detector flags missing terminal states |
| Full output capture | Sidecar ships stdout/stderr/artifacts to GCS |
| Idempotent replay | Completed tasks skip automatically on re-run |
| Crash recovery | Re-run `dispatch_wave()` with same `wave_id` resumes from checkpoint |

---

## Quick Reference

| Task | Command |
|------|---------|
| Apply Terraform | `terraform apply -var="project_id=claude-mcp-457317"` |
| Create GPU node pool | `gcloud container node-pools create gpu-pool --cluster=CLUSTER --accelerator type=nvidia-l4,count=2 --machine-type=g2-standard-24` |
| Enable image streaming | `gcloud container clusters update CLUSTER --enable-image-streaming` |
| Check GPU allocation | `kubectl describe nodes -l cloud.google.com/gke-accelerator=nvidia-l4` |
| View GPU utilization | `kubectl exec -it POD -- nvidia-smi` |
| Kueue status | `kubectl get clusterqueues -o wide && kubectl get workloads -A` |
| Dispatch wave | `python3 scripts/dispatch.py --manifest manifest.json --bucket gs://gke-dispatch-claude-mcp-457317` |

## Source References

- Terraform: `~/GitHub/ai-on-gke/common-infra/common/`
- Kueue: `~/GitHub/ai-on-gke/batch-reference-architecture/`
- Inference: `~/GitHub/gcp-ai-on-gke/modules/inference-service/`, `best-practices/`
- Dispatch: `${CLAUDE_PLUGIN_ROOT}/skills/dispatch/` (preserved separately)
