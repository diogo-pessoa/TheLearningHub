from django.contrib.auth.models import User
from django.test import TestCase


class TestProductViews(TestCase):

    def setUp(self) -> None:
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        self.visitor = User.objects.get(username='visitor')

    def test_pricing_view_as_anonymous(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pricing.html')
