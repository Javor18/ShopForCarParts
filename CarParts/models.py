import form as form
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import render


# Create your models here.

class ProductMixin(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)

    ean_num = models.CharField(max_length=100, null=True, blank=True)
    mpn_num = models.CharField(max_length=100, null=True, blank=True)

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        abstract = True

class Tyre(ProductMixin, models.Model):

    season = models.CharField(max_length=100)

    width = models.IntegerField()
    height = models.IntegerField()
    diameter = models.IntegerField()
    load_index = models.IntegerField()

    type = models.CharField(max_length=100, null=True, blank=True)

    speed_index = models.CharField(max_length=100)
    rim_protection = models.BooleanField()
    run_flat = models.BooleanField()

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        # I want the verbose name to be equal to brand name
        verbose_name = "Tyre"
        verbose_name_plural = "Tyres"
