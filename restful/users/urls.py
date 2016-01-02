from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectsViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^test-task$', views.test_celery),
]
