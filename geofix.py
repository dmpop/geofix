import android, sys, os, sqlite3
from datetime import datetime

geofix_dir = '/sdcard/Geofix/'
wait = 9000

if not os.path.exists(geofix_dir):
    os.makedirs(geofix_dir)

droid = android.Android()
droid.startLocating()
droid.eventWaitFor('location', int(wait))
location = droid.readLocation().result
droid.stopLocating()

date_stamp = datetime.strftime(datetime.now(), '%Y-%m-%d')
time_stamp = datetime.strftime(datetime.now(), '%H:%M:%S')

try:
    coords = location['network']
    lat = coords['latitude']
    lon = coords['longitude']
    droid.notify('Network coordinates', str(lat) + ' ' + str(lon))
except (KeyError):
    try:
        coords = location['gps']
        lat = coords['latitude']
        lon = coords['longitude']
        droid.notify('GPS coordinates', str(lat) + ' ' + str(lon))
    except (KeyError):
        droid.notify('Geofix', 'Failed to obtain coordinates. :-(')
    
OSM='http://www.openstreetmap.org/index.html?mlat=' + str(lat) + '&mlon=' + str(lon) + '&zoom=18'
f_path = geofix_dir + 'geofix.tsv'
f = open(f_path,'a')
f.write(str(date_stamp) + '\t' + str(time_stamp) + '\t' + str(lat) + '\t' + str(lon) + '\t' + OSM + '\n')
f.close()
#Save the obtained data in the geofix.sqlite database
if os.path.exists(geofix_dir + 'geofix.sqlite'):
    sql_query = "INSERT INTO geofix (d_stamp, t_stamp, lat, lon, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (date_stamp, time_stamp, lat, lon, OSM)
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute(sql_query)
    conn.commit()
    conn.close()
else:
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute("CREATE TABLE geofix (id INTEGER PRIMARY KEY, d_stamp char(10), t_stamp char(8), lat char(11), lon char(11), osm_url char(256))")
    sql_query = "INSERT INTO geofix (d_stamp, t_stamp, lat, lon, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (date_stamp, time_stamp, lat, lon, OSM)
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute(sql_query)
    conn.commit()
    conn.close()
#Uncomment the code below to show the obtained GPS coordinates on OpenStreetMap
# droid.dialogCreateAlert("OpenStreetMap","Show location on the map?")
# droid.dialogSetPositiveButtonText("Yes")
# droid.dialogSetNegativeButtonText("No")
# droid.dialogShow()
# response=droid.dialogGetResponse().result
# droid.dialogDismiss()
# if response.has_key("which"):
#     result=response["which"]
#     if result=="positive":
#         droid.startActivity('android.intent.action.VIEW', OSM)
