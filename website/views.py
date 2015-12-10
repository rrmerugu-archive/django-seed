__author__ = 'rrmerugu'


from django.shortcuts import render_to_response
from django.template import RequestContext

def home_page(request):
    response = render_to_response('index.html', {'title':'Django Seed | RSQUARE LABS'}, context_instance=RequestContext(request))
    response.status_code = 200
    return response