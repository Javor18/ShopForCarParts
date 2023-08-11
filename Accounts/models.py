from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, User
from django.contrib.auth import models as auth_models
from django.contrib.auth import get_user_model
from django.shortcuts import render
import form as form



from Accounts import apps


#
# # Create your models here.
#

class Customer(models.Model):

    user = models.OneToOneField(User, null=True, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
