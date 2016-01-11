from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from . import tasks
from rest_framework import viewsets
from core.models import  Project, Post, Subscriber, MyUser
from .serializers import UserSerializer, ProjectSerialzer, PostSerializer, SubscriberSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
##http://jpadilla.com/post/73791304724/auth-with-json-web-tokens
from django.views.decorators.cache import never_cache
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from datetime import datetime


logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world. You're are now seeing the rsquarelabs-xyz APIs .")



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)



class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset =  Project.objects.all()
    serializer_class =  ProjectSerialzer

    def create_from_client(self, request, *args, **kwargs):
        logger.debug("Create projects from client")
        return viewsets.ModelViewSet.create(self, request, *args, **kwargs)




class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer




def test_celery(request):
	result = tasks.add.delay(10 , 30)
	return HttpResponse(result.task_id)





class TestCache(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (AllowAny,)

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






class TestDecorator(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes =  (JSONWebTokenAuthentication,)

    @never_cache
    def get(self, request, format=None):
        logger.debug(request.user)
        print "XXOOXX %s" %request.user.username
        data = {'test': 'decorator'}
        return Response(data)



