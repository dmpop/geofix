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

import sqlite3, os
from bottle import route, run, debug, template, request, redirect, static_file

@route('/geofix')
def geofix():
    if os.path.exists('static/Geofix/geofix.sqlite'):
        conn = sqlite3.connect('static/Geofix/geofix.sqlite')
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
    conn = sqlite3.connect('static/Geofix/geofix.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM geofix WHERE dt LIKE ?", (dt, ))
    conn.commit()
    return template('snapshot.tpl', dt=dt)

@route('/delete/:no', method='GET')
def delete(no):

    if request.GET.get('delete','').strip():
        conn = sqlite3.connect('static/Geofix/geofix.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM geofix WHERE dt LIKE ?", (no, ))
        conn.commit()
        os.remove('static/Geofix/' + no + '.jpg')

        return redirect('/geofix')
    else:
        return template('delete.tpl', no=no)

run(host="0.0.0.0",port=8381, debug=True, reloader=True)