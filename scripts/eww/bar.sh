#!/bin/bash

echo 1 

usage() {
    echo "Usage: $0 [-h] [-r]"
    echo
    echo "Options:"
    echo "  -h            Show this help message"
    echo "  -r            Update all variables after eww reload"
    echo
    echo "If no options are passed, the script will:"
    echo "  - Create eww bar widget"
    echo "  - Update eww variables"
    exit 1
}

update_vars() {
    # Pass initial screen brightess value to eww var
    ~/.config/scripts/eww/helpers/brightness.sh
    # Pass initial volume value to eww var
    ~/.config/scripts/eww/helpers/volume.sh
}

reload=false

# Parse options
while getopts ":hr" opt; do
  case $opt in
    h)
      usage
      ;;
    r)
      reload=true
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage
      ;;
  esac
done

shift $((OPTIND -1))

# Open bar widget
if [[ "$reload" != true ]]; then
    eww open bar --screen 1
fi

update_vars
