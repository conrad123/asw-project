#!/bin/bash

PROJECT_DIR=/home/vagrant/server

##
#	Running server at 10.10.10.10:8080
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon server;./manage.py runserver 0.0.0.0:8080;deactivate;"

exit 0