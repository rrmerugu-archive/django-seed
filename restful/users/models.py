from __future__ import unicode_literals
from django.db import models



#http://stackoverflow.com/questions/17896346/django-custom-user-authentication-nonetype-error
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



class Projects(models.Model):
    project_id = models.CharField(max_length=16)
    project_name = models.CharField(max_length=150)
