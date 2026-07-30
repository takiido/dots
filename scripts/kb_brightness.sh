#!/bin/sh
MAX_VALUE=3
MIN_VALUE=0
CURRENT_VALUE=0

get_value() {
  CURRENT_VALUE=$(brightnessctl -d "asus::kbd_backlight" get)
}

get_value
echo "$CURRENT_VALUE"

if [ "$CURRENT_VALUE" -lt "$MAX_VALUE" ]; then
  brightnessctl -d "asus::kbd_backlight" set +1
  CURRENT_VALUE=$(brightnessctl -d "asus::kbd_backlight" get)
else
  CURRENT_VALUE=$(brightnessctl -d "asus::kbd_backlight" set 0)
fi
