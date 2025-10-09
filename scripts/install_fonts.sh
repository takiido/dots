#!/bin/bash
set -e

FONTS_DIR="$HOME/.local/share/fonts/otf"
SOURCE_DIR="$HOME/dots/fonts/CommitMono"

mkdir -p "$FONTS_DIR"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Source directory $SOURCE_DIR does not exist. Exiting."
  exit 1
fi

cp -r "$SOURCE_DIR" "$FONTS_DIR/"

fc-cache -f -v

