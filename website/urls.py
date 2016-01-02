__author__ = 'rrmerugu'
from django.conf.urls import url

from . import views
from django.contrib.auth.views import password_reset, password_reset_done

from django.contrib.auth import views as auth_views
urlpatterns =[
    url(r'^$', views.home_page, name='homepage'),
    url(r'^auth/login/$', views.login_user, name='login'),
    url(r'^user/$', views.main, name='main'),
    url(r'^auth/logout/$', views.logout_user, name='logout'),
    url(r'^auth/register/$', views.register, name='logout'),
    url(r'^auth/welcome/$', views.register_success, name='logout'),



    url(r'^auth/password-reset/$', password_reset,
     {'post_reset_redirect' : 'auth/password-reset-done/', 'template_name': 'password-reset.html'}, name="password_reset"),

    url(r'^auth/password-reset-done/$', password_reset_done,
        { 'template_name': 'password-reset-done.html'}, name="password_reset_done"),


]

