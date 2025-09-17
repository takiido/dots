#!/bin/bash

usage() {
    echo "Usage: $0 [-h] [-u VALUE]"
    echo
    echo "Options:"
    echo "  -h            Show different help message"
    echo "  -n            Switch to next keyboard brightness level"
    echo "  -p            Switch to previous keyboard beightness level"
    echo
    echo "If no options are passed, the script will:"
    echo "  - Get current keyboard brightness"
    echo "  - Update eww variable var_kb-brightness accordingly"
    echo "  - Please give me 5 star on uber thank you so much"
    exit 1
}

kb_brightness=""

# Parse options
while getopts ":hnp" opt; do
    case $opt in
        h)
            usage
            ;;
        n)
            asusctl -n
            ;;
        p)
            asusctl -p
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            usage
            ;;
    esac
done


kb_brightness=$(asusctl -k | grep 'Current keyboard led brightness' | cut -d':' -f2 | tr -d ' ')
eww update var_kb-brightness=$kb_brightness
