__author__ = 'rrmerugu'

from .models import Blog
from rest_framework_mongoengine.serializers import  DocumentSerializer

import logging
logger = logging.getLogger(__name__)

class BlogSerializer(DocumentSerializer):
    class Meta:
        model = Blog