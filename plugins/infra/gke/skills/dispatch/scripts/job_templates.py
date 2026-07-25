#!/usr/bin/env python3
"""K8s Job YAML builders for gke-dispatch.

Separates YAML structure from dispatch logic. Two builders:
- executor jobs: one Job per task, with Secret Manager mounts
- indexed jobs: single Indexed Job for generic container tasks
"""

import json

from gcs_utils import RESOURCE_PROFILES


def _job_name(wave_id: str, suffix: str = "") -> str:
    name = f"gke-dispatch-{wave_id}"
    if suffix:
        name = f"{name}-{suffix}"
    return name.replace("_", "-").lower()[:63]


def _resources(profile: str) -> dict:
    return RESOURCE_PROFILES.get(profile, RESOURCE_PROFILES["standard"])


def _pending(manifest: dict) -> list[dict]:
    return [t for t in manifest["tasks"] if t["status"] == "pending"]


def build_executor_job(task: dict, wave_id: str, namespace: str,
                       sa: str, bucket: str, retries: int, timeout: int) -> str:
    """Single executor Job YAML for one LLM task."""
    profile = task.get("resource_profile", "standard")
    resources = _resources(profile)
    t_name = _job_name(wave_id, task["id"])
    inputs = task.get("inputs", {})
    is_gpu = "gpu" in resources
    gpu_request = '\n            nvidia.com/gpu: "1"' if is_gpu else ""
    gpu_limit = '\n            nvidia.com/gpu: "1"' if is_gpu else ""
    accelerator = resources.get("accelerator")
    deps = task.get("depends_on") or []
    if deps:
        # Poll each dep's result.json on GCS. Exit 0 only when ALL deps have exit_code 0.
        # Extract each dep's repo_branch from result.json and persist to /shared/dep-branches.txt
        # for the main container's git-merge step (entrypoint reads DEP_BRANCHES_FILE).
        dep_ids_str = " ".join(deps)
        wait_deps_init = (
            "      - name: wait-deps\n"
            "        image: google/cloud-sdk:slim\n"
            "        command: [\"sh\", \"-c\"]\n"
            "        args:\n"
            "        - |\n"
            "          set -e\n"
            f"          DEPS=\"{dep_ids_str}\"\n"
            "          : > /shared/dep-branches.txt\n"
            "          for dep_id in $DEPS; do\n"
            f"            DEP_RESULT=\"{bucket}/waves/{wave_id}/outputs/$dep_id/result.json\"\n"
            "            echo \"Waiting for dependency: $DEP_RESULT\"\n"
            "            while ! gsutil ls \"$DEP_RESULT\" > /dev/null 2>&1; do sleep 15; done\n"
            "            RJSON=$(gsutil cat \"$DEP_RESULT\")\n"
            "            EC=$(echo \"$RJSON\" | grep -o '\"exit_code\": *[0-9]*' | grep -o '[0-9]*$')\n"
            "            if [ \"$EC\" != \"0\" ]; then\n"
            "              echo \"FATAL: dependency $dep_id failed (exit_code=$EC)\" >&2\n"
            "              exit 1\n"
            "            fi\n"
            f"            BRANCH=\"gke-dispatch/{wave_id}/$dep_id\"\n"
            "            echo \"$BRANCH\" >> /shared/dep-branches.txt\n"
            "            echo \"Dependency satisfied: $dep_id (branch=$BRANCH)\"\n"
            "          done\n"
            "          echo \"Dep branches written to /shared/dep-branches.txt:\"\n"
            "          cat /shared/dep-branches.txt\n"
            "        volumeMounts:\n"
            "        - name: shared\n"
            "          mountPath: /shared\n"
        )
    else:
        wait_deps_init = ""
    if accelerator:
        accelerator_required = (
            "      affinity:\n"
            "        nodeAffinity:\n"
            "          requiredDuringSchedulingIgnoredDuringExecution:\n"
            "            nodeSelectorTerms:\n"
            "            - matchExpressions:\n"
            "              - key: cloud.google.com/gke-accelerator\n"
            "                operator: In\n"
            f"                values: [\"{accelerator}\"]\n"
        )
    else:
        accelerator_required = (
            "      affinity:\n"
            "        nodeAffinity:\n"
            "          preferredDuringSchedulingIgnoredDuringExecution:\n"
            "          - weight: 100\n"
            "            preference:\n"
            "              matchExpressions:\n"
            "              - key: gpu-type\n"
            "                operator: In\n"
            "                values:\n"
            "                - nvidia-l4-dual\n"
            "          - weight: 50\n"
            "            preference:\n"
            "              matchExpressions:\n"
            "              - key: gpu-type\n"
            "                operator: In\n"
            "                values:\n"
            "                - nvidia-l4\n"
        )

    return f"""apiVersion: batch/v1
kind: Job
metadata:
  name: {t_name}
  namespace: {namespace}
  labels:
    app: gke-dispatch
    wave-id: "{wave_id}"
    task-id: "{task['id']}"
spec:
  backoffLimit: {retries}
  activeDeadlineSeconds: {timeout + 60}
  ttlSecondsAfterFinished: 3600
  template:
    metadata:
      labels:
        app: gke-dispatch
        wave-id: "{wave_id}"
        task-id: "{task['id']}"
    spec:
      serviceAccountName: {sa}
      restartPolicy: OnFailure
      nodeSelector:
        cloud.google.com/gke-spot: "true"
      tolerations:
      - key: cloud.google.com/gke-spot
        operator: Equal
        value: "true"
        effect: NoSchedule
      - key: nvidia.com/gpu
        operator: Exists
        effect: NoSchedule
{accelerator_required.rstrip()}
      volumes:
      - name: secrets
        emptyDir: {{}}
      - name: shared
        emptyDir: {{}}
      initContainers:
{wait_deps_init.rstrip()}
      - name: fetch-secrets
        image: google/cloud-sdk:slim
        command: ["sh", "-c"]
        args:
        - |
          gcloud secrets versions access latest --secret=gsd-claude-oauth-token --project=claude-mcp-457317 > /var/secrets/claude-oauth-token
          gcloud secrets versions access latest --secret=gsd-github-app-private-key --project=claude-mcp-457317 > /var/secrets/github-app-key
        volumeMounts:
        - name: secrets
          mountPath: /var/secrets
      containers:
      - name: executor
        image: {task['image']}
        env:
        - name: WAVE_ID
          value: "{wave_id}"
        - name: TASK_ID
          value: "{task['id']}"
        - name: GCS_BUCKET
          value: "{bucket}"
        - name: REPO_URL
          value: "{inputs.get('repo_url', '')}"
        - name: REPO_BRANCH
          value: "{inputs.get('repo_branch', 'main')}"
        - name: GIT_SHA
          value: "{inputs.get('git_sha', '')}"
        - name: PLAN_PATH
          value: "{inputs.get('plan_path', '')}"
        - name: TASK_CMD
          value: "{task['cmd']}"
        - name: MAX_TURNS
          value: "{inputs.get('max_turns', '25')}"
        - name: GITHUB_APP_ID
          value: "3604031"
        - name: GITHUB_APP_KEY_FILE
          value: "/var/secrets/github-app-key"
        - name: DEP_BRANCHES_FILE
          value: "/shared/dep-branches.txt"
        resources:
          requests:
            cpu: "{resources['cpu']}"
            memory: "{resources['memory']}"{gpu_request}
          limits:
            cpu: "{resources['cpu_limit']}"
            memory: "{resources['memory_limit']}"{gpu_limit}
        volumeMounts:
        - name: secrets
          mountPath: /var/secrets
          readOnly: true
        - name: shared
          mountPath: /shared
"""


def build_executor_jobs_yaml(manifest: dict) -> str:
    """Generate per-task Job YAMLs for executor images."""
    tasks = _pending(manifest)
    if not tasks:
        return ""

    wave_id = manifest["wave_id"]
    namespace = manifest["config"].get("namespace", "gke-dispatch")
    sa = manifest["config"].get("service_account", "gke-dispatch-worker")
    bucket = manifest["config"]["bucket"].rstrip("/")
    timeout = max(t.get("timeout_seconds", 600) for t in tasks)
    retries = max(t.get("retries", 2) for t in tasks)

    jobs = [
        build_executor_job(t, wave_id, namespace, sa, bucket, retries, timeout)
        for t in tasks
    ]
    return "---\n".join(jobs)


def build_indexed_job_yaml(manifest: dict) -> str:
    """Generate a single K8s Indexed Job YAML for generic container tasks."""
    tasks = _pending(manifest)
    if not tasks:
        return ""

    wave_id = manifest["wave_id"]
    namespace = manifest["config"].get("namespace", "gke-dispatch")
    sa = manifest["config"].get("service_account", "gke-dispatch-worker")
    bucket = manifest["config"]["bucket"].rstrip("/")
    parallelism = manifest["config"].get("parallelism_cap") or len(tasks)
    completions = len(tasks)

    profile = tasks[0].get("resource_profile", "standard")
    resources = _resources(profile)
    timeout = max(t.get("timeout_seconds", 600) for t in tasks)
    retries = max(t.get("retries", 2) for t in tasks)

    task_id_map = json.dumps({i: t["id"] for i, t in enumerate(tasks)})
    cmd_map = json.dumps({i: t["cmd"] for i, t in enumerate(tasks)})
    image = tasks[0]["image"]
    job_name = _job_name(wave_id)

    gpu_section = ""
    if profile == "gpu":
        gpu_section = '            nvidia.com/gpu: "1"'

    return f"""apiVersion: batch/v1
kind: Job
metadata:
  name: {job_name}
  namespace: {namespace}
  labels:
    app: gke-dispatch
    wave-id: "{wave_id}"
spec:
  completions: {completions}
  parallelism: {parallelism}
  completionMode: Indexed
  backoffLimit: {retries}
  activeDeadlineSeconds: {timeout + 60}
  ttlSecondsAfterFinished: 3600
  template:
    metadata:
      labels:
        app: gke-dispatch
        wave-id: "{wave_id}"
    spec:
      serviceAccountName: {sa}
      restartPolicy: OnFailure
      volumes:
      - name: shared
        emptyDir: {{}}
      initContainers:
      - name: idempotent-check
        image: google/cloud-sdk:slim
        command: ["sh", "-c"]
        args:
        - |
          TASK_ID=$(echo '{task_id_map}' | python3 -c "import sys,json; print(json.load(sys.stdin)[str($JOB_COMPLETION_INDEX)])")
          RESULT_PATH="{bucket}/waves/{wave_id}/outputs/$TASK_ID/result.json"
          if gsutil ls "$RESULT_PATH" 2>/dev/null; then
            echo "SKIP" > /shared/action
            echo "Task $TASK_ID already completed, skipping"
          else
            echo "RUN" > /shared/action
          fi
        env:
        - name: JOB_COMPLETION_INDEX
          valueFrom:
            fieldRef:
              fieldPath: metadata.annotations['batch.kubernetes.io/job-completion-index']
        volumeMounts:
        - name: shared
          mountPath: /shared
      containers:
      - name: task
        image: {image}
        command: ["sh", "-c"]
        args:
        - |
          ACTION=$(cat /shared/action)
          if [ "$ACTION" = "SKIP" ]; then
            echo "Idempotent skip"
            exit 0
          fi
          TASK_ID=$(echo '{task_id_map}' | python3 -c "import sys,json; print(json.load(sys.stdin)[str($JOB_COMPLETION_INDEX)])")
          TASK_CMD=$(echo '{cmd_map}' | python3 -c "import sys,json; print(json.load(sys.stdin)[str($JOB_COMPLETION_INDEX)])")
          mkdir -p /outputs
          echo "Running task $TASK_ID: $TASK_CMD"
          START=$(date +%s)
          eval "$TASK_CMD" > /shared/stdout.log 2> /shared/stderr.log
          EXIT_CODE=$?
          END=$(date +%s)
          DURATION=$((END - START))
          cat > /shared/result.json <<RESULT
          {{
            "exit_code": $EXIT_CODE,
            "task_id": "$TASK_ID",
            "duration_seconds": $DURATION,
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
          }}
          RESULT
          exit $EXIT_CODE
        env:
        - name: JOB_COMPLETION_INDEX
          valueFrom:
            fieldRef:
              fieldPath: metadata.annotations['batch.kubernetes.io/job-completion-index']
        - name: WAVE_ID
          value: "{wave_id}"
        - name: GCS_BUCKET
          value: "{bucket}"
        resources:
          requests:
            cpu: "{resources['cpu']}"
            memory: "{resources['memory']}"
          limits:
            cpu: "{resources['cpu_limit']}"
            memory: "{resources['memory_limit']}"
{gpu_section}
        volumeMounts:
        - name: shared
          mountPath: /shared
      - name: log-shipper
        image: google/cloud-sdk:slim
        command: ["sh", "-c"]
        args:
        - |
          TASK_ID=$(echo '{task_id_map}' | python3 -c "import sys,json; print(json.load(sys.stdin)[str($JOB_COMPLETION_INDEX)])")
          OUTPUT_BASE="{bucket}/waves/{wave_id}/outputs/$TASK_ID"
          while [ ! -f /shared/result.json ] && [ ! -f /shared/action ] ; do sleep 2; done
          if [ -f /shared/action ] && grep -q SKIP /shared/action; then exit 0; fi
          while [ ! -f /shared/result.json ]; do sleep 2; done
          sleep 1
          gsutil cp /shared/stdout.log "$OUTPUT_BASE/stdout.log" 2>/dev/null || true
          gsutil cp /shared/stderr.log "$OUTPUT_BASE/stderr.log" 2>/dev/null || true
          gsutil cp /shared/result.json "$OUTPUT_BASE/result.tmp.json"
          gsutil mv "$OUTPUT_BASE/result.tmp.json" "$OUTPUT_BASE/result.json"
          if [ -d /outputs ] && [ "$(ls -A /outputs 2>/dev/null)" ]; then
            gsutil -m cp -r /outputs/* "$OUTPUT_BASE/artifacts/" 2>/dev/null || true
          fi
        env:
        - name: JOB_COMPLETION_INDEX
          valueFrom:
            fieldRef:
              fieldPath: metadata.annotations['batch.kubernetes.io/job-completion-index']
        volumeMounts:
        - name: shared
          mountPath: /shared
"""


def build_job_yaml(manifest: dict) -> str:
    """Route to executor or indexed job builder based on image name."""
    tasks = _pending(manifest)
    if not tasks:
        return ""
    if "claude-executor" in tasks[0].get("image", ""):
        return build_executor_jobs_yaml(manifest)
    return build_indexed_job_yaml(manifest)
