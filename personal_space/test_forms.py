from django.contrib.auth.models import User
from django.test import TestCase

from .forms import PersonalDetailsForm
from .models import UserProfile


class TestArticlesForms(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create(username='test_user', password='test_pass', is_staff=True)
        self.user.save()

    def test_update_info_form_is_valid(self):
        form = PersonalDetailsForm({
                                    'first_name': 'John',
                                    'last_name': 'Doe',
                                    'bio': 'listing a user bio'
                                    })
        self.assertTrue(form.is_valid())
        if form.is_valid():
            form.save()
        user_info = UserProfile.objects.all()
        for info in user_info:
            self.assertIsNotNone(info.bio)
            self.assertEqual(info.last_name, 'Doe')
