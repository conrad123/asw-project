#!/bin/bash

echo "==============================================================================="
echo "Database environment installation is beginning. This may take a few minutes..."
echo "==============================================================================="

##
#	Install core components
##
echo "Updating package repositories..."
apt-get update

echo "Installing required packages..."
apt-get -y install git

echo "Installing and upgrading pip..."
apt-get -y install python-setuptools
easy_install -U pip

echo "Installing required packages for NFS file sharing for vagrant..."
apt-get -y install nfs-common

echo "Installing required packages for postgresql..."
apt-get -y install postgresql

echo "Installing required packages for python package 'psycopg2'..."
apt-get -y install python-dev python3-dev libpq-dev

##
#	Setup the database
##
echo "Configuring postgresql..."
sudo -u postgres psql -c "create user vagrant with password 'vagrant';"
sudo -u postgres psql -c "create database vagrant;"
sudo -u postgres psql -c "grant all privileges on database vagrant to vagrant;"

echo "Installing python packages for postgresql..."
apt-get -y install python-psycopg2
pip install dj-database-url

echo "Changing default settings of postgresql..."
sudo cp /home/vagrant/database/pg_hba.conf /etc/postgresql/9.3/main/
sudo cp /home/vagrant/database/postgresql.conf /etc/postgresql/9.3/main/
sudo reboot

##
#	Setup is complete.
##
echo "==============================================================================="
echo "Database environment is complete."
echo "==============================================================================="

exit 0