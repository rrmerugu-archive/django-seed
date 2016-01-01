__author__ = 'rrmerugu'
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from restful.users.models import User
from django.contrib import auth


# from mongoengine.django.auth import MongoEngineBackend
#
#
# class FeaztSocialEmailBackend(MongoEngineBackend):
#
#     def authenticate(self, email=None, auth_thru=None, facebook_id=None, google_id=None, password=None, user=None):
#         proceed = False
#         if auth_thru == 'fb':
#             user = self.user_document.objects(email=email, auth_thru=auth_thru, facebook_id=facebook_id).first()
#             if user:
#                 proceed = True
#         elif auth_thru == 'google':
#             user = self.user_document.objects(email=email, auth_thru=auth_thru, google_id=google_id).first()
#             if user:
#                 proceed = True
#         elif auth_thru == 'email':
#             user = self.user_document.objects(email=email, auth_thru=auth_thru).first()
#             if user and user.check_password(password):
#                 if user.email_confirmed:
#                     proceed = True
#         elif auth_thru == 'directly':
#             user = user
#             proceed = True
#         if proceed:
#             backend = auth.get_backends()[1]
#             user.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
#             return user
#         return None



class CustomModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        print username
        print password
        try:
            user = User.objects.get(username=username)
            print user, "--"
            if user.is_active:
                if user.check_password(password):
                    return user
            else:
                return None #user is not active / suspended
        except  User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None