__author__ = 'rrmerugu'
from django.contrib.auth.backends import ModelBackend
from core.auth import  User



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