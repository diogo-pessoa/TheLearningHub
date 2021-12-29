import logging

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from products.models import UserSubscription

logger = logging.getLogger(__name__)


def fulfill_subscription_order(session):
    if session['status'] == 'complete' and session['mode'] == 'subscription':
        user_subscription = UserSubscription.objects.filter(
            user=get_object_or_404(User, pk=session['client_reference_id'])).first()
        if user_subscription:
            user_subscription.subscription = session['subscription']
            user_subscription.stripe_customer_id = session['customer']
            user_subscription.subscription_active = True
            user_subscription.save()


def cancel_user_subscription(stripe_customer_id):
    if stripe_customer_id:
        user_subscription = UserSubscription.objects.filter(stripe_customer_id=stripe_customer_id).first()
        if user_subscription:
            user_subscription.subscription_active = False
            user_subscription.save()
        else:
            logging.warning(
                f'User subscription not found for user {user_subscription.user}, '
                f'could not cancel subscription.')


def get_user_subscription(user):
    """
    Queries User subscription, if returning premium customer returns a user Stripe customer id.
    :param user:
    :return: stripe_customer_id or None
    """
    user_subscription = UserSubscription.objects.filter(user=user).first() or None
    if user_subscription:
        stripe_customer_id = user_subscription.stripe_customer_id
    else:
        UserSubscription.objects.create(user=user)
        stripe_customer_id = None
    return stripe_customer_id
