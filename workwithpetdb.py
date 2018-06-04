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

if socket.gethostname().find('.')>=0:
    srvhostname=socket.gethostname()
else:
    srvhostname=socket.gethostbyaddr(socket.gethostname())[0]

conn = connect( host = 'MYHOST',
                        port = 3306,
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
cursor.execute( "SHOW SESSION VARIABLES WHERE Variable_name IN ('wsrep_cluster_name', 'wsrep_cluster_address', 'wsrep_node_address', 'version', 'wsrep_node_name', 'hostname', 'timestamp')" )
data = cursor.fetchall()
print(json2html.convert(json = data))


print '<br><br>'
print '<form action="insert.py" method="POST">'
print ' Nome<br><input type="text" name="name" value="Bobby"><br><br>'
print ' Dono<br><input type="text" name="owner" value="John"><br><br>'
print ' Especie<br><input type="text" name="species" value="Dog"><br><br>'
print ' Sexo<br><input type="text" name="sex" value="m"><br><br>'
print ' Data Nascimento<br><input type="text" name="birth" value="2015-03-15"><br><br>'
print ' Data Morte<br><input type="text" name="death" value=""><br><br>'
print ' <input type="submit" value="Inserir na DB">'
print ' </form>'

print '<input type="button" value="Reload Page" onClick="window.location.reload()">'
print '</body></html>'
