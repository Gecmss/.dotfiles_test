#!/bin/sh

# Key mapping
setxkbmap latam -option caps:swapescape & # Key map with caps and scape alternate


# Resolution
# xrandr --output DVI-D-1 --off --output HDMI-1 --primary --mode 1600x900 --pos 0x0 --rotate normal --output VGA-1 --off

#System Icons

#Usb
udiskie -t &

#Network manager
nm-applet &

#Volume
volumeicon &

#Wallpaper
nitrogen --restore &

#Picom
picom --vsync --backend glx --xrender-sync-fence &

# Conky
conky --pause=6 &
