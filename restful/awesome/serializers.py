import logging

from rest_framework_mongoengine.serializers import DocumentSerializer

from .models import Blog

logger = logging.getLogger(__name__)


class BlogSerializer(DocumentSerializer):
    class Meta:
        model = Blog
