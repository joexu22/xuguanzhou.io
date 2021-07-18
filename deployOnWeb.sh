#!/bin/bash

# this script is basically what needs to be run by an AWS EC2 Instance
# place in Configure Instance Details, Advanced Details, User data

sudo yum -y update

sudo yum -y install httpd
sudo service httpd start

sudo yum -y install git
git clone https://github.com/joexu22/xuguanzhou.io.git
cd xuguanzhou.io

python3 -m pip install -r requirements.txt
pelican content -s pelicanconf.py -t ./themes/xuguanzhou/
sudo rsync -avc --delete output/ /var/www/html
