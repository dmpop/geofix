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
#Enable location, and obtain location data
droid = androidhelper.Android()
droid.startLocating()
droid.eventWaitFor('location', int(wait))
location = droid.readLocation().result
droid.stopLocating()
#Generate date and time string
dt = datetime.strftime(datetime.now(), '%Y%m%d-%H%M%S')
#Extract latitude and longitude coordinates from the network source
try:
    coords = location['network']
    lat = str(coords['latitude'])
    lon = str(coords['longitude'])
    droid.makeToast('Network coordinates: ' + lat + ' ' + lon)
except (KeyError):
    #If network source is not available, extract latitude and longitude values from GPS
    try:
        coords = location['gps']
        lat = str(coords['latitude'])
        lon = str(coords['longitude'])
        droid.makeToast('GPS coordinates: '+ lat + ' ' + lon)
    except (KeyError):
        droid.makeToast('Geofix failed to obtain coordinates.')
        sys.exit()
#Generate coordinates in the digiKam format
digikam = 'geo:' + lat + ',' + lon
#Take an accompanying photo
droid.dialogCreateAlert("Geofix","Take an accompanying photo?")
droid.dialogSetPositiveButtonText("Yes")
droid.dialogSetNegativeButtonText("No")
droid.dialogShow()
response=droid.dialogGetResponse().result
droid.dialogDismiss()
if response["which"] == "positive":
    droid.cameraInteractiveCapturePicture(geofix_dir + dt + '.jpg')
#Generate an OpenStreetMap URL and save the prepared data in the geofix.tsv file
osm ='http://www.openstreetmap.org/index.html?mlat=' + lat + '&mlon=' + lon + '&zoom=18'
f_path = geofix_dir + 'geofix.tsv'
f = open(f_path,'a')
f.write(str(dt) + '\t' + str(lat) + '\t' + str(lon) + '\t' + digikam + '\t' + osm + '\n')
f.close()
#Save the prepared data in the geofix.sqlite database
if os.path.exists(geofix_dir + 'geofix.sqlite'):
    sql_query = "INSERT INTO geofix (dt, lat, lon, digikam, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (dt, lat, lon, digikam, osm)
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute(sql_query)
    conn.commit()
    conn.close()
else:
    #Create the database if it doesn't exist
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute("CREATE TABLE geofix (id INTEGER PRIMARY KEY, dt VARCHAR, lat VARCHAR, lon VARCHAR, digikam VARCHAR, osm_url VARCHAR)")
    sql_query = "INSERT INTO geofix (dt, lat, lon, digikam, osm_url) VALUES ('%s', '%s', '%s', '%s', '%s')" % (dt, lat, lon, digikam, osm)
    conn = sqlite3.connect(geofix_dir + 'geofix.sqlite')
    conn.execute(sql_query)
    conn.commit()
    conn.close()

droid.vibrate()
