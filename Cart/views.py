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
        return Order.objects.filter(customer=self.request.user)