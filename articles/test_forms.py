from django.test import TestCase

from .forms import ArticlesForm


class TestArticlesForms(TestCase):

    def test_title_is_required(self):
        form = ArticlesForm({'title': ''})
        self.assertFalse(form.is_valid())

    def test_form_has_fills_author_created_date(self):
        form = ArticlesForm({
            'title': 'My test article',
            'description': 'brief description of my article',
            'restricted_access': True,
            'draft': True,
        }, "test_user")
        self.assertTrue(form.is_valid())
