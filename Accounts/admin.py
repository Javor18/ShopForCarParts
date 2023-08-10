from django.contrib import admin

# Register your models here.

from Accounts.models import Customer

admin.site.register(Customer)
