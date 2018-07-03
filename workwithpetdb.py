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
print '<b><u>MYAPP</u></b><br><br>'
print '<input type="button" value="Reload Page" onClick="window.location.reload()">'

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



print '<br><br>'
cursor.execute( "SHOW SESSION VARIABLES WHERE Variable_name IN ('wsrep_cluster_name', 'wsrep_cluster_address', 'wsrep_node_address', 'version', 'wsrep_node_name', 'hostname', 'timestamp')" )
data = cursor.fetchall()
print(json2html.convert(json = data))

print '<br>'
print '<br>'

print '<table style="width:1%;white-space:nowrap;">'
print ' <form action="insert.py" method="POST">'
print '  <tr><th>Nome</th><th><input type="text" name="name" value="Bobby"></th></tr>'
print '  <tr><th>Dono</th><th><input type="text" name="owner" value="Pedro"></th></tr>'
print '  <tr><th>Especie</th><th><input type="text" name="species" value="Dog"></th></tr>'
print '  <tr><th>Sexo</th><th><input type="text" name="sex" value="m"></th></tr>'
print '  <tr><th>Data Nascimento</th><th><input type="text" name="birth" value="2015-03-15"></th></tr>'
print '  <tr><th></th></tr>'
print '  <tr><th><input type="submit" value="Inserir na DB"></th></tr>'
print ' </form>'
print '</table>'

cursor.execute( "SELECT * FROM pet" )
data = cursor.fetchall()
print '<br'>
print '  Web Server: ' + srvhostname + ' (<a href="haproxy?stats">stats</a>)<br>'
print '  DB LB Server: ' + conn.host + ':' + str(conn.port) + ' (<a href="http://' + conn.host + '/haproxy?stats">stats</a>)<br>'
print '<br>'
print(json2html.convert(json = data))

print '</body></html>'
