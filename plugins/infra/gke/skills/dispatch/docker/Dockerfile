FROM node:20-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    bash \
    openssh-client \
    ca-certificates \
    python3 \
    python3-pip \
    jq \
    apt-transport-https \
    gnupg \
    sudo \
  && pip3 install --break-system-packages PyJWT cryptography \
  && curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg \
  && echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" > /etc/apt/sources.list.d/google-cloud-sdk.list \
  && apt-get update && apt-get install -y --no-install-recommends google-cloud-cli \
  && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash --uid 1001 executor \
 && mkdir -p /workspace /scripts \
 && chown -R executor:executor /workspace /scripts

USER executor
WORKDIR /home/executor

RUN curl -fsSL https://claude.ai/install.sh | bash \
 && test -x /home/executor/.local/bin/claude \
 && /home/executor/.local/bin/claude --version

USER root
RUN ln -sf /home/executor/.local/bin/claude /usr/local/bin/claude \
 && test -x /usr/local/bin/claude

USER executor
RUN git config --global user.email "claude-executor@envsn.com" \
 && git config --global user.name "Claude Code (GKE Executor)" \
 && mkdir -p /home/executor/.ssh \
 && ssh-keyscan github.com >> /home/executor/.ssh/known_hosts 2>/dev/null

USER root
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY generate_github_token.py /scripts/generate_github_token.py
RUN chown executor:executor /scripts/generate_github_token.py /entrypoint.sh

USER executor
WORKDIR /workspace

ENTRYPOINT ["/entrypoint.sh"]
