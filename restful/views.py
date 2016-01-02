from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from core.models import  Project, Post, Subscriber
from core.auth import  User
from .serializers import UserSerializer, ProjectSerialzer, PostSerializer, SubscriberSerializer
from rest_framework.permissions import IsAuthenticated



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



