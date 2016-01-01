__author__ = 'rrmerugu'
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return HttpResponse("Hello, world!, website starts here .")


def home_page(request):
    is_loggedin = True
    response = render_to_response('homepage.html', {'title':'RSQUARE LABS | Localised Intelligence', 'is_loggedin': is_loggedin}, context_instance=RequestContext(request))
    response.status_code = 200
    return response
