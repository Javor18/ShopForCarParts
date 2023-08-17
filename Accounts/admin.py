from django.contrib import admin

# Register your models here.

from Accounts.models import Customer
from Accounts.models import WishlistItem

class CustomerAdmin(admin.ModelAdmin):

    list_display = ['email','username', 'is_staff']

    class Meta:
        model = Customer


admin.site.register(Customer, CustomerAdmin)
admin.site.register(WishlistItem)
