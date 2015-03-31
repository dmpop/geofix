# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import android, time, datetime
droid = android.Android()
droid.startLocating()
time.sleep(9)

dt = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
location = droid.readLocation().result

net = location['network']
net_lat = net['latitude']
net_lon = net['longitude']

gps = location['gps']
gps_lat = gps['latitude']
gps_lon = gps['longitude']

droid.makeToast(str(net_lat) + ' ' + str(net_lon) + '\n' + str(gps_lat) + ' ' +str(gps_lon))

OSM='http://www.openstreetmap.org/index.html?mlat=' + str(gps_lat) + '&mlon=' + str(gps_lon) + '&zoom=18'

f_path = '/sdcard/geofix.csv'
f = open(f_path,'a')
f.write(str(dt) + ',' + str(net_lat) + ',' + str(net_lon) + ',' + str(gps_lat) + ',' +str(gps_lon) + '\t' + OSM + '\n' )
f.close()
droid.notify('Geofix', 'All done!')
