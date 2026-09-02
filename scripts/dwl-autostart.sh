#!/bin/sh

WP=leaves.jpg

pipewire &
pipewire-pulse &
wireplumber &

WLR_DIR=/home/takiido/repos/wlr-randr/build/wlr-randr

wbg -s /home/takiido/wp/$WP &

if $WLR_DIR | grep -q "ED270R"; then
	$WLR_DIR --output HDMI-A-1 --mode 1920x1080@143.992996
fi

pkill -x someblocks
pkill -x somebar

while true; do
  pkill -x someblocks
  rm -f "$XDG_RUNTIME_DIR"/somebar-*
	someblocks >/tmp/someblocks.log 2>&1 &
	somebar >/tmp/somebar.log 2>&1
done
