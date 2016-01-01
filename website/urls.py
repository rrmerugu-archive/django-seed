__author__ = 'rrmerugu'
from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.home_page, name='homepage'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^main/$', views.main, name='main'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^register/$', views.register, name='logout'),
    url(r'^welcome/$', views.register_success, name='logout'),



    url(r'^user/password/reset/$',  'django.contrib.auth.views.password_reset',
     {'post_reset_redirect' : '/user/password/reset/done/'}, name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),

]