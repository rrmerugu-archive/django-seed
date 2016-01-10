__author__ = 'rrmerugu'
from django.db import models
from django.contrib import admin
from django.utils import timezone
from .utils import  get_client_ip

import logging
logger = logging.getLogger(__name__)

project_type_choices = (
    ("r2_gromacs", "R2 GROMACS"),
    ("r2_qsar", "R2 QSAR"),
    ("r2_scraper", "R2 SCRAPER")
)

class Project(models.Model):

    project_id = models.AutoField(primary_key=True )
    project_key = models.CharField(max_length=100, blank=False, null=False)
    project_name = models.CharField(max_length=200)
    project_tags = models.CharField(max_length=500)

    project_config = models.CharField(max_length=500)
    project_path = models.CharField(max_length=500)
    project_type = models.CharField(max_length=30, choices=project_type_choices)
    project_log = models.CharField(max_length=500)
    project_started = models.DateTimeField(auto_now_add=timezone.now())
    project_user_email = models.EmailField(max_length=100)
    project_ip_address = models.GenericIPAddressField(null=True, blank=True, default="0.0.0.0")



    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        logger.debug(kwargs)

        super(Project, self).save(*args, **kwargs)




def mark_as_done(modeladmin, request, queryset):
    queryset.update(status='p')





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


class Subscriber(models.Model):
    subscriber_id = models.IntegerField()
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())
    date_updated = models.DateTimeField(blank=True, null =True)


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Subscriber)
# admin.site.register(Project)