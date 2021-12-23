# Create your views here.
import logging

import stripe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from TheLearningHub.settings import STRIPE_API_KEY, SITE_DOMAIN, STRIPE_ENDPOINT_SECRET
from products.forms import StripeSubscriptionForm
from products.models import Product, UserSubscription
from src.integrations.stripe import fulfill_subscription_order, cancel_user_subscription, get_user_subscription

stripe.api_key = STRIPE_API_KEY
endpoint_secret = STRIPE_ENDPOINT_SECRET

logger = logging.getLogger(__name__)


@login_required()
def create_checkout_session(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        checkout_session = stripe.checkout.Session.create(
            client_reference_id=request.user.id,
            customer=get_user_subscription(request.user),
            line_items=[
                {
                    # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
                    'price': f'{product.stripe_product_id}',
                    'quantity': 1,
                },
            ],
            payment_method_types=['card'],
            mode=f'{product.stripe_product_mode}',
            success_url=f'{SITE_DOMAIN}/products/success',
            cancel_url=f'{SITE_DOMAIN}/products/cancel',
        )
        return redirect(checkout_session.url, code=303)


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    session = event['data']['object']
    if event['type'] == 'checkout.session.completed':
        fulfill_subscription_order(session)

    elif event['type'] == 'customer.subscription.deleted':
        cancel_user_subscription(session['customer'])
    else:
        logging.warning('Unhandled event type {}'.format(event['type']))

    return HttpResponse(status=200)


def manage_subscriptions_portal(request):
    user_subscription = UserSubscription.objects.get(user=request.user)
    session = stripe.billing_portal.Session.create(
        customer=user_subscription.stripe_customer_id,
        return_url=SITE_DOMAIN,
    )

    # redirect to the URL for the customer_portal session
    return redirect(session.url, code=303)


def manage_stripe_subscriptions(request):
    subscriptions = Product.objects.filter(stripe_product_mode='subscription')
    if request.method == 'POST':
        form = StripeSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Created.')
            return render(request, 'stripe_subscription_form.html', {
                'form': form,
                'subscriptions': subscriptions
            })
        else:
            messages.error(request,
                           'Failed to create Subscription. Please try again!')
    else:
        form = StripeSubscriptionForm()
    return render(request, 'stripe_subscription_form.html', {
        'form': form,
        'subscriptions': subscriptions
    })


@login_required(redirect_field_name='home')
def delete_stripe_subscription(request, subscription_id):
    """ Deletes Stripe Subscription """
    content = get_object_or_404(Product, pk=subscription_id)
    content.delete()
    messages.success(request, 'Subscription deleted.')
    return redirect('manage_stripe_subscriptions')


def subscriptions(request):
    subscriptions = Product.objects.filter(stripe_product_mode='subscription')
    user_subscription = UserSubscription.objects.filter(user=request.user).first() or None
    context = {
        'subscriptions': subscriptions,
        'user_subscription': user_subscription
    }
    return render(request, 'subscriptions.html', context)
