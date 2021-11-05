from django.contrib.auth.models import User
from django.test import TestCase

from articles.models import Article


class TestArticlesViews(TestCase):

    def setUp(self) -> None:
        test_super_user = User.objects.create_user('john', 'doe@test.com', 'johndoe123', is_staff=True)
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        test_super_user.save()
        self.user = User.objects.get(username='john')
        self.visitor = User.objects.get(username='visitor')

    def test_get_browse_articles(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles.html')
        #  TODO link to article works

    def test_article_renders_for_anonymous_user(self):
        article = Article.objects.create(title='test', author=self.user)
        response = self.client.get(f'/articles/{article.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article.html')

    def test_not_allowed_delete_if_not_staff(self):
        """ Login as visitor and fails to delete article"""
        article = Article.objects.create(title='test', author=self.user)
        article.save()
        self.client.login(username='visitor', password='visitordoe123')
        response = self.client.get(f'/articles/delete/{article.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Sorry, you are not allowed to remove an article')
        self.assertIsNotNone(Article.objects.get(title=article.title))

    def test_delete_article_if_is_staff(self):
        """ Login as superuser to delete article"""
        article = Article.objects.create(title='test2', author=self.user)
        article.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.get(f'/articles/delete/{article.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Article removed Successfully!')
        self.assertEqual(len(Article.objects.all()), 0)

    def test_write_article_as_visitor_redirects(self):
        self.client.login(username='visitor', password='visitordoe123')
        response = self.client.get(f'/articles/write_article')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Sorry, only content Managers can create Articles.')

    def test_write_article_as_staff(self):
        self.client.login(username='john', password='johndoe123')
        response = self.client.get(f'/articles/write_article')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'write_article.html')

    def test_search_content_no_content(self):
        article = Article.objects.create(title='test', author=self.user)
        article.save()
        response = self.client.get(f'/articles/?search_query=')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, "You didn't enter any search criteria!")

    def test_search_returns_article(self):
        article = Article.objects.create(title='test', description='testing search', author=self.user)
        article.save()
        response = self.client.get(f'/articles/?search_query=test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testing search', str(response.content))
