__author__ = 'rrmerugu'

from django.db import models
from django.contrib import admin
from django.utils import timezone


class Project(models.Model):
    project_id = models.IntegerField()
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name



def mark_as_done(modeladmin, request, queryset):
    queryset.update(status='p')

admin.site.register(Project)



class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, unique=True, db_index=True)
    title_slug = models.CharField(max_length=300, unique=True, db_index=True)
    text = models.TextField()
    created_date = models.DateTimeField( default=timezone.now)
    published_date = models.DateTimeField( blank=True, null=True)
    category = models.ForeignKey(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




admin.site.register(Post)
admin.site.register(Category)