import logging

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from products.models import UserSubscription

logger = logging.getLogger(__name__)


def fulfill_subscription_order(session):
    if session['status'] == 'complete' and session['mode'] == 'subscription':
        user_subscription = UserSubscription.objects.get(
            user=get_object_or_404(User, pk=session['client_reference_id']))
        if user_subscription:
            user_subscription.subscription = session['subscription']
            user_subscription.stripe_customer_id = session['customer']
            user_subscription.subscription_active = True
            user_subscription.save()
    # TODO Send receipt to customer by email


def send_invoice_by_email(user_email, invoice_details):
    pass
    # TODO Enable send email feature
    # send_mail(
    #     'Invoice Details',
    #     'Here is the message.',
    #     'ddppessoa@gmail.com',
    #     [user_email],
    #     fail_silently=False,
    # )


def cancel_user_subscription(stripe_customer_id):
    if stripe_customer_id:
        user_subscription = UserSubscription.objects.get(stripe_customer_id=stripe_customer_id)
        if user_subscription:
            user_subscription.subscription_active = False
            user_subscription.save()
        # so user can access his customer_portal for a invoice history
        # TODO Send details cancellation email
        # https://docs.djangoproject.com/en/3.2/topics/email/
        else:
            logging.warning(
                f'User subscription not found for user {user_subscription.user}, '
                f'could not cancel subscription.')
    # TODO Review this to make sure user does not keep active subscription after cancellation is processed by stripe.


def get_user_subscription(user):
    """
    Queries User subscription, if returning premium customer returns a user Stripe customer id.
    :param user:
    :return: stripe_customer_id or None
    """
    user_subscription = UserSubscription.objects.get(user=user)
    if user_subscription:
        stripe_customer_id = user_subscription.stripe_customer_id
    else:
        UserSubscription.objects.create(user=user)
        stripe_customer_id = None
    return stripe_customer_id
