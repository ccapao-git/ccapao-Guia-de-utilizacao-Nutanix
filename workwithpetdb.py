#!/usr/bin/env python

from pymysql import connect, err, sys, cursors
from json2html import *

import cgitb
cgitb.enable()

print "Content-type: text/html"
print
print "<html><head>"
print ""
print "</head><body>"
print "Here you have:<br><br>"

conn = connect( host = 'MYHOST',
                        port = MYPORT,
                        user = 'MYUSER',
                        passwd = 'MYPASS',
                        db = 'MYDB' );

cursor = conn.cursor( cursors.DictCursor );

cursor.execute( "SELECT * FROM pet" )
data = cursor.fetchall()

print(json2html.convert(json = data))
print "</body></html>"
