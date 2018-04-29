#!/usr/bin/env python

from pymysql import connect, err, sys, cursors
from json2html import *
import socket
import cgitb
#cgitb.enable()

print 'Content-type: text/html'
print
print '<html><head>'
print '<title>MYAPP</title>'
print '</head><body>'

if socket.gethostname().find('.')>=0:
    srvhostname=socket.gethostname()
else:
    srvhostname=socket.gethostbyaddr(socket.gethostname())[0]

conn = connect( host = 'MYHOST',
                        port = MYPORT,
                        user = 'MYUSER',
                        passwd = 'MYPASS',
                        db = 'MYDB' );

cursor = conn.cursor( cursors.DictCursor );

cursor.execute( "SELECT * FROM pet" )
data = cursor.fetchall()

print
print "  Web Server: " + srvhostname + "<br>"
print "  DB Server: " + conn.host + ":" + str(conn.port) + "<br><br>"
print(json2html.convert(json = data))

print '<br><br>'
cursor.execute( "SELECT @@hostname" )
data = cursor.fetchall()
print(json2html.convert(json = data))

print
print "  Web Server: " + srvhostname + "<br>"
print "  DB Server: " + conn.host + ":" + str(conn.port) + "<br><br>"
print(json2html.convert(json = data))
print '<br><br>'
print '<input type="button" value="Reload Page" onClick="window.location.reload()">'
print '</body></html>'
