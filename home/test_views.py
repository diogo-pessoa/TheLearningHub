from django.test import TestCase

from home.models import Page


class TestHomeViews(TestCase):

    def test_main_pages_view(self):
        about = Page.objects.create(title='about', content='<p>Valid content</p>')
        about.save()
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_pages_template.html')
        self.assertEqual(about.content, response.context['page'].content)
