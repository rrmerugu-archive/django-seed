from __future__ import unicode_literals

from django.db import models
from core.auth import User
# Create your models here.



class Projects(models.Model):
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=100)
    project_name_slug = models.CharField(max_length=150)
    project_owner = models.ForeignKey(User)
    project_tags = models.CharField(max_length=300)