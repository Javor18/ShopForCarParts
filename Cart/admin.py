from django.contrib import admin

# Register your models here.

from Cart.models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):

    list_display = ["id", "customer", "date_ordered", "status"]

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):

    list_display = ["id", "product", "order", "quantity", "date_added"]

admin.site.register(OrderItem, OrderItemAdmin)

