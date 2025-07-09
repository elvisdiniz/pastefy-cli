FROM mcr.microsoft.com/devcontainers/base:alpine-3.21

# Install common tools and utilities
RUN apk update && \
    apk add --no-cache \
    binutils \
    chezmoi \
    starship \
    eza \
    bat \
    curl \
    git \
    vim \
    fastfetch \
    fzf \
    fd \
    ripgrep \
    neovim \
    bottom \
    fish \
    zoxide \
    zsh && \
    apk upgrade --no-cache

# Install Python and pip
RUN apk add --no-cache \
    python3 \
    py3-requests \
    py3-coverage && \
    apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing/ \
    py3-pyinstaller

