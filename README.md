# Django-seed
The seed project with the implementation of REDIS, Celery, MongoEngine, django rest framework to quickly get started 

This seed will be installed and configured with 

1. Mongoengine
2. redis 
3. celery
4. 


### Running in Development Mode
$python manage.py runserver




### Running in Production Mode 

1. Installing django in Apache
/var/httpd/conf/http.conf
<VirtualHost *:80>


</VirtualHost>




## Installing the VirtualEnv
```
sudo pip install virtualenv

mkdir djang-seed

cd django-seed

virtualenv . 

source bin/activate

```



pip install -r requirements.txt




## Cautions 
1. Dont upgrade the mongoengine==0.9.0  to mongoengine==0.1.x, Django support has been split from the main MongoEngine repository. The legacy Django extension may be found bundled with the 0.9 release of MongoEngine. http://docs.mongoengine.org/django.html#django-support



