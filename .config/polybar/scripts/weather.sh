#!/bin/bash

api_key=<your-openweather-api-key>
city_id=<your-openweather-town-code>
cache_file="$HOME/.config/polybar/cache/weather.json"

fetch_weather (){
  url="api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${api_key}&cnt=5&units=metric&lang=en"
  curl ${url} -s -o ${cache_file}
}

echo_temp (){
  echo "$(grep -oP '"temp"[]:\-?[0-9]*\.[0-9]*' ${cache_file} | cut -d: -f2)°C"
}

echo_location () {
  echo "$(grep -o '"name":"[a-zA-Z]*"' ${cache_file} | cut -d: -f2 | sed 's/"//g'): "
}

echo_joined () {
  echo "$(echo_location)$(echo_temp)"
}

# update_cache_file (){
#   unix_modified=$(($(stat -c %Y ${cache_file})))
#   unix_current=$(($(date +%s)))
#   if [[ $((unix_current - unix_modified)) -gt "3600" ]]; then
#     fetch_weather
#   fi
# }

for i in "$@"; do
  case $i in
    -f) fetch_weather ;;
    -t) echo_temp ;;
    -l) echo_location ;;
    -e) echo_joined ;;
    # -u) update_cache_file ;;
    *) 
    ;;
  esac
done
