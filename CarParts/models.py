from django.db import models

# Create your models here.

class Tires(models.Model):

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

    season = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.brand} {self.model} {self.price}"

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
