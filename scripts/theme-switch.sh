#!/bin/bash
# usage: theme-switch dark|light|toggle

resolve_session_env() {
	local pid
	pid=$(pgrep -u "$(id -un)" -x dwl | head -n1)
	[ -z "$pid" ] && return 1
	[ -r "/proc/$pid/environ" ] || return 1

	local var value
	for var in DBUS_SESSION_BUS_ADDRESS XDG_RUNTIME_DIR WAYLAND_DISPLAY; do
		if [ -z "${!var}" ]; then
			value=$(tr '\0' '\n' <"/proc/$pid/environ" | grep "^${var}=" | cut -d= -f2-)
			[ -n "$value" ] && export "$var=$value"
		fi
	done
}
resolve_session_env
export PATH="/usr/local/bin:$PATH"

STATE_DIR="${XDG_STATE_HOME:-$HOME/.local/state}"
STATE_FILE="$STATE_DIR/theme-mode"
mkdir -p "$STATE_DIR"
mode="$1"
if [ "$mode" = "toggle" ]; then
	current=$(cat "$STATE_FILE" 2>/dev/null || echo light)
	[ "$current" = "dark" ] && mode=light || mode=dark
fi
echo "$mode" >"$STATE_FILE"

somebar -c "theme $mode"
gsettings set org.gnome.desktop.interface color-scheme "prefer-$mode" 2>/dev/null

if [ "$mode" = "dark" ]; then
	sed -i 's/^style=.*/style=kvantum-dark/' "$HOME/.config/qt5ct/qt5ct.conf" 2>/dev/null
else
	sed -i 's/^style=.*/style=kvantum/' "$HOME/.config/qt5ct/qt5ct.conf" 2>/dev/null
fi

if [ "$mode" = "dark" ]; then
	cp "$HOME/.config/foot/theme-dark.ini" "$HOME/.config/foot/theme.ini"
  pkill -USR1 -x foot
else
	cp "$HOME/.config/foot/theme-light.ini" "$HOME/.config/foot/theme.ini"
  pkill -USR2 -x foot
fi
