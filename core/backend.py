__author__ = 'rrmerugu'
from django.contrib.auth.backends import ModelBackend
from core.auth import  MyUser



class CustomModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        print username
        print password
        try:
            user = MyUser.objects.get(username=username)
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