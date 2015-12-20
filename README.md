# Django-seed


[![Build Status](https://api.travis-ci.org/rsquarelabs/django-seed.svg)](https://travis-ci.org/rsquarelabs/django-seed)
[![codecov.io](https://codecov.io/github/rsquarelabs/django-seed/coverage.svg?branch=master)](https://codecov.io/github/rsquarelabs/django-seed?branch=master)
[![Requirements Status](https://requires.io/github/rsquarelabs/django-seed/requirements.svg?branch=master)](https://requires.io/github/rsquarelabs/django-seed/requirements/?branch=master)

The seed project with the implementation of REDIS, Celery, MongoEngine, django rest framework to quickly get started 


This seed will be installed and configured with

1. Django
2. Mongoengine
3. Logging 
4. DjangoRestFramework
5. Sending Emails to Admin on Errors (TODO)
6. Celery (TODO)
7. Redis/RabbitMQ (TODO)
 

 
You may try one of the pre-releases from here https://github.com/rsquarelabs/django-seed/releases/
 
## Requirements 

supports Python 2.7, 3.4, 3.5
```
sudo yum install python27 gcc httpd mod_wsgi-python27  libxml2-devel python-devel libxslt-devel libffi-devel openssl-devel
sudo pip install virtualenv
```

## Setting the project
```
git clone https://github.com/rsquarelabs/django-seed.git
cd django-seed/
```

## Installing the VirtualEnv
```
virtualenv . 
source bin/activate
```

## Installing the packages needed

```
pip install -r requirements.txt
```
###### For Ubuntu users,if there is any problem in installing pyyaml , run the following command
```
sudo apt-get install libyaml-dev libpython2.7-dev
```



## Running Development Mode
```
python manage.py runserver
```
Whenever there is a change happening in the files, the site reloads automatically. This by default will start the site at `http://localhost:8000`, you can start in different port by command `python manage.py runserver 0.0.0.0:9000`


### Running in Production Mode 

1. Installing django in Apache
`vi /etc/httpd/conf/httpd.conf `
```

# this section will be commented in the httpd.conf, uncomment them to use virtualhosts
NameVirtualHost *:80


# Add the WSGI settings
WSGISocketPrefix /var/run/wsgi
WSGIPythonPath /var/www/html/rsquarelabs.site/lib/python2.7/site-packages:/var/www/html/rsquarelabs.other/lib/python2.7/site-packages
WSGIDaemonProcess ec2-user processes=1 maximum-requests=500 threads=1
WSGIProcessGroup ec2-user


<VirtualHost *:80>
    ServerAdmin hello@rsquarelabs.xyz
    DocumentRoot /var/www/html/rsquarelabs.site/rsquarelabs
    ServerName rsquarelabs.site
    <Directory /var/www/html/rsquarelabs.site/rsquarelabs>
        <Files wsgi.py>
            Order allow,deny
            Allow from all
        </Files>
    </Directory>
    WSGIScriptAlias / /var/www/html/rsquarelabs.site/rsquarelabs/wsgi.py
    ErrorLog /var/www/html/rsquarelabs.site/logs/rsquarelabs.site-error_log
    CustomLog /var/www/html/rsquarelabs.site/logs/rsquarelabs.site-access_log common
</VirtualHost>
```

You **MUST have to RELOAD** the server to see the changes using the command `sudo service httpd reload` .


## TODO
1. Install and configure Celery and Redis/RabbitMQ 
2. Basic queuing of tasks with Celery
3. Send emails to admins on errors 
4. Add python packages path to the path if using virtualenv in `rsquarelabs/wsgi.py`


## Cautions 
1. Dont upgrade the mongoengine==0.9.0  to mongoengine==0.1.x, Django support has been split from the main MongoEngine repository. The legacy Django extension may be found bundled with the 0.9 release of MongoEngine. http://docs.mongoengine.org/django.html#django-support
2. User pymongo==2.8.x only 
3. Modules from requirements.txt only are supported. 

Yo
