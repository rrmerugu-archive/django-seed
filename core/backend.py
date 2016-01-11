__author__ = 'rrmerugu'
from django.contrib.auth.backends import ModelBackend
from core.models import  MyUser



class CustomModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        print username
        print password
        try:
            user = MyUser.objects.get(email=username)
            print user, "--"
            if user.is_active:
                if user.check_password(password):
                    return user
            else:
                return None #user is not active / suspended
        except  MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None



#
# Logging In With Email Addresses in Django
# class EmailOrUsernameModelBackend(object):
#     def authenticate(self, username=None, password=None):
#         if '@' in username:
#             kwargs = {'email': username}
#         else:
#             kwargs = {'username': username}
#         try:
#             user = User.objects.get(**kwargs)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None
#
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
#
# AUTHENTICATION_BACKENDS = (
#     'myproject.accounts.backends.EmailOrUsernameModelBackend',
#     'django.contrib.auth.backends.ModelBackend'
# )