import android, time, sys
import os, sqlite3
from datetime import datetime
droid = android.Android()
droid.startLocating()
time.sleep(9)

date_stamp = datetime.strftime(datetime.now(), '%Y-%m-%d')
time_stamp = datetime.strftime(datetime.now(), '%H:%M:%S')
location = droid.readLocation().result

try:
    net = location['network']
    net_lat = net['latitude']
    net_lon = net['longitude']
    OSM='http://www.openstreetmap.org/index.html?mlat=' + str(net_lat) + '&mlon=' + str(net_lon) + '&zoom=18'
    f_path = '/sdcard/geofix_net.tsv'
    f = open(f_path,'a')
    f.write(str(date_stamp) + '\t' + str(time_stamp) + '\t' + str(net_lat) + '\t' + str(net_lon) + '\t' + OSM + '\n')
    f.close()
    droid.notify('Network coordinates', str(net_lat) + ' ' + str(net_lon))
except (KeyError):
    droid.makeToast('Failed. Please try again.')

try:
    gps = location['gps']
    gps_lat = gps['latitude']
    gps_lon = gps['longitude']
    OSM='http://www.openstreetmap.org/index.html?mlat=' + str(gps_lat) + '&mlon=' + str(gps_lon) + '&zoom=18'
    f_path = '/sdcard/geofix_gps.tsv'
    f = open(f_path,'a')
    f.write(str(date_stamp) + '\t' + str(time_stamp) + '\t' + str(gps_lat) + '\t' + str(gps_lon) + '\t' + OSM + '\n')
    f.close()
    droid.notify('GPS coordinates', str(gps_lat) + ' ' + str(gps_lon))
    #Save the obtained data in the geofix.sqlite database
    if os.path.exists('geofix.sqlite'):
        sql_query = "INSERT INTO geofix (d_stamp, t_stamp, gps_lat, gps_lon, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (date_stamp, time_stamp, gps_lat, gps_lon, OSM)
        conn = sqlite3.connect('geofix.sqlite')
        conn.execute(sql_query)
        conn.commit()
        conn.close()
    else:
        conn = sqlite3.connect('geofix.sqlite')
        conn.execute("CREATE TABLE geofix (id INTEGER PRIMARY KEY, d_stamp char(10), t_stamp char(8), gps_lat char(11), gps_lon char(11), osm_url char(256))")
        sql_query = "INSERT INTO geofix (d_stamp, t_stamp, gps_lat, gps_lon, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (date_stamp, time_stamp, gps_lat, gps_lon, OSM)
        conn = sqlite3.connect('geofix.sqlite')
        conn.execute(sql_query)
        conn.commit()
        conn.close()
    #Uncomment to show the obtained GPS coordinates on OpenStreetMap
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
except (KeyError):
    droid.makeToast('Failed. Please try again.')
    sys.exit()
