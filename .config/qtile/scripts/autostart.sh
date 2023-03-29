#!/bin/sh

# Set screen resolutions and refresh rate
xrandr --output DisplayPort-2 --mode 2560x1440 --rate 143.97 --primary --output DisplayPort-1 --mode 1920x1080 --rate 74.92 --right-of DisplayPort-2

# Set mouse sensitivity
mouse_device_id=$(xinput | grep 'Razer Mamba Elite  ' | grep -oE 'id=[0-9]*' | cut -d "=" -f 2 | head -n 1)
xinput --set-prop "$mouse_device_id" 'libinput Accel Speed' -0.8

#start sxhkd to replace Qtile native key-bindings

picom -b --config "$HOME/.config/picom.conf" &
dunst -conf "$HOME/.config/dunst/dunstrc" & 
pulseaudio --daemonize=no --exit-idle-time=-1 &
sxhkd -c "$HOME/.config/sxhkd/sxhkdrc" &
exec "$HOME/.config/qtile/scripts/disable-blackscreen.sh" &
xfce4-clipman &

# Default apps to start
kdeconnect-app &
nextcloud &
alacritty &
firefox &
discord &
thunderbird &

# Wait before starting
sleep 1
exec "$HOME/.config/polybar/launch.sh" & # Ensure that pulseaudio daemon is running
exec "eww daemon" &
