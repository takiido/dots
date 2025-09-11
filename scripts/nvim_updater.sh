#!/usr/bin/env zsh

# -------------------------------------------------------------------
# Script Name: nvim_updater.sh
# Purpose: Download and install the latest Neovim Nightly build.
# Author: takiido
# Date Created: 2025-09-11
# Usage: ./nvim_updater.sh
# Dependencies: curl, tar, sudo
# -------------------------------------------------------------------

# Define color codes for output formatting (Green for success)
GREEN="\033[32m"
NC="\033[0m"  # No Color (reset formatting)

# Set strict error handling
set -euo pipefail

# URL for the latest Neovim Nightly release tarball
URL="https://github.com/neovim/neovim/releases/download/nightly/nvim-linux-x86_64.tar.gz"

# Temporary directory to download and extract the tarball
TMP_DIR="/tmp/nvim-nightly"

# Installation directory for Neovim Nightly
INSTALL_DIR="/opt/nvim-nightly"

# Path to the Neovim binary symlink
BIN="/usr/local/bin/nvim"

# Step 1: Create temporary directory for downloading
mkdir -p "$TMP_DIR"

# Change working directory to the temporary directory
cd "$TMP_DIR"

# Step 2: Download the latest Neovim Nightly tarball
echo "$GREEN> Downloading Nvim Nightly build...$NC"
curl -L --progress-bar -o nvim-nightly.tar.gz "$URL"

# Step 3: Extract the downloaded tarball
echo "$GREEN> Extracting...$NC"
tar -xzf nvim-nightly.tar.gz

# Step 4: Remove the old Neovim installation (if any)
echo "$GREEN> Removing old installation...$NC"
sudo rm -rf "$INSTALL_DIR"

# Step 5: Move the newly extracted Neovim build to the installation directory
sudo mv nvim-linux-x86_64 "$INSTALL_DIR"

# Step 6: Update the symlink to point to the new Neovim binary
echo "$GREEN> Updating symlink...$NC"
sudo ln -sf "$INSTALL_DIR/bin/nvim" "$BIN"

# Step 7: Clean up by removing the temporary directory
cd /
rm -rf "$TMP_DIR"

# Step 8: Confirm successful update
echo "$GREEN> Neovim Nightly updated$NC"

