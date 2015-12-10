__author__ = 'rrmerugu'

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^', views.home_page, name='dashboard'),

]