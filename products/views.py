# Create your views here.

import stripe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from TheLearningHub.settings import STRIPE_API_KEY, SITE_DOMAIN, STRIPE_ENDPOINT_SECRET
from products.models import Product

stripe.api_key = STRIPE_API_KEY
endpoint_secret = STRIPE_ENDPOINT_SECRET

@login_required()
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
            success_url=f'{SITE_DOMAIN}/products/success',
            cancel_url=f'{SITE_DOMAIN}/products/cancel',
        )
        return redirect(checkout_session.url, code=303)


def pricing(request):
    subscriptions = Product.objects.filter(stripe_product_mode='subscription')
    context = {
        'subscriptions': subscriptions
    }
    return render(request, 'pricing.html', context)


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')

@csrf_exempt
def my_webhook_view(request):
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

  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    # Fulfill the purchase...
    fulfill_order(session)

  # Passed signature verification
  return HttpResponse(status=200)

def fulfill_order(session):
  # TODO: fill me in
  # TODO Add a copy on application DB
  # TODO Send receipt to customer by email
  # TODO Set user as Premium subscriber
  print("Fulfilling order")