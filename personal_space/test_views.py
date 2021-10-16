import json

from django.contrib.auth.models import User
from django.test import TestCase

from personal_space.models import UserDetail, UserBookmark


class TestPersonalSpaceViews(TestCase):

    # TODO Review possible clean-up of setUp duplication
    def setUp(self) -> None:
        test_super_user = User.objects.create_user('john', 'doe@test.com', 'johndoe123', is_staff=True)
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        test_super_user.save()
        self.user = User.objects.get(username='john')
        self.visitor = User.objects.get(username='visitor')

    def test_profile_page_redirects_for_anonymous_users(self):
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 302)

    def test_get_profile_page_user_bio_information(self):
        ''' Test User Profile page is able to load user Bio and are available on view'''
        user_details = UserDetail.objects.create(user=self.user, bio="This is John's Bio")
        user_details.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_details'][0], UserDetail)
        self.assertEqual(response.context['user_details'][0].bio, user_details.bio)
        self.assertEqual(response.context['user_details'][0].user, self.user)

    def test_get_user_profile_bookmarks(self):
        ''' Test User Profile page is able to load user Bookmarks and are available on view'''
        user_bookmarks = UserBookmark.objects.create(user=self.user,
                                                     content_path="/articles/8/",
                                                     content_title="nice Article")
        user_bookmarks.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_bookmarks'][0], UserBookmark)
        self.assertEqual(response.context['user_bookmarks'][0].content_title, user_bookmarks.content_title)
        self.assertEqual(response.context['user_bookmarks'][0].content_path, user_bookmarks.content_path)
        self.assertEqual(response.context['user_bookmarks'][0].user, self.user)
