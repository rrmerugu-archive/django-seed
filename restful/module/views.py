__author__ = 'rrmerugu'

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from datetime import datetime
from django.http import JsonResponse

import logging
logger = logging.getLogger(__name__)


class TestApi(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        logger.debug("Testing the API")
        d = datetime.now()
        mesg = "TESTED : API at %s" %d
        response = {}
        response['mesg'] = mesg
        return JsonResponse(response, status=200)