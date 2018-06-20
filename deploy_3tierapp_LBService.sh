#!/bin/sh
# CALM Service Name = LBService
# AVISO: ter em conta que os packages sao download do repositorio publico directamente, 
#        pelo que pode levar algum tempo a concluir

set -ex

sudo hostnamectl set-hostname @@{name}@@
sudo hostnamectl

sudo echo Nutanix CALM array identifier: @@{calm_array_index}@@ | sudo tee /tmp/arrayid.calm

sudo yum install -y epel-release
sudo yum update -y

sudo yum install -y haproxy

#sudo yum install -y firewalld
#sudo systemctl enable firewalld
#sudo systemctl start firewalld

#sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
#sudo firewall-cmd --reload
#sudo firewall-cmd --list-all

sudo tee -a /etc/haproxy/haproxy.cfg <<<'frontend http_front
 bind *:80
 stats uri /haproxy?stats
 default_backend http_back

backend http_back
 balance roundrobin'

hosts=$(echo "@@{WebService.address}@@" | sed 's/^,//' | sed 's/,$//' | tr "," "\n")

for host in $hosts
do
 echo " server host-${host} ${host}:80 weight 1 maxconn 100 check" | sudo tee -a /etc/haproxy/haproxy.cfg
done

sudo systemctl enable haproxy
sudo systemctl restart haproxy
sudo systemctl -l status haproxy
