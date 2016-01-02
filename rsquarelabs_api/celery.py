from __future__ import absolute_import
import os


from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rsquarelabs_api.settings')

worker = Celery('rsquarelabs_api')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
worker.config_from_object('django.conf:settings')
worker.autodiscover_tasks(lambda: settings.INSTALLED_APPS)