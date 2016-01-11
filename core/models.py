__author__ = 'rrmerugu'
from django.db import models
from django.contrib import admin
from django.utils import timezone
from .utils import  get_client_ip

import logging
logger = logging.getLogger(__name__)


from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password):
        user = self.create_user(email,
                first_name=first_name,
                password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def register_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        ## gather the token for the user and return it
        return user


class MyUser(AbstractBaseUser):
    # Last login, is active, and password are included automatically
    username =  models.CharField(max_length=30, blank=False)
    email    =  models.EmailField(max_length=150, blank=False, unique=True)
    date_joined =  models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)


    # Permission | Administration Purpose
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Permissions | Others
    is_scientist = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    interests = models.CharField(max_length=100)


    ## define the user manager class for User
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']


    def __str__(self): # __unicode__ on Python 2
        return self.email
    # These are needed for the admin
    # https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#custom-users-and-django-contrib-admin
    # Full example - https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#a-full-example
    # def is_active(self):
    #     return self.is_active

    def get_full_name(self):
        return "%s %s"%(self.first_name, self.last_name)

    def get_short_name(self):
        return "%s" %self.first_name
    #
    # def is_staff(self):
    #     return self.is_staff
    #
    # def is_admin(self):
    #     return self.is_admin
    #
    # def is_superuser(self):
    #     return self.is_superuser

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        app_label = "core"



project_type_choices = (
    ("r2_gromacs", "R2 GROMACS"),
    ("r2_qsar", "R2 QSAR"),
    ("r2_scraper", "R2 SCRAPER")
)



class Project(models.Model):

    project_id = models.AutoField(primary_key=True )
    project_key = models.CharField(max_length=100, blank=False, null=False)
    project_name = models.CharField(max_length=200)
    project_tags = models.CharField(max_length=500)

    project_config = models.CharField(max_length=500)
    project_path = models.CharField(max_length=500)
    project_type = models.CharField(max_length=30, choices=project_type_choices)
    project_log = models.CharField(max_length=500)
    project_started = models.DateTimeField(auto_now_add=timezone.now())
    project_user_email = models.EmailField(max_length=100)
    project_ip_address = models.GenericIPAddressField(null=True, blank=True, default="0.0.0.0")



    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        logger.debug(kwargs)

        super(Project, self).save(*args, **kwargs)




def mark_as_done(modeladmin, request, queryset):
    queryset.update(status='p')





class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title


class Post(models.Model):
    author = models.ForeignKey(MyUser)
    title = models.CharField(max_length=200, unique=True, db_index=True)
    title_slug = models.CharField(max_length=300, unique=True, db_index=True)
    text = models.TextField()
    created_date = models.DateTimeField( default=timezone.now)
    published_date = models.DateTimeField( blank=True, null=True)
    category = models.ForeignKey(Category)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    subscriber_id = models.IntegerField()
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now())
    date_updated = models.DateTimeField(default=timezone.now(),blank=True, null =True)


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Subscriber)
# admin.site.register(Project)