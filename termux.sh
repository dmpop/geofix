#!/bin/bash
#apt update
#apt install termux-api jq sqlite
#termux-location | jq '.latitude' | termux-toast
lat=$(termux-location | jq '.latitude')
lon=$(termux-location | jq '.longitude')
echo $lat, $lon | termux-toast