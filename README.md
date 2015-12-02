# Django-seed
The seed project with the implementation of REDIS, Celery, MongoEngine, django rest framework to quickly get started 

This seed will be installed and configured with 

1. Django
2. Mongoengine
3. Logging 
4. DjangoRestFramework
5. Sending Emails to Admin on Errors (TODO)
6. Celery (TODO)
7. Redis/RabbitMQ (TODO)
 
 
## Requirements 
``
sudo yum install python27
sudo pip install virtualenv
``

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
3. Basic queuing of tasks with Celery
2. Send emails to admins on errors 



## Cautions 
1. Dont upgrade the mongoengine==0.9.0  to mongoengine==0.1.x, Django support has been split from the main MongoEngine repository. The legacy Django extension may be found bundled with the 0.9 release of MongoEngine. http://docs.mongoengine.org/django.html#django-support
2. User pymongo==2.8.x only 
3. Modules from requirements.txt only are supported. 


