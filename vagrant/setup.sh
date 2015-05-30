#!/usr/bin/env bash

# install most packages

apt-get update
apt-get install -y firefox nginx python3.4 python3-pip xvfb


# install base python requirements

pip3 install virtualenv virtualenvwrapper


# configure nginx
cp /vagrant/vagrant/nginx.conf /etc/nginx/sites-available/default
service nginx restart


# setup virtualenvwrapper

echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> /home/vagrant/.profile
echo "export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv" >> /home/vagrant/.profile
echo "export WORKON_HOME=/home/vagrant/.virtualenvs" >> /home/vagrant/.profile
echo "export PROJECT_HOME=/home/vagrant/Devel" >> /home/vagrant/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.profile
source /home/vagrant/.profile


# setup virtualenvs

mkvirtualenv -r /vagrant/requirements/dev.txt dev-env
echo "export DJANGO_SETTINGS_MODULE='artblog.settings.development'" >> $VIRTUAL_ENV/bin/postactivate
echo "export SECRET_KEY='Development Key - Change for Production'" >> $VIRTUAL_ENV/bin/postactivate
echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/predeactivate
echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/predeactivate

mkvirtualenv -r /vagrant/requirements/testing.txt testing-env
echo "export DJANGO_SETTINGS_MODULE='artblog.settings.testing'" >> $VIRTUAL_ENV/bin/postactivate
echo "export SECRET_KEY='Development Key - Change for Production'" >> $VIRTUAL_ENV/bin/postactivate
echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/predeactivate
echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/predeactivate

mkvirtualenv -r /vagrant/requirements/staging.txt staging-env
echo "export DJANGO_SETTINGS_MODULE='artblog.settings.staging'" >> $VIRTUAL_ENV/bin/postactivate
echo "export SECRET_KEY='Development Key - Change for Production'" >> $VIRTUAL_ENV/bin/postactivate
echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/predeactivate
echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/predeactivate


# run this if, for some reason, you need a virtualenv
# for production on your vagrant VM

# mkvirtualenv -r /vagrant/requirements/production.txt production-env
# echo "export DJANGO_SETTINGS_MODULE='artblog.settings.production'" >> $VIRTUAL_ENV/bin/postactivate
# echo "export SECRET_KEY='Development Key - Change for Production'" >> $VIRTUAL_ENV/bin/postactivate
# echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/predeactivate
# echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/predeactivate