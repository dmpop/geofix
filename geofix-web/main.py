#!/usr/bin/python
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
        output = template('geofix.tpl', rows=result)
        return output
    else:
        return ('The geofix.sqlite database is not found')

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

run(host="0.0.0.0",port=8381, debug=True, reloader=True)
