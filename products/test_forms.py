from django.test import TestCase

from .forms import StripeSubscriptionForm
from .models import Product


class TestStripeSubscriptionForm(TestCase):

    def test_create_stripe_subscription_form(self):
        form = StripeSubscriptionForm({'name': 'Premium Plan',
                                       'stripe_product_id': 'Random product_id',
                                       'price': 199,
                                       'stripe_product_mode': 'subscription'
                                       })
        if form.is_valid():
            form.save()
        subscriptions = Product.objects.all()
        for subscription in subscriptions:
            self.assertEqual(subscription.name, 'Premium Plan')
            self.assertEqual(subscription.stripe_product_id, 'Random product_id')
            self.assertIsNotNone(subscription.price)
            self.assertEqual('subscription', subscription.stripe_product_mode)
