#!/bin/sh
# CALM Service Name = WebService
# AVISO: ter em conta que os packages sao download do repositorio publico directamente, 
#        pelo que pode levar algum tempo a concluir

set -ex

sudo hostnamectl set-hostname @@{name}@@
sudo hostnamectl

sudo echo Nutanix CALM array identifier: @@{calm_array_index}@@ | sudo tee /tmp/arrayid.calm

sudo yum install -y epel-release
sudo yum update -y

sudo yum install -y httpd

#sudo yum install -y firewalld
#sudo systemctl enable firewalld
#sudo systemctl start firewalld

#sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
#sudo firewall-cmd --reload
#sudo firewall-cmd --list-all

sudo yum install -y wget
sudo yum install -y python
sudo yum install -y python-pip
sudo pip install pymysql
sudo pip install json2html

sudo setsebool -P httpd_can_network_connect_db=1

sudo cp -p /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.backup

sudo grep -v 'DocumentRoot "/var/www/html"' /etc/httpd/conf/httpd.conf.backup | sudo tee /etc/httpd/conf/httpd.conf

sudo tee -a /etc/httpd/conf/httpd.conf <<<'

# myapp custom config

DocumentRoot "/var/www/myapp"

<Directory "/var/www/myapp">
    Options Indexes FollowSymLinks
    Options +ExecCGI
    DirectoryIndex index.py
    AddHandler cgi-script .py
</Directory>
'

sudo chmod 644 /etc/httpd/conf/httpd.conf

sudo mkdir /var/www/myapp
sudo chmod 755 /var/www/myapp

sudo wget https://raw.githubusercontent.com/ccapao-git/ccapao-Guia-de-utilizacao-Nutanix/master/workwithpetdb.py

sudo sed 's/MYAPP/@@{calm_application_name}@@/g' ./workwithpetdb.py | \
sudo  sed 's/MYHOST/@@{DBService.address}@@/g' | \
sudo  sed 's/MYPORT/3306/g' | \
sudo  sed 's/MYUSER/@@{CUSTDBUSER}@@/g' | \
sudo  sed 's/MYPASS/@@{CUSTDBPASS}@@/g' | \
sudo  sed 's/MYDB/@@{CUSTDBNAME}@@/g' > index.py

sudo mv index.py /var/www/myapp/index.py
sudo chown apache:apache /var/www/myapp/index.py
sudo chcon -t httpd_sys_script_exec_t /var/www/myapp/index.py
sudo chmod 755 /var/www/myapp/index.py
sudo ls -laZ /var/www/myapp/index.py

sudo rm -f workwithpetdb.py

sudo systemctl enable httpd
sudo systemctl start httpd
sudo systemctl -l status httpd

sudo curl http://127.0.0.1
