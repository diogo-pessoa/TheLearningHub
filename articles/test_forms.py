from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .forms import ArticlesForm
from .models import Article


class TestArticlesForms(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='test_user')

    def test_form_is_valid(self):
        form = ArticlesForm({'title': 'My test article',
                             'description': 'brief description of my article',
                             }, author=self.user)
        self.assertTrue(form.is_valid())

    def test_form_default_values(self):
        form = ArticlesForm({'title': 'My test article',
                             'description': 'brief description of my article',
                             }, author=self.user)
        if form.is_valid():
            form.save()
        article = Article.objects.get(title='My test article')
        self.assertFalse(article.restricted_access)
        self.assertIsNotNone(article.created_at)

