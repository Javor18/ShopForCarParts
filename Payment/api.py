import json
import uuid

import requests

import Cart.models
from CarShop import settings
from Cart.models import Order


def create_order(token):

    last_order = Order.objects.last()

    headers = {
        'Content-Type': 'application/json',
        'PayPal-Request-Id': str(uuid.uuid4()),
        'Authorization': f'Bearer {token}',
    }

    data = json.dumps({
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "reference_id": "a9f80740-38f0-11e8-b467-0ed5f89f718s",
                "amount": {
                    "currency_code": "USD",
                    "value": last_order.get_total_price
                },
                "payment_source": {
                    "paypal": {
                        "experience_context": {
                            "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
                            "payment_method_selected": "PAYPAL", "brand_name": "CarPartsShop",
                            "locale": "en-US", "landing_page": "LOGIN",
                            "shipping_preference": "SET_PROVIDED_ADDRESS", "user_action": "PAY_NOW",
                            "return_url": "http://localhost:8000/pay/payment-succeeded",
                            "cancel_url": "http://localhost:8000/pay/payment-cancelled"
                        }
                    }
                }
            }
        ]
    })

    response = requests.post(
        "https://api-m.sandbox.paypal.com/v2/checkout/orders",
        headers=headers, data=data
    )

    return response


def get_token():
    headers = {
        "Accept-Language": "en_US",
        "Content-Type": "application/json"
    }
    response = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        headers=headers,
        auth=(settings.CLIENT_ID, settings.APP_SECRET),
        data={'grant_type': 'client_credentials'}
    )
    return response.json()["access_token"]


def capture_fund_for_order(token, order_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    data = json.dumps({
        "amount": {
            "currency_code": "USD",
            "value": "110.00"
        },
        "description": "Boomsserang"
    })

    print(data)
    response = requests.post(
        f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture",
        headers=headers,
        data=data
    )
    print(response.__dict__)
    return response.json()
