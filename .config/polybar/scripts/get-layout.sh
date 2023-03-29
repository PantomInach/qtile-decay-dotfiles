#!/bin/bash

# Gets the layout of the current screen in qtile
if [[ $1 != "" ]]; then
  while [[ true ]]; do
    screen=$(qtile cmd-obj -o cmd screen -f info | grep -o "'index': [0-9]" | grep -o '[0-9]')
    screen=$((${screen} + 1))
    groups=$(qtile cmd-obj -o cmd -f screens | grep "'group': '[0-9]*'" | grep -o '[0-9]*' | cut -f1)
    group=$(echo ${groups} | cut -d ' ' -f${screen})
    layout=$(qtile cmd-obj -o group ${group} -f info | grep -o "'layout': '[a-zA-Z]*'" | cut -d: -f2 | sed "s/'//g")
    echo $layout
    sleep $1
  done
fi
