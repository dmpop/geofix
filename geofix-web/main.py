#!/usr/bin/python

#!/usr/bin/python

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

import sqlite3, os, sys
from PIL import Image
from bottle import route, run, debug, template, request, redirect, static_file

@route ('/geofix/optimize')
def optimize():
    path = "static/snapshots/"
    dirs = os.listdir(path)
    target_size = 800
    for item in dirs:
        if os.path.isfile(path+item):
            img = Image.open(path+item)
            f, e = os.path.splitext(item)
            original_size = max(img.size[0], img.size[1])
            if original_size >= target_size:
                wpercent = (target_size/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                img = img.resize((target_size,hsize), Image.ANTIALIAS)
                img.save(path+item, 'JPEG', quality=90)
    return redirect('/geofix')

@route('/geofix')
def geofix():
    if os.path.exists('static/geofix.sqlite'):
        conn = sqlite3.connect('static/geofix.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM geofix ORDER BY dt DESC")
        result = c.fetchall()
        c.close()
        output = template('main.tpl', rows=result)
        return output
    else:
        return ('The geofix.sqlite database is not found')

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/snapshot/:dt')
def snapshot(dt):
    conn = sqlite3.connect('static/geofix.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM geofix WHERE dt LIKE ?", (dt, ))
    conn.commit()
    return template('snapshot.tpl', dt=dt)

@route('/delete/:no', method='GET')
def delete(no):

    if request.GET.get('delete','').strip():
        conn = sqlite3.connect('static/geofix.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM geofix WHERE dt LIKE ?", (no, ))
        conn.commit()
        os.remove('static/snapshots/' + no + '.jpg')

        return redirect('/geofix')
    else:
        return template('delete.tpl', no=no)

run(host="0.0.0.0",port=8381, debug=True, reloader=True)