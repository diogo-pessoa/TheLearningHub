from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .forms import ArticlesForm
from .models import Article


class TestArticlesForms(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='test_user', is_staff=True)

    def test_form_is_valid(self):
        form = ArticlesForm({'title': 'My test article',
                             'description': 'brief description of my article',
                             'author': self.user
                             })
        self.assertTrue(form.is_valid())
        self.assertTrue(form.draft)

    def test_article_has_all_fields(self):
        """ Test Form is valid and article is saved with correct fields"""
        form = ArticlesForm({'title': 'My test article',
                             'description': 'brief description of my article',
                             'author': self.user,
                             'content': '<p>test</p>'
                             })
        if form.is_valid():
            form.save()
        articles = Article.objects.all()
        for article in articles:
            self.assertFalse(article.draft)
            self.assertFalse(article.restricted_access)
            self.assertIsNotNone(article.content)
            self.assertEqual(self.user, article.author)







