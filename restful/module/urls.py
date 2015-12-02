__author__ = 'rrmerugu'
from django.conf.urls import url, include
from restful.module import views


from rest_framework_mongoengine import routers
router = routers.MongoSimpleRouter(trailing_slash=False)
router.register(r'blog', views.BlogViewSet, base_name='blog')


urlpatterns = [
    url(r'^testapi', views.TestApi.as_view()),
    url(r'^', include(router.urls))

]