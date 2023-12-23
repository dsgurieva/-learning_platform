import stripe
from django.config import settings
import requests
from django.urls import reverse


def create_payment(amount):
    stripe.api_key = settings.STRIPE_API_KEY
    response = stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    return response


def create_session_payment(amount: int, name_product: str):
    stripe.api_key = "sk_test_51OQSKmA019y72R72lU8NPNVqX6oUooHlfeawh7oxUxbBlmY6sRZX40mQ8mKSY1OdLYuXyKTGCncNg9Ao08l3g8o4003Tib0dzI"
    product = stripe.Product.create(name=name_product)
    price = stripe.Price.create(
        unit_amount=amount,
        currency="usd",
        recurring={"interval": "month"},
        product=product['id'],
    )
    response = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price['id'],
                "quantity": 1,
            },
        ],
        mode="subscription",
    )
    return response
