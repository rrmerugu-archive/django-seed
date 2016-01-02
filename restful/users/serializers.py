__author__ = 'rrmerugu'


from rest_framework import   serializers
from core.models import Project
from core.auth import User
# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class ProjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Project