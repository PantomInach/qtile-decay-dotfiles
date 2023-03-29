#!/bin/bash

config=~/.config/polybar/config.ini

pkill polybar

for monitor in $(polybar --list-monitors | sed 's/ //g'); do
  res="1k"
  if [[ $monitor == *"2560x1440"* ]]; then
    res=""
  fi
  m=$(echo $monitor | cut -d":" -f1)

  MONITOR=$m polybar --reload --config=$config workspace$res 2>&1 | tee -a /tmp/polybar.log & disown
  MONITOR=$m polybar --reload --config=$config datecenter$res 2>&1 | tee -a /tmp/polybar.log & disown
  MONITOR=$m polybar --reload --config=$config trays$res 2>&1 | tee -a /tmp/polybar.log & disown

done
