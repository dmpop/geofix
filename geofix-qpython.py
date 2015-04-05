#-*-coding:utf8;-*-
#qpy:console
#qpy:2
import androidhelper, sys, os, sqlite3
from datetime import datetime
#Specify the destination directory for storing geographical data
geofix_dir = '/sdcard/Geofix/'
wait = 9000
#Create the destination directory if it doesn't exist
if not os.path.exists(geofix_dir):
    os.makedirs(geofix_dir)
#ble location, and obtain location data
droid = androidhelper.Android()
droid.startLocating()
droid.eventWaitFor('location', int(wait))
location = droid.readLocation().result
droid.stopLocating()
#Generate date ad time stamps
date_stamp = datetime.strftime(datetime.now(), '%Y-%m-%d')
time_stamp = datetime.strftime(datetime.now(), '%H:%M:%S')
#Extract latitude and longitude values coordinates from the network source
try:
    coords = location['network']
    lat = coords['latitude']
    lon = coords['longitude']
    droid.makeToast('Network coordinates: ' + str(lat) + ' ' + str(lon))
except (KeyError):
    #If network source is not available extract latitude and longitude values from GPS
    try:
        coords = location['gps']
        lat = coords['latitude']
        lon = coords['longitude']
        droid.makeToast('GPS coordinates: '+ str(lat) + ' ' + str(lon))
    except (KeyError):
        droid.makeToast('Geofix failed to obtain coordinates.')
        sys.exit()
#Generate an OpenStreetMap URL and save the prepared data in the geofix.tsv file
osm ='http://www.openstreetmap.org/index.html?mlat=' + str(lat) + '&mlon=' + str(lon) + '&zoom=18'
f_path = geofix_dir + 'geofix.tsv'
f = open(f_path,'a')
f.write(str(date_stamp) + '\t' + str(time_stamp) + '\t' + str(lat) + '\t' + str(lon) + '\t' + osm + '\n')
f.close()
#Save the prepared data in the geofix.sqlite database
if os.path.exists(geofix_dir + 'geofix.sqlite'):
    #Create the database if it doesn't exist
    sql_query = "INSERT INTO geofix (d_stamp, t_stamp, lat, lon, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (date_stamp, time_stamp, lat, lon, osm)
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute(sql_query)
    conn.commit()
    conn.close()
else:
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute("CREATE TABLE geofix (id INTEGER PRIMARY KEY, d_stamp char(10), t_stamp char(8), lat char(11), lon char(11), osm_url char(256))")
    sql_query = "INSERT INTO geofix (d_stamp, t_stamp, lat, lon, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (date_stamp, time_stamp, lat, lon, osm)
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute(sql_query)
    conn.commit()
    conn.close()

droid.vibrate()

#Uncomment the code below to show the obtained GPS coordinates on the map
# droid.dialogCreateAlert("OpenStreetMap","Show location on the map?")
# droid.dialogSetPositiveButtonText("Yes")
# droid.dialogSetNegativeButtonText("No")
# droid.dialogShow()
# response=droid.dialogGetResponse().result
# droid.dialogDismiss()
# if response.has_key("which"):
#     result=response["which"]
#     if result=="positive":
#         droid.webViewShow(osm)
