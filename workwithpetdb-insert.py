#!/usr/bin/env python

from pymysql import connect, err, sys, cursors
from json2html import *
import socket
import cgitb
import cgi
#cgitb.enable()

print 'Content-type: text/html'
print
print '<html><head>'
print '<title>MYAPP</title>'
print '</head><body>'

conn = connect( host = 'MYHOST',
                        port = 3306,
                        user = 'MYUSER',
                        passwd = 'MYPASS',
                        db = 'MYDB' );

cursor = conn.cursor( cursors.DictCursor );

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('name')
owner = form.getvalue('owner')
species = form.getvalue('species')
sex = form.getvalue('sex')
birth = form.getvalue('birth')
death = form.getvalue('death')

cursor.execute("INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s)",[name,owner,species,sex,birth,death])
conn.commit()

print '<input type="button" value="Reload Page" onClick="location.href=\'index.py\'">'
print '</body></html>'
