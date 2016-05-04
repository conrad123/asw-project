#!/bin/bash

PROJECT_DIR=/home/vagrant/server
USER_HOME=/home/vagrant

echo "==============================================================================="
echo "Server environment installation is beginning. This may take a few minutes..."
echo "==============================================================================="

##
#	Install core components
##
echo "Updating package repositories.."
apt-get update

echo "Installing required packages.."
apt-get -y install git

echo "Installing and upgrading pip.."
apt-get -y install python-setuptools
easy_install -U pip

echo "Installing required packages for NFS file sharing for vagrant.."
apt-get -y install nfs-common

echo "Installing required packages for python package 'psycopg2'.."
apt-get -y install python-dev python3-dev libpq-dev

echo "Installing virtualenvwrapper from pip.."
pip install virtualenvwrapper

##
#	Setup virtualenvwrapper
##
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ${USER_HOME}/.bashrc

##
#	Setup virtualenv
##
echo "Install the virtual environment.."
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};mkvirtualenv --python=`which python3` server;deactivate;"

##
#	Installing required python packages
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon server;pip install -r requirements.txt;deactivate;"

##
#	Database migrations
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon server;./manage.py migrate;deactivate;"
echo "Migrations completed."

##
#	Setup is complete.
##
echo "==============================================================================="
echo "Server environment is complete."
echo "==============================================================================="

exit 0