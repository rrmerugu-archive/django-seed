from django.conf.urls import url, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
# router.register(r'user', views.UserViewSet)
router.register(r'project', views.ProjectViewSet)
router.register(r'post', views.BlogViewSet)
router.register(r'subscriber', views.SubscriberViewSet)


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^test-task$', views.test_celery),
    url(r'^test-cache', views.TestCache.as_view()),
    url(r'^test-decorator', views.TestDecorator.as_view()),
     url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
 url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
]
