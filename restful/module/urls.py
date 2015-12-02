__author__ = 'rrmerugu'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^testapi', views.TestApi.as_view()),

]