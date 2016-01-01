from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'username']

    username = models.CharField(max_length=254, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    is_developer = models.BooleanField(default=False)


class Projects(models.Model):
    project_id = models.CharField(max_length=16)
    project_name = models.CharField(max_length=150)
