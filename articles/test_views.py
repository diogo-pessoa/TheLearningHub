from django.test import TestCase

from articles.models import Article, Author


class TestArticlesViews(TestCase):

    def setUp(self) -> None:
        self.user = Author.objects.create(username='test_user')

    def test_get_browse_articles(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles.html')
        #  TODO link to article works

    def test_article(self):
        article = Article.objects.create(title='test', author=self.user)
        response = self.client.get(f'/articles/{article.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article.html')

    def test_delete_article_redirects_non_super_user(self):
        article = Article.objects.create(title='test', author=self.user)
        response = self.client.get(f'/articles/delete/{article.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Sorry, you are not allowed to remove an article')
