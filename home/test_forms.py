from django.test import TestCase

from .forms import PageForm, UploadFileForm
from .models import Page


class TestArticlesForms(TestCase):

    def test_form_is_valid_and_default_content(self):
        form = PageForm({'content': 'testing content'})
        self.assertTrue(form.is_valid())
        if form.is_valid():
            form.save()
        pages = Page.objects.all()
        for page in pages:
            self.assertIsNotNone(page.title)
            self.assertEqual('testing content', page.content)

    def test_file_upload_form(self):
        file = open('test_file.txt', 'a').close()

        form = UploadFileForm({'content': 'testing content',
                               'file': file,
                               'page_source': '/articles'})

        if form.is_valid():
            form.save()
        pages = Page.objects.all()
        for page in pages:
            self.assertIsNotNone(page.title)
            self.assertEqual('testing content', page.content)
