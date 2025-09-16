#!/bin/bash

usage() {
    echo "Usage: $0 [-h] [-u VALUE]"
    echo
    echo "Options:"
    echo "  -h            Show this help message"
    echo "  -u VALUE      Update volume to VALUE (percentage, e.g., 75)"
    echo
    echo "If no options are passed, the script will:"
    echo "  - Get current volume"
    echo "  - Update eww variable var_volume accordingly"
    exit 1
}

volume=""

# Parse options
while getopts ":hu:" opt; do
  case $opt in
    h)
      usage
      ;;
    u)
      volume=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      usage
      ;;
  esac
done

shift $((OPTIND -1))

if [[ -n "$volume" ]]; then
    # Set default sink volume with pactl
    pactl set-sink-volume @DEFAULT_SINK@ $volume%
    # Update eww
    eww update var_volume=$volume
else
    # Get default sink volume from pactl
    brightness=$(brightnessctl -m | grep -oP '\d+%' | tr -d '%')
    # Update eww
    eww update var_volume=$volume
fi
