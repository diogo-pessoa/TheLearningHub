# Create your views here.
import json

import stripe
from django.shortcuts import redirect, render, get_object_or_404
from jsonify.convert import jsonify

from TheLearningHub.settings import STRIPE_API_KEY, SITE_DOMAIN
from products.models import Product

stripe.api_key = STRIPE_API_KEY


def create_checkout_session(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
                    'price': f'{product.stripe_product_id}',
                    'quantity': 1,
                },
            ],
            payment_method_types=['card'],
            mode=f'{product.stripe_product_mode}',
            success_url=f'{SITE_DOMAIN}/success',
            cancel_url=f'{SITE_DOMAIN}/cancel',
        )
        return redirect(checkout_session.url, code=303)


def pricing(request):
    subscriptions = Product.objects.filter(stripe_product_mode='subscription')
    print(subscriptions)
    context = {
        'subscriptions': subscriptions
    }
    return render(request, 'pricing.html', context)


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def create_subscription(request, product_id):

    product = Product.objects.get(id=product_id)
    # Simulating authenticated user. Lookup the logged in user in your
    # database, and set customer_id to the Stripe Customer ID of that user.
    customer_id = request.user

    # Extract the price ID from environment variables given the name
    # of the price passed from the front end.
    #
    # `price_id` is the an ID of a Price object on your account.
    # This was populated using Price's `lookup_key` in the /config endpoint
    price_id = product.stripe_product_id

    try:
        # Create the subscription. Note we're using
        # expand here so that the API will return the Subscription's related
        # latest invoice, and that latest invoice's payment_intent
        # so we can collect payment information and confirm the payment on the front end.

        # Create the subscription
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[{
                'price': price_id,
            }],
            payment_behavior='default_incomplete',
            expand=['latest_invoice.payment_intent'],
        )
        return jsonify(subscriptionId=subscription.id,
                       clientSecret=subscription.latest_invoice.payment_intent.client_secret)

    except Exception as e:
        return jsonify(error={'message': e.user_message}), 400
