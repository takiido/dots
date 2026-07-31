#!/bin/sh

pipewire &
pipewire-pulse &
wireplumber &

WLR_DIR=/home/takiido/repos/wlr-randr/build/wlr-randr

wbg -s /home/takiido/wp/dd.jpg &

if WLR_DIR | grep -q "ED270R"; then
  WLR_DIR --output HDMI-A-1 --mode 1920x1080@143.992996
fi


someblocks &
exec somebar
