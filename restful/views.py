from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from core.models import  Project, Post, Subscriber
from core.auth import  User
from .serializers import UserSerializer, ProjectSerialzer, PostSerializer, SubscriberSerializer
from rest_framework.permissions import IsAuthenticated

import logging
logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world. You're are now seeing the rsquarelabs-xyz APIs .")



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This is the Project viewset.
    """
    permission_classes = (IsAuthenticated,)
    queryset =  Project.objects.all()
    serializer_class =  ProjectSerialzer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


from django.http import HttpResponse
from . import tasks

def test_celery(request):
	result = tasks.add.delay(10 , 30)
	return HttpResponse(result.task_id)


from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from datetime import datetime
from rest_framework import permissions


class TestCache(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        data = cache.get('time')
        logging.debug(datetime.now())

        if data is None:
            data = datetime.now()
            logger.debug("no cache found, so creating new one, %s" %data)

            cache.set('time', data)
        logger.debug("ending the test")
        return Response(data)


