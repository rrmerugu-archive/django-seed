import logging
from datetime import datetime

from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_mongoengine import viewsets  # , generics

from .models import Blog
from .serializers import BlogSerializer

logger = logging.getLogger(__name__)


class TestApi(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        logger.debug("Testing the API")
        d = datetime.now()
        mesg = "TESTED : API at %s" % d
        response = {}
        response['mesg'] = mesg
        return JsonResponse(response, status=200)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
