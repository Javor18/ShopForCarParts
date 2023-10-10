import uuid

from django.db import models
from django.contrib.auth.models import User
from CarParts.models import Tyre
from django.contrib.auth import get_user_model



# Create your models here.

UserModel = get_user_model()

# class Cart(models.Model):
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
#     drink_name = models.CharField(max_length=300)
#     drink_price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(UserModel, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True, default=uuid.uuid4)
    status = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Tyre, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def get_total(self):
        return self.quantity * self.product_price