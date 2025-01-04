FROM debian:bookworm-slim AS builder

ENV CARGO_HOME="/opt/.cargo"
ENV RUSTUP_HOME="/opt/.rustup"
ENV UV_INSTALL_DIR="/opt/.cargo/bin"

SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]

WORKDIR /opt

# 必要なツールのインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates curl

# uvとrustupのインストール
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y


FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm

ENV CARGO_HOME="/opt/.cargo"
ENV RUSTUP_HOME="/opt/.rustup"
ENV PATH="/opt/.cargo/bin:/home/vscode/.cargo/bin:$PATH"
ENV PYTHONUNBUFFERED=True
ENV UV_LINK_MODE=copy

WORKDIR /opt

# builderステージから必要なディレクトリをコピー
COPY --from=builder --chown=vscode: $CARGO_HOME $CARGO_HOME
COPY --from=builder $RUSTUP_HOME $RUSTUP_HOME

# Node.jsとnpmのインストール
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g git-cz
