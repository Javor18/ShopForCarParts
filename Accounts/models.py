# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
#
# # Create your models here.
#
# class User(AbstractUser):
#
#     is_customer = models.BooleanField(default=False)
#     is_mechanic = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_manager = models.BooleanField(default=False)
#     is_salesman = models.BooleanField(default=False)
#     is_delivery = models.BooleanField(default=False)
#     is_accountant = models.BooleanField(default=False)
#     is_owner = models.BooleanField(default=False)
#
#
#     def __str__(self):
#         return self.username