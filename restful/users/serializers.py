__author__ = 'rrmerugu'


from rest_framework import   serializers
from .models import Projects
from core.auth import User
# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class ProjectSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Projects