#!/bin/bash

usage() {
    echo "Usage: $0 [-h] [-u VALUE]"
    echo
    echo "Options:"
    echo "  -h            Show this help message"
    echo "  -u VALUE      Update screen brightness to VALUE (percentage, e.g., 75)"
    echo
    echo "If no options are passed, the script will:"
    echo "  - Get current screen brightness"
    echo "  - Update eww variable var_brightness accordingly"
    exit 1
}

brightness=""

# Parse options
while getopts ":hu:" opt; do
  case $opt in
    h)
      usage
      ;;
    u)
      brightness=$OPTARG
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

if [[ -n "$brightness" ]]; then
    brightnessctl set --quiet "${brightness}%"
    eww update var_brightness=$brightness
else
    # Get brightness from brightnessctl
    brightness=$(brightnessctl -m | grep -oP '\d+%' | tr -d '%')
    # Update eww
    eww update var_brightness=$brightness
fi

