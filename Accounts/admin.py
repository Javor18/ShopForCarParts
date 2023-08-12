from django.contrib import admin

# Register your models here.

from Accounts.models import Customer
from Accounts.models import WishlistItem


admin.site.register(Customer)
admin.site.register(WishlistItem)
