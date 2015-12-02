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
<VirtualHost *:80>


</VirtualHost>
```

## Cautions 
1. Dont upgrade the mongoengine==0.9.0  to mongoengine==0.1.x, Django support has been split from the main MongoEngine repository. The legacy Django extension may be found bundled with the 0.9 release of MongoEngine. http://docs.mongoengine.org/django.html#django-support
2. User pymongo==2.8.x only 
3. Modules from requirements.txt only are supported. 


