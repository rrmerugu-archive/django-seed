from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from core.models import  Project, Post, Subscriber
from core.auth import  User
from .serializers import UserSerializer, ProjectSerialzer, PostSerializer, SubscriberSerializer
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny

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



# def token_required(request):
#     logger.debug(request)
#     logger.debug(request.data)
#
#     return None
#
# @token_required


#
#
# class TokenVerify(BasePermission):
#
#     def has_permission(self, request, view):
#         logger.debug(request)
#         logger.debug(request.data)
#         logger.debug(request.user)
#         # logger.debug(request.META.get('HTTP_AUTHORIZATION'))
#         token = request.META.get('HTTP_AUTHORIZATION')
#         logger.debug(token)
#         logger.debug(request.auth)
#         if token is None:
#             # clearly not authorised
#             return False
#         else :
#             # chance - might be authorised
#             return False
#
#         return False

from rest_framework_jwt.authentication import JSONWebTokenAuthentication



##http://jpadilla.com/post/73791304724/auth-with-json-web-tokens

class TestDecorator(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes =  (JSONWebTokenAuthentication,)
    def get(self, request, format=None):
        logger.debug(request.user)
        print "XXOOXX %s" %request.user.username
        data = {'test': 'decorator'}
        return Response(data)