from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_browse_articles(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
