from django.contrib.auth.models import User
from django.test import TestCase

from articles.models import Article
from personal_space.models import UserProfile, UserBookmarkArticle, UserNoteFromVideoClass
from video_classes.models import VideoClass


class TestPersonalSpaceViews(TestCase):

    def setUp(self) -> None:
        test_super_user = User.objects.create_user('john', 'doe@test.com',
                                                   'johndoe123',
                                                   is_staff=True)
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        test_super_user.save()
        self.user = User.objects.get(username='john')
        self.visitor = User.objects.get(username='visitor')
        # Creating Test article
        self.article = Article.objects.create(title="test")
        # Creating a video_class
        self.video_class = VideoClass.objects.create(title="Video_class")

    def test_profile_page_redirects_for_anonymous_users(self):
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 302)

    def test_get_profile_page_user_bio_information(self):
        """ Test User Profile page is able to load user Bio and are available on view """
        user_profile = UserProfile.objects.create(user=self.user, bio="This is John's Bio", first_name='John',
                                                  last_name='Doe')
        user_profile.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_profile_info'][0], UserProfile)
        self.assertEqual(response.context['user_profile_info'][0].user, self.user)
        self.assertEqual(response.context['user_profile_info'][0].bio, user_profile.bio)
        self.assertEqual(response.context['user_profile_info'][0].first_name, user_profile.first_name)
        self.assertEqual(response.context['user_profile_info'][0].last_name, user_profile.last_name)

    def test_get_user_profile_bookmarks(self):
        """ Test User Profile page is able to load user Bookmarks and are available on view """
        user_bookmarks = UserBookmarkArticle.objects.create(user=self.user, article=self.article)
        user_bookmarks.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_bookmarks'][0]['object'], Article)
        self.assertEqual(response.context['user_bookmarks'][0]['object'].title, self.article.title)

    def test_get_user_notes(self):
        self.client.login(username='john', password='johndoe123')
        user_note = UserNoteFromVideoClass.objects.create(user=self.user,
                                                          video_class=self.video_class,
                                                          content="this is the a note from the course")
        user_note.save()
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_notes'][0], UserNoteFromVideoClass)
        self.assertEqual(response.context['user_notes'][0].content, user_note.content)
        self.assertIsInstance(response.context['user_notes'][0].video_class, VideoClass)

    def test_update_user_details_view(self):
        self.client.login(username='john', password='johndoe123')
        response = self.client.get('/personal_space/update_personal_details')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_personal_details.html')

    def test_add_bookmark(self):
        """push a nwe bookmark and query the model to confirm it was created"""
        self.article.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.post(f'/personal_space/add_bookmark/', {'article_id': self.article.id})
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Article added to your favorites!')
        bookmark = UserBookmarkArticle.objects.all()
        self.assertEqual(bookmark[0].article.id, self.article.id)

    def test_remove_bookmark(self):
        bookmark = UserBookmarkArticle(user=self.user, article=self.article)
        bookmark.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.post(f'/personal_space/remove_bookmark/{bookmark.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Removed from your bookmarks')
        bookmark = UserBookmarkArticle.objects.all()
        self.assertQuerysetEqual(bookmark, [])
