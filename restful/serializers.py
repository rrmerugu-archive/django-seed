__author__ = 'rrmerugu'


from rest_framework import   serializers
from django.http import JsonResponse
from core.models import Project, Post, Subscriber, MyUser

import logging
logger = logging.getLogger(__name__)


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('password', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        return MyUser.objects.register_user(**validated_data)


class ProjectSerialzer(serializers.ModelSerializer):

    class Meta:
        model= Project


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber