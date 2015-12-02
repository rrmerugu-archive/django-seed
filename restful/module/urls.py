__author__ = 'rrmerugu'
from django.conf.urls import url
from restful.module import views

urlpatterns = [
    url(r'^testapi', views.TestApi.as_view()),
    # url(r'^blog/', views.BlogViewSet.as_view()),

]