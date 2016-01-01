from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User as BaseUser

class User(models.Model):
    user_projects = models.CharField(max_length=30)