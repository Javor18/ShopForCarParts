import json
import string
import random

from .models import *
from CarParts.models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
        print('cookie cart')
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']
            tire = Tyre.objects.get(id=i)
            total = (tire.price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            item = {
                'product': {
                    'id': tire.id,
                    'brand': tire.brand,
                    'model': tire.model,
                    'price': tire.price,
                },
                'quantity': cart[i]['quantity'],
                'get_total': total,
            }
            items.append(item)
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):

    cookieData = cookieCart(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']

    cart_data = {'cartItems': cartItems, 'order': order, 'items': items}
    print(cart_data)
    return cart_data

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

    return result_str