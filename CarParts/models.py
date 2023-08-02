from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Tyre(models.Model):

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    ean_num = models.CharField(max_length=100, null=True, blank=True)
    mpn_num = models.CharField(max_length=100, null=True, blank=True)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    season = models.CharField(max_length=100)

    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    width = models.IntegerField()
    height = models.IntegerField()
    type = models.CharField(max_length=100, null=True, blank=True)
    diameter = models.IntegerField()
    load_index = models.IntegerField()

    speed_index = models.CharField(max_length=100)
    rim_protection = models.BooleanField()
    run_flat = models.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.object_name_constant = "Tires"

    def get_verbose_name(self):
        return self.object_name_constant

    def __str__(self):
        return self.get_verbose_name()

    def __repr__(self):
        return f"{self.brand} {self.model} {self.price}"

    class Meta:
        # I want the verbose name to be equal to brand name
        verbose_name = "Tyre"
        verbose_name_plural = "Tyres"

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Book(models.Model):
    #    correct:
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING)
    # incorrect:
    # profile = models.ForeignKey(Profile)