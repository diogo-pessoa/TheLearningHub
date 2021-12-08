from django.test import TestCase

from articles.models import Article
from home.models import Page
from video_classes.models import VideoClass


class TestHomeViews(TestCase):

    def test_main_page_unified_view(self):
        about = Page.objects.create(title='about', content='<p>Valid content</p>')
        about.save()
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main_pages_template.html')
        self.assertEqual(about.content, response.context['page'].content)

    def test_search_returns_video_classes_and_articles(self):
        article = Article.objects.create(title='test')
        article.save()
        video_class = VideoClass.objects.create(title='test')
        video_class.save()
        response = self.client.get('/search/?search_query=test')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['search_result'])

    def test_search_content_no_content(self):
        article = Article.objects.create(title='test')
        article.save()
        response = self.client.get(f'/search/?search_query=')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, "You didn't enter any search criteria!")

    def test_search_returns_article(self):
        article = Article.objects.create(title='test', description='testing search')
        article.save()
        response = self.client.get(f'/search/?search_query=test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testing search', str(response.content))

    def test_get_browse_articles(self):
        response = self.client.get('/learning_area/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
