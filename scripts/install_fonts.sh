#!/bin/bash
set -e

SRC_DIR="$HOME/dots/fonts"
DEST_DIR="$HOME/.local/share/fonts"

mkdir -p "$DEST_DIR"

find "$SRC_DIR" -type f \( -iname "*.ttf" -o -iname "*.otf" \) | while read -r font_file; do
  echo "Installing: $(basename "$font_file")"
  cp "$font_file" "$DEST_DIR/"
done

fc-cache -f -v
