__author__ = 'rrmerugu'
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!, website starts here .")
