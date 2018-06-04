#!/bin/sh
# CALM Service Name = DBService
# AVISO: ter em conta que os packages sao download do repositorio publico directamente, 
#        pelo que pode levar algum tempo a concluir

# AVISO: ter atenção ao comportamento na falha de um 2-node cluster http://galeracluster.com/documentation-webpages/twonode.html

set -ex

sudo hostnamectl set-hostname @@{name}@@
sudo hostnamectl

sudo echo Nutanix CALM array identifier: @@{calm_array_index}@@ | sudo tee /tmp/arrayid.calm

sudo yum install -y epel-release
sudo yum update -y

sudo yum install -y mariadb-server

#sudo yum install -y firewalld
#sudo systemctl enable firewalld
#sudo systemctl start firewalld

#sudo firewall-cmd --zone=public --add-port=3306/tcp --permanent
#sudo firewall-cmd --reload
#sudo firewall-cmd --list-all

sudo systemctl enable mariadb
sudo systemctl start mariadb
sudo systemctl -l status mariadb

sudo mysql -u root <<EOF
 show databases;
 create database @@{CUSTDBNAME}@@;
 show databases;
 create user '@@{CUSTDBUSER}@@'@'%' identified by '@@{CUSTDBPASS}@@';
 grant all privileges on @@{CUSTDBNAME}@@.* to '@@{CUSTDBUSER}@@'@'%';
 flush privileges;
 SELECT User, Host, Password FROM mysql.user;
 USE @@{CUSTDBNAME}@@;
 CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
 INSERT INTO pet VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);
 SELECT * from pet;
EOF
