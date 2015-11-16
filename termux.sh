#!/bin/bash
#apt update
#apt install termux-api jq sqlite imagemagick
geofix_dir="Geofix"
dt=`date +%Y%m%d-%H%M%S`
if [ ! -d "$geofix_dir" ]; then
  mkdir $geofix_dir
  mkdir $geofix_dir"/snapshots"
fi
lat=$(termux-location | jq '.latitude')
lon=$(termux-location | jq '.longitude')
echo "Coordinates: $lat, $lon" | termux-toast
echo "$dt, $lat, $lon" >> $geofix_dir"/geofix.csv"
digikam="geo:$lat,$lon"
osm="http://www.openstreetmap.org/index.html?mlat=$lat&mlon=$lon&zoom=18"
if [ ! -f "$geofix_dir/geofix.sqlite" ]; then
  sqlite3 "$geofix_dir/geofix.sqlite"  "CREATE TABLE geofix (id INTEGER PRIMARY KEY, dt VARCHAR, lat VARCHAR, lon VARCHAR, digikam VARCHAR, osm_url VARCHAR);"
  sqlite3 "$geofix_dir/geofix.sqlite"  "INSERT INTO geofix (dt, lat, lon, digikam, osm_url) VALUES ('$dt', '$lat', '$lon', '$digikam', '$osm');"
else
  sqlite3 "$geofix_dir/geofix.sqlite"  "INSERT INTO geofix (dt, lat, lon, digikam, osm_url) VALUES ('$dt', '$lat', '$lon', '$digikam', '$osm');"
fi
termux-camera-photo --camera 0 $geofix_dir"/snapshots/"$dt.jpg
#convert $geofix_dir"/snapshots/"$dt.jpg -resize 600x $geofix_dir"/snapshots/"$dt.jpg
echo "All done!" | termux-toast
termux-vibrate