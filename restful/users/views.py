from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Projects
from .serializers import UserSerializer, ProjectSerialzer

def index(request):
    return HttpResponse("Hello, world. You're are now seeing the rsquarelabs-xyz APIs .")



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset =  Projects.objects.all()
    serializer_class = ProjectSerialzer


from django.http import HttpResponse
from . import tasks

def test_celery(request):
	result = tasks.add.delay(10 , 30)

	return HttpResponse(result.task_id)