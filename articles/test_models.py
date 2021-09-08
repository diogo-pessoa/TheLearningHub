from django.conf import settings
from django.test import TestCase
from .models import Article


class TestArticlesModels(TestCase):

    def test_article_save_as_draft(self):
        pass
        # user = self.client.cre(username='Adam', password='password')
        #
        # article = Article.objects.create(title='New Article', author=user.id)
        # self.assertTrue(article.draft)
