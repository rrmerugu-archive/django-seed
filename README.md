# Django-seed
The seed project with the implementation of REDIS, Celery, MongoEngine, django rest framework to quickly get started 

This seed will be installed and configured with 

1. Mongoengine
2. redis 
3. celery
4. 
 


## Installing the VirtualEnv
```
sudo pip install virtualenv
mkdir djang-seed
cd django-seed
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
    ServerAdmin rsquarelabs@gmail.com
    DocumentRoot /var/www/html/api.rsquarelabs.xyz/server
    ServerName api.rsquarelabs.xyz

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

## Cautions 
1. Dont upgrade the mongoengine==0.9.0  to mongoengine==0.1.x, Django support has been split from the main MongoEngine repository. The legacy Django extension may be found bundled with the 0.9 release of MongoEngine. http://docs.mongoengine.org/django.html#django-support
2. User pymongo==2.8.x only 
3. Modules from requirements.txt only are supported. 


