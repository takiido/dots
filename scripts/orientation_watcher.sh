#!/bin/bash

# -------------------------------------------------------------------
# Script Name: orientation_watcher.sh
# Purpose: Automatically rotates the display based on accelerometer orientation.
# Author: takiido
# Date Created: 2025-09-11
# Usage: ./orientation_watcher.sh
# Dependencies: monitor-sensor, hyprctl
# -------------------------------------------------------------------

# This script monitors the accelerometer's orientation and changes the display
# orientation accordingly. It listens for orientation change events and uses
# `hyprctl` to adjust the monitor's display transform.

# Start monitoring the accelerometer for orientation changes
monitor-sensor --accel | while read -r line; do
    # Check if the line contains an accelerometer orientation change message
    if [[ "$line" =~ Accelerometer\ orientation\ changed:\ (.*) ]]; then
        # Extract the orientation change from the matched string using regex
        orientation="${BASH_REMATCH[1]}"
        
        # Extract the last word (orientation direction) from the string
        last_word=$(echo "$orientation" | awk '{print $NF}')
        
        # Output the detected orientation change to the terminal
        echo "Orientation Changed: $last_word"

        # Use a case statement to handle different orientations
        case "$last_word" in
            # If orientation is 'normal', set the display to normal orientation
            "normal")
                hyprctl keyword monitor eDP-1, transform, 0
                ;;
            # If orientation is 'left-up', rotate the display to 90 degrees (left)
            "left-up")
                hyprctl keyword monitor eDP-1, transform, 1
                ;;
            # If orientation is 'right-up', rotate the display to 270 degrees (right)
            "right-up")
                hyprctl keyword monitor eDP-1, transform, 3
                ;;
            # If orientation is 'bottom-up', rotate the display to 180 degrees (inverted)
            "bottom-up")
                hyprctl keyword monitor eDP-1, transform, 2
                ;;
            # Handle unexpected orientation values by printing a message
            *)
                echo "Unknown orientation: $last_word"
                ;;
        esac
    fi
done

