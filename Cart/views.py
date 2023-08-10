from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView
from .models import Cart
from Cart.models import *
from Cart.templates import *


# Create your views here.

# class CartView(ListView, request):
#
#     model = Cart
#     template_name = 'cart.html'
#     context_object_name = 'cart'
#
#     order_id = request.COOKIES.get('order_id')
#     order = Order.objects.get(id=order_id)
#     items = Order.objects.get(id=order_id).orderitem_set.all()
#
#     total_items = 0
#
#     total_price = 0
#
#     for item in items:
#         total_items += item.quantity
#         total_price += item.product.price_with_profit * item.quantity
#
#     cartItems = {}
#
#     context = {'items': items, 'order': order, 'cartItems': cartItems, 'total_items': total_items, 'total_price': total_price}
#

def cart(request):

    # if request.user.is_authenticated:
    #     customer = request.user
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #     cartItems = order['get_cart_items']

    order_id = request.COOKIES.get('order_id')
    order = Order.objects.get(id=order_id)
    items = Order.objects.get(id=order_id).orderitem_set.all()

    total_items = 0

    total_price = 0

    for item in items:
        total_items += item.quantity
        total_price += item.product.price_with_profit * item.quantity

    cartItems = {}

    context = {'items': items, 'order': order, 'cartItems': cartItems, 'total_items': total_items, 'total_price': total_price}
    return render(request, 'cart.html', context)