from django.shortcuts import render
from django.views.generic import ListView
from .models import Cart

# Create your views here.

class CartView(ListView):

    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart'
