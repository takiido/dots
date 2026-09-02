#!/bin/bash
# usage: theme-switch dark|light|toggle

STATE_FILE="$XDG_STATE_HOME/theme-mode"
STATE_FILE="${STATE_FILE:-$HOME/.local/state/theme-mode}"
mkdir -p "$(dirname "$STATE_FILE")"

mode="$1"
if [ "$mode" = "toggle" ]; then
	current=$(cat "$STATE_FILE" 2>/dev/null || echo light)
	[ "$current" = "dark" ] && mode=light || mode=dark
fi

echo "$mode" > "$STATE_FILE"

# somebar
somebar -c "theme $mode"

# gtk (gtk3/4 via gsettings, if using a gsettings-backed environment)
gsettings set org.gnome.desktop.interface color-scheme "prefer-$mode" 2>/dev/null

# qt (if using qt5ct/qt6ct)
if [ "$mode" = "dark" ]; then
	sed -i 's/^style=.*/style=kvantum-dark/' "$HOME/.config/qt5ct/qt5ct.conf" 2>/dev/null
else
	sed -i 's/^style=.*/style=kvantum/' "$HOME/.config/qt5ct/qt5ct.conf" 2>/dev/null
fi

# foot terminal — swap colors config and reload via SIGUSR1 (foot supports live reload)
if [ "$mode" = "dark" ]; then
	cp "$HOME/.config/foot/theme-dark.ini" "$HOME/.config/foot/theme.ini"
else
	cp "$HOME/.config/foot/theme-light.ini" "$HOME/.config/foot/theme.ini"
fi
pkill -SIGUSR1 foot 2>/dev/null
