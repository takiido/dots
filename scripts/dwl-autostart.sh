#!/bin/sh

pipewire &
pipewire-pulse &
wireplumber &

wbg -s /home/takiido/wp/dd.jpg &

if wlr-randr | grep -q "ED270R"; then
  wlr-randr --output HDMI-A-1 --mode 1920x1080@143.992996
fi


someblocks &
exec somebar
