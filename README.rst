Artblog
=======

This is a blog project for those who need a art-centric platform.

At the moment, it's mostly just boilerplate code, but that should change
in the coming weeks!

This project is still in development, and is not ready to be used.

If you'd like to use the boilerplate to work on development yourself,
check out the Requirements and Quick Start!


Requirements
============

For development, this project is using the following:

-Oracle VM VirtualBox and Vagrant (optional, but takes care of all the rest)
-python3
-pip3
-virtualenv and virtualenvwrapper
-Firefox (for Selenium tests)


Using Vagrant may make your life much easier.
If you'd like to do so, you can get VirtualBox from here: https://www.virtualbox.org/wiki/Downloads

Then, download Vagrant from here: https://www.vagrantup.com/

Note that if you use the Vagrant route, you shouldn't need the rest of the requirements.
They'll be installed on your VM when it sets up.  Feel free to just skip ahead to the quick start!


If you do choose to avoid Vagrant, for whatever reason, continue on with the rest of the requirements.

Python can be downloaded here: https://www.python.org/downloads/

Firefox can be downloaded here: https://www.mozilla.org/en-US/firefox/new/

Installing pip3, virtualenv, and virtualenvwrapper can be a pain depending on your system.
I would recommend Google-ing for instructions for your preferred operating system.


Quick Start Guide
=================

Download the Artblog Project from GitHub
----------------------------------------

First, you need to clone a local copy of the project from GitHub onto your desktop.
The project can be found here: https://github.com/Kalenai/artblog-project


Configure Oracle VM VirtualBox and start Vagrant
------------------------------------------------

Run VirtualBox once to make sure it's set up.
Next, open a shell or terminal in the root project folder for the artblog-project and run:
::

  $ vagrant up

This will download the Vagrant box and run provisioning, downloading and installing
all requirements, setting environment variables, and setting up virtual environments
for testing and staging, all within the VM where it won't affect your main system.


SSH into your new Vagrant VM
----------------------------

Once your VM is up, you can access it by SSH.  If your console supports SSH, you can
do this by typing:
::

  $ vagrant ssh

Otherwise, I would recommend using PuTTY (you can convert the SSH key using PuTTYgen).


Navigating the default virtual environments
-------------------------------------------

As the VM is set up, the default environment (using no virtualenv) is for development.
Use one of the following commands to access your environments for testing and staging:
::

  $ workon testing-env
  $ workon staging-env

To deactivate them, use:
::

  $ deactivate

Note that you can also edit '/vagrant/setup.sh' in your project folder if you'd rather
use a different setup for the virtualenvs.


Django Secret Key
-----------------

Note that the SECRET_KEY variable used in the VM is **not** secure!
**Do not deploy using the default key!**

You can generate a secure SECRET_KEY here: http://www.miniwebtool.com/django-secret-key-generator


Not using Vagrant
-----------------

I have not done any development on this project without using Vagrant.  The development tools,
such as the included tests, are written to be used with Vagrant, so I recommend sticking with that.

However, if you do wish to avoid Vagrant, you'll need to install the requirements manually,
create virtual environments, and install Python requirements from their respective lists in
the 'requirements' folder.

Many of the tests are written to be used headlessly using pyvirtualdisplay, so you may wish
to modify them to fit your desired development environment.