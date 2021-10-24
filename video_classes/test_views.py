from django.contrib.auth.models import User
from django.test import TestCase


class TestVideosClassViews(TestCase):

    def setUp(self) -> None:
        test_super_user = User.objects.create_user('john', 'doe@test.com', 'johndoe123', is_staff=True)
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        test_super_user.save()
        self.user = User.objects.get(username='john')
        self.visitor = User.objects.get(username='visitor')

    def test_content_manager_creates_video_class(self):
        self.client.login(username='john', password='johndoe123')
        response = self.client.get(f'/video_class/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('new_video_class.html')
