from django.contrib.auth.models import User
from django.test import TestCase

from articles.models import Article
from home.learning_area import load_role_based_content_list
from home.models import Page
from products.models import UserSubscription
from video_classes.models import VideoClass


class TestHomeViews(TestCase):

    def setUp(self) -> None:
        self.content_manager = User.objects.create_user('Manager', 'doe@test.com', 'manager123', is_staff=True)
        self.content_manager.save()

        self.visitor = User.objects.create_user('visitor', 'doe@test.com', 'manager123', is_staff=False)
        self.visitor.save()

        self.premium_user = User.objects.create_user('premium_user', 'doe@test.com', 'manager123', is_staff=False)
        self.premium_user.save()

        self.article_in_draft = Article.objects.create(title='draft_article', author=self.content_manager, draft=True,
                                                       premium_content=False)
        self.article_in_free = Article.objects.create(title='free_article', author=self.content_manager, draft=False,
                                                      premium_content=False)
        self.article_in_Premium = Article.objects.create(title='premium_article', author=self.content_manager,
                                                         draft=False,
                                                         premium_content=True)

        self.video_in_draft = VideoClass.objects.create(title='free_video_draft', author=self.content_manager,
                                                        draft=True,
                                                        premium_content=False)
        self.free_video_published = VideoClass.objects.create(title='free_video', author=self.content_manager,
                                                              draft=False,
                                                              premium_content=False)

        self.video_premium = VideoClass.objects.create(title='premium_video', author=self.content_manager,
                                                       draft=False,
                                                       premium_content=True)

        self.articles_list = [self.article_in_draft, self.article_in_free, self.article_in_Premium]

        self.videos_list = [self.video_in_draft, self.free_video_published, self.video_premium]

        self.content_list = [self.article_in_draft, self.free_video_published, self.video_premium]

        self.user_subscription = UserSubscription.objects.create(user=self.premium_user, subscription_active=True)
        self.user_subscription.save()

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
        article = Article.objects.create(title='test', description='testing search', draft=False)
        article.save()
        response = self.client.get(f'/search/?search_query=test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('testing search', str(response.content))

    def test_get_browse_articles(self):
        response = self.client.get('/learning_area/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')

    def test_get_content_management_area(self):
        page = Page.objects.create(title='title', content='content')
        page.save()
        self.client.login(username='Manager', password='manager123')
        response = self.client.get('/content_management')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'control_panel.html')
        self.assertEqual(response.context['pages'][0].title, page.title)

    def test_load_role_based_content_list_for_staff_show_All_types(self):
        """ Show all content if User is Staff member """

        filtered_list = load_role_based_content_list(self.content_list, False, self.content_manager.is_staff)
        self.assertIn(self.article_in_draft, filtered_list)
        self.assertIn(self.free_video_published, filtered_list)
        self.assertIn(self.video_premium, filtered_list)

    def test_load_role_based_content_list_for_Premium_users_no_drafts(self):
        """ shows Content is Premium, Free and not in Draft for Premium User """

        filtered_list = load_role_based_content_list(self.content_list, subscription_active=True, user_is_staff=False)
        self.assertNotIn(self.article_in_draft, filtered_list)
        self.assertIn(self.free_video_published, filtered_list)
        self.assertIn(self.video_premium, filtered_list)

    def test_load_role_based_content_list_for_registered_users_not_premium(self):
        """ Shows only content that is not premium or draft. """

        filtered_list = load_role_based_content_list(self.content_list, subscription_active=False, user_is_staff=False)
        self.assertNotIn(self.article_in_draft, filtered_list)
        self.assertNotIn(self.video_premium, filtered_list)
        self.assertIn(self.free_video_published, filtered_list)

    def test_load_role_based_articles_list_for_registered_users_not_premium(self):
        """ Shows only content that is not premium or draft. """

        filtered_list = load_role_based_content_list(self.articles_list, subscription_active=False, user_is_staff=False)
        self.assertNotIn(self.article_in_draft, filtered_list)
        self.assertNotIn(self.article_in_Premium, filtered_list)
        self.assertIn(self.article_in_free, filtered_list)

    def test_load_role_based_videos_list_for_registered_users_premium(self):
        """ Shows only content that is not premium or draft. """

        filtered_list = load_role_based_content_list(self.videos_list, subscription_active=True, user_is_staff=False)
        self.assertNotIn(self.video_in_draft, filtered_list)
        self.assertNotIn(self.article_in_draft, filtered_list)
        self.assertIn(self.video_premium, filtered_list)
        self.assertIn(self.free_video_published, filtered_list)

    # Testing Access to querying only articles + Videos returning object, based on user privilege

    def test_get_learning_area_view_loading_user_premium_user_access(self):
        self.client.login(username='premium_user', password='manager123')
        response = self.client.get('/learning_area/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
        self.assertIn(self.video_premium, response.context['search_result'])
        self.assertNotIn(self.article_in_draft, response.context['search_result'])

    def test_get_learning_area_view_loading_user_anonymous_user_access(self):
        response = self.client.get('/learning_area/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
        self.assertIn(self.free_video_published, response.context['search_result'])
        self.assertNotIn(self.article_in_draft, response.context['search_result'])
        self.assertNotIn(self.video_premium, response.context['search_result'])

    def test_get_learning_area_view_loading_user_is_staff(self):
        self.client.login(username=self.content_manager.username, password='manager123')
        response = self.client.get('/learning_area/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
        self.assertIn(self.free_video_published, response.context['search_result'])
        self.assertIn(self.article_in_draft, response.context['search_result'])
        self.assertIn(self.video_in_draft, response.context['search_result'])
        self.assertIn(self.video_premium, response.context['search_result'])

    # Testing Access to querying only articles returning object, based on user privilege

    def test_search_articles_view_loading_user_anonymous_user_access(self):
        response = self.client.get('/search/?search_query=nav_learning_articles')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
        self.assertIn(self.article_in_free, response.context['search_result'])
        self.assertNotIn(self.article_in_draft, response.context['search_result'])
        self.assertNotIn(self.article_in_Premium, response.context['search_result'])
        self.assertNotIn(self.video_premium, response.context['search_result'])

    def test_search_articles_view_loading_user_premium_user_access(self):
        self.client.login(username='premium_user', password='manager123')
        response = self.client.get('/search/?search_query=nav_learning_articles')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
        self.assertIn(self.article_in_Premium, response.context['search_result'])
        self.assertIn(self.article_in_free, response.context['search_result'])
        self.assertNotIn(self.article_in_draft, response.context['search_result'])

    # Testing Access to querying only videos returning object, based on user privilege

    def test_search_video_classes_view_loading_user_anonymous_user_access(self):
        response = self.client.get('/search/?search_query=nav_learning_videos')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
        self.assertIn(self.free_video_published, response.context['search_result'])
        self.assertNotIn(self.video_in_draft, response.context['search_result'])
        self.assertNotIn(self.video_premium, response.context['search_result'])
        self.assertNotIn(self.article_in_Premium, response.context['search_result'])

    def test_search_video_classes_view_loading_user_premium_user_access(self):
        self.client.login(username='premium_user', password='manager123')
        response = self.client.get('/search/?search_query=nav_learning_videos')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_area.html')
        self.assertIn(self.video_premium, response.context['search_result'])
        self.assertIn(self.free_video_published, response.context['search_result'])
        self.assertNotIn(self.video_in_draft, response.context['search_result'])
        self.assertNotIn(self.article_in_free, response.context['search_result'])
