__author__ = 'rrmerugu'

from django.db import models


class Projects(models.Model):
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=100)


