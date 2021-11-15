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

    def test_pricing_view_as_anonymous(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pricing.html')
        self.assertEqual(response.context['subscriptions'][0].name, 'Premium Plan')

    def test_pricing_view_with_subscription(self):
        self.client.login(username='visitor', password='visitordoe123')
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pricing.html')
        self.assertEqual(response.context['subscriptions'][0].name, 'Premium Plan')
        self.assertEqual(response.context['user_subscription'].subscription, 'Stripe_random_id')
        self.assertEqual(response.context['user_subscription'].user.username, 'visitor')
