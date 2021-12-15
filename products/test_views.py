from django.contrib.auth.models import User
from django.test import TestCase

from products.models import Product, UserSubscription


class TestProductViews(TestCase):

    def setUp(self) -> None:
        """
            Creates a user, a subscription Product and a UserSubscription
        """
        # User
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        # Production of mode subscription
        test_subscription_product = Product.objects.create(
            name='Premium Plan',
            price=199,
            stripe_product_id='random_string_with_number_and_letters',
            stripe_product_mode='subscription'
        )
        test_subscription_product.save()

        test_user_subscription = UserSubscription.objects.create(
            subscription='Stripe_random_id',
            user=test_customer_user
        )
        test_user_subscription.save()