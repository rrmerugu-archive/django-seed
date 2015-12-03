from django.conf.urls import url, include
from rest_framework_mongoengine import routers

from . import views

router = routers.MongoSimpleRouter(trailing_slash=False)
router.register(r'blog', views.BlogViewSet, base_name='blog')

urlpatterns = [
    url(r'^testapi', views.TestApi.as_view()),
    url(r'^', include(router.urls))

]
