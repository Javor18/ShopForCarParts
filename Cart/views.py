from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView
from .models import Cart
from Cart.models import *
from Cart.templates import *


# Create your views here.

class CartView(LoginRequiredMixin, ListView):
    template_name = 'cart.html'

    def get_queryset(self):
        return OrderItem.objects.filter(order__customer=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()

        total_price = 0
        total_items = 0

        for item in context_data['object_list']:

            total_price += item.product.price * item.quantity
            total_items += item.quantity

        context_data["total_price"] = total_price
        context_data["total_items"] = total_items

        return context_data
