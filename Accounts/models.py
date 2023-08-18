from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from CarParts.models import Tyre



from Accounts import apps


#
# # Create your models here.
#

class Customer(AbstractUser):

    phone = models.CharField(max_length=200, null=True, blank=True)


UserModel = get_user_model()
class WishlistItem(models.Model):
    user = models.ForeignKey(UserModel, null=True, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Tyre , on_delete=models.CASCADE)