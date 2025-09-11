#!/usr/bin/env zsh

GREEN="\033[32m"
NC="\033[0m"

set -euo pipefail

URL="https://github.com/neovim/neovim/releases/download/nightly/nvim-linux-x86_64.tar.gz"
TMP_DIR="/tmp/nvim-nightly"
INSTALL_DIR="/opt/nvim-nightly"
BIN="/usr/local/bin/nvim"

mkdir -p "$TMP_DIR"
cd "$TMP_DIR"

echo "$GREEN> Downloading Nvim Nightly build...$NC"
curl -L --progress-bar -o nvim-nightly.tar.gz "$URL"

echo "$GREEN> Extracting...$NC"
tar -xzf nvim-nightly.tar.gz

echo "$GREEN> Removing old installation...$NC"
sudo rm -rf "$INSTALL_DIR"

sudo mv nvim-linux-x86_64 "$INSTALL_DIR"

echo "$GREEN> Updating symlink...$NC"
sudo ln -sf "$INSTALL_DIR/bin/nvim" "$BIN"

cd /
rm -rf "$TMP_DIR"

echo "$GREEN> Neovim Nightly updated$NC"
