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
        # Content Manager
        content_manager = User.objects.create_user('Manager', 'doe@test.com', 'manager123', is_staff=True)
        content_manager.save()
        # Production of mode subscription
        self.test_subscription_product = Product.objects.create(
            name='Premium Plan',
            price=199,
            stripe_product_id='random_string_with_number_and_letters',
            stripe_product_mode='subscription'
        )
        self.test_subscription_product.save()

        test_user_subscription = UserSubscription.objects.create(
            subscription='Stripe_random_id',
            user=test_customer_user
        )
        test_user_subscription.save()

    def test_delete_stripe_subscription(self):
        subscription = Product.objects.create(name='premium test', stripe_product_id='random_id', price='199',
                                              stripe_product_mode='subscription')
        subscription.save()
        self.client.login(username='Manager', password='manager123')
        response = self.client.post(f'/products/delete_stripe_subscription/{subscription.id}')
        self.assertEqual(response.status_code, 301)

    def test_signup_subscription_page(self):
        self.client.login(username='Manager', password='manager123')
        response = self.client.get(f'/products/subscriptions')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['subscriptions'])
        self.assertTemplateUsed(response, 'subscriptions.html')
        self.assertEqual(response.context['subscriptions'][0].name, self.test_subscription_product.name)
