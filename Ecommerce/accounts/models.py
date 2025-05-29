from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    phone = models.CharField(verbose_name='phone number', max_length=11, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(verbose_name='full name', max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.phone
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin