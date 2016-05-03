#!/bin/bash

PROJECT_DIR=/home/vagrant/site

##
#	Running server at localhost:8080
##
sudo su - vagrant /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;cd ${PROJECT_DIR};workon site;./manage.py runserver 0.0.0.0:8080;deactivate;"

exit 0