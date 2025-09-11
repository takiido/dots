#!/bin/bash

CONFIG_FILE="$HOME/.config/.current_mode"
MODES=("normal" "touch" "dock")

if [[ -f "$CONFIG_FILE" ]]; then
    current_mode=$(cat "$CONFIG_FILE")
else
    current_mode="normal"
fi

for i in "${!MODES[@]}"; do
    if [[ "${MODES[$i]}" == "$current_mode" ]]; then
        current_index=$i
        break
    fi
done

next_index=$(( (current_index + 1) % ${#MODES[@]} ))
next_mode="${MODES[$next_index]}"

echo "$next_mode" > "$CONFIG_FILE"

echo "Switched mode: $next_mode"

