from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from products.models import UserSubscription


def fulfill_subscription_order(request, session):
    print(session)
    if session['status'] == 'complete' and session['mode'] == 'subscription':
        UserSubscription.objects.create(
            subscription=session['subscription'],
            order=session,
            user=get_object_or_404(User, pk=session['client_reference_id']))
    # TODO Send receipt to customer by email


def send_invoice_by_email(user_email, invoice_details):
    pass


def get_stripe_subscription_information(stripe_subscription_id):
    pass

def cancel_user_subscription(stripe_subscription_id):
    pass