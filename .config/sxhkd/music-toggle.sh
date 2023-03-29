#!/bin/bash

status=$(playerctl status)

if [[ $status == "Playing" ]]; then
  playerctl pause
elif [[ $status == "Paused" ]]; then
  playerctl play
fi
