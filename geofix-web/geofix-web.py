#!/usr/bin/python
import sqlite3, os
from bottle import route, run, debug, template, request, static_file

@route('/geofix')
def wimb():
    if os.path.exists('geofix.sqlite'):
        conn = sqlite3.connect('geofix.sqlite')
        c = conn.cursor()
        c.execute("SELECT * FROM geofix ASC")
        result = c.fetchall()
        c.close()
        output = template('geofix.tpl', rows=result)
        return output
    else:
        return ('The geofix.sqlite database is not found')

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0",port=8080, debug=True, reloader=True)
