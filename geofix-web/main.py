#!/usr/bin/python
import sqlite3, os
from bottle import route, run, debug, template, request, redirect, static_file

@route('/geofix')
def geofix():
    if os.path.exists('geofix.sqlite'):
        conn = sqlite3.connect('geofix.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM geofix ORDER BY d_stamp DESC")
        result = c.fetchall()
        c.close()
        output = template('geofix.tpl', rows=result)
        return output
    else:
        return ('The geofix.sqlite database is not found')

@route('/delete/:no', method='GET')
def delete(no):

    if request.GET.get('delete','').strip():
        conn = sqlite3.connect('geofix.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM geofix WHERE id LIKE ?", (no, ))
        conn.commit()

        return redirect('/geofix')
    else:
        return template('delete.tpl', no=no)

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0",port=8381, debug=True, reloader=True)
