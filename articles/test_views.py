from django.contrib.auth.models import User
from django.test import TestCase

from articles.models import Article


class TestArticlesViews(TestCase):

    def test_get_browse_articles(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles.html')
        #  TODO link to article works

    def test_article(self):
        user = User.objects.create(username='test_user')
        article = Article.objects.create(title='test', author=user)
        response = self.client.get(f'/articles/{article.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article.html')
