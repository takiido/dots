#!/bin/sh

WP=leaves.jpg

apply_theme() {
	mode="$1"
	"$HOME/.local/bin/theme-switch" "$mode"
	(
		for i in $(seq 1 50); do
			[ -p "$XDG_RUNTIME_DIR/somebar-0" ] && break
			sleep 0.1
		done
		somebar -c "theme $mode"
	) &
}

pipewire &
pipewire-pulse &
wireplumber &

WLR_DIR=/home/takiido/repos/wlr-randr/build/wlr-randr

wbg -s /home/takiido/wp/$WP &

if $WLR_DIR | grep -q "ED270R"; then
	$WLR_DIR --output HDMI-A-1 --mode 1920x1080@143.992996
fi

hour=$(date +%H)
if [ "$((10#$hour))" -ge 6 ] && [ "$((10#$hour))" -lt 18 ]; then
	apply_theme light
else
	apply_theme dark
fi

pkill -x someblocks
pkill -x somebar

while true; do
  pkill -x someblocks
  rm -f "$XDG_RUNTIME_DIR"/somebar-*
	someblocks >/tmp/someblocks.log 2>&1 &
	somebar >/tmp/somebar.log 2>&1
done
