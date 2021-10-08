from django.test import TestCase


class TestPersonalSpaceViews(TestCase):

    def test_get_profile_page(self):
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
