from __future__ import unicode_literals
from django.db import models
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# from django.contrib.auth.models import User as BaseUser, PermissionsMixin, BaseUserManager, UserManager


## https://www.caktusgroup.com/blog/2013/08/07/migrating-custom-user-model-django/
## http://www.roguelynn.com/words/django-custom-user-models/



from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    # Last login, is active, and password are included automatically
    username                        =       models.CharField(max_length=30, blank=False, unique=True, )
    email                           =       models.EmailField(max_length=150, blank=False)
    date_joined                       =       models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']




class Projects(models.Model):
    project_id = models.CharField(max_length=16)
    project_name = models.CharField(max_length=150)
