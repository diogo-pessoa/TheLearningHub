from django.test import TestCase


class TestArticlesViews(TestCase):

    def test_get_browse_articles(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles.html')

