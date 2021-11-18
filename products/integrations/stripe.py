import logging

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from products.models import UserSubscription

logger = logging.getLogger(__name__)


def fulfill_subscription_order(request, session):
    print(session)
    if session['status'] == 'complete' and session['mode'] == 'subscription':
        UserSubscription.objects.create(
            subscription=session['subscription'],
            order=session,
            user=get_object_or_404(User, pk=session['client_reference_id']),
            stripe_customer_id=session['customer'])
    # TODO Send receipt to customer by email


def send_invoice_by_email(user_email, invoice_details):
    pass


def cancel_user_subscription(stripe_customer_id):
    if stripe_customer_id:
        user_subscription = UserSubscription.objects.get(stripe_customer_id=stripe_customer_id)
        if user_subscription:
            user_subscription.delete()
            # TODO replace the `delete` with a toggle `deactived` to keep application user relation with Stripe customer_id
            # so user can access his customer_portal for a invoice history
            # TODO Send details cancellation email
        else:
            logging.warning(
                f'User subscription not found for user {user_subscription.user}, '
                f'could not cancel subscription.')
    # TODO Review this to make sure user does not keep active subscription after cancellation is processed by stripe.
