#!/bin/bash

PROJECT_DIR=/home/vagrant/site
USER_HOME=/home/vagrant

echo "Environment installation is beginning. This may take a few minutes.."

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

echo "Installing required packages for postgres.."
apt-get -y install postgresql

echo "Installing required packages for python package 'psycopg2'.."
apt-get -y install python-dev python3-dev libpq-dev

echo "Installing virtualenvwrapper from pip.."
pip install virtualenvwrapper

##
#	Setup the database
##
echo "Configuring postgres.."
sudo -u postgres psql -c "create user vagrant with password 'vagrant';"
sudo -u postgres psql -c "create database vagrant;"
sudo -u postgres psql -c "grant all privileges on database vagrant to vagrant;"

##
#	Setup virtualenvwrapper
##
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ${USER_HOME}/.bashrc

##
#	Setup virtualenv
##
echo "Install the virtual environment.."
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};mkvirtualenv --python=`which python3` site;deactivate;"

##
#	Installing required python packages
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon site;pip install -r requirements.txt;deactivate;"

##
#	Creating django project
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon site;django-admin.py startproject prova .;deactivate;"
echo "Django application created."

##
#	Database migrations
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon site;./manage.py migrate;deactivate;"
echo "Migrations completed."

##
#	Copying source code in project folder
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon site;cp -r /home/vagrant/site/src/* /home/vagrant/site/prova;deactivate;"

##
#	Running server at localhost:8080
##
# sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon site;./manage.py runserver 0.0.0.0:8080;deactivate;"

##
#	Setup is complete.
##
echo ""
echo "The environment has been installed."
echo ""
echo "You can start the machine by running: vagrant up"
echo "You can ssh to the machine by running: vagrant ssh"
echo "You can stop the machine by running: vagrant halt"
echo "You can delete the machine by running: vagrant destroy"
echo ""
exit 0
