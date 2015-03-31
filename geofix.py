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

import android, time, sys
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
    droid.makeToast('Network: ' + str(net_lat) + ' ' + str(net_lon))
except (KeyError):
    droid.makeToast('Failed. Please try again.')
    sys.exit()

try:
    gps = location['gps']
    gps_lat = gps['latitude']
    gps_lon = gps['longitude']
    OSM='http://www.openstreetmap.org/index.html?mlat=' + str(gps_lat) + '&mlon=' + str(gps_lon) + '&zoom=18'
    f_path = '/sdcard/geofix_gps.tsv'
    f = open(f_path,'a')
    f.write(str(date_stamp) + '\t' + str(time_stamp) + '\t' + str(gps_lat) + '\t' + str(gps_lon) + '\t' + OSM + '\n')
    f.close()
    droid.makeToast('GPS: ' + str(net_lat) + ' ' + str(net_lon))
except (KeyError):
    droid.makeToast('Failed. Please try again.')
    sys.exit()

droid.notify('Geofix', 'All done!')
