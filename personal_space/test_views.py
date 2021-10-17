from django.contrib.auth.models import User
from django.test import TestCase

from personal_space.models import UserProfile, UserBookmark, UserNote


class TestPersonalSpaceViews(TestCase):

    # TODO Review possible clean-up of setUp duplication
    def setUp(self) -> None:
        test_super_user = User.objects.create_user('john', 'doe@test.com', 'johndoe123', first_name="John",
                                                   last_name="Doe", is_staff=True)
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        test_super_user.save()
        self.user = User.objects.get(username='john')
        self.visitor = User.objects.get(username='visitor')

    def test_profile_page_redirects_for_anonymous_users(self):
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 302)

    def test_get_profile_page_user_bio_information(self):
        """ Test User Profile page is able to load user Bio and are available on view """
        user_profile = UserProfile.objects.create(user=self.user, bio="This is John's Bio")
        user_profile.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_profile_info'][0], UserProfile)
        self.assertEqual(response.context['user_profile_info'][0].bio, user_profile.bio)
        self.assertEqual(response.context['user_profile_info'][0].user, self.user)

    def test_get_user_profile_bookmarks(self):
        """ Test User Profile page is able to load user Bookmarks and are available on view """
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

    def test_get_user_profile_information(self):
        """ Test User Profile information in personal page """

        self.client.login(username='john', password='johndoe123')
        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_role_information'], User)
        self.assertEqual(response.context['user_role_information'].first_name, self.user.first_name)
        self.assertEqual(response.context['user_role_information'].last_name, self.user.last_name)
        self.assertEqual(response.context['user_role_information'].is_staff, self.user.is_staff)

    def test_get_user_notes(self):
        """ Test a user accessing his notes following from the view perspective, as a site member.
            - User saves a note
            - Navigates to profile page
            - User will see has access to what is in the view context
            note this is an list as a user can have one or more notes.
        """

        self.client.login(username='john', password='johndoe123')

        user_note = UserNote.objects.create(user=self.user,
                                            note_content='content_title',
                                            content_path='/articles/8/',
                                            note_title="this is the a note from the course")
        user_note.save()

        response = self.client.get('/personal_space/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_index.html')
        self.assertIsInstance(response.context['user_notes'][0], UserNote)
        self.assertEqual(response.context['user_notes'][0].note_title, user_note.note_title)
        self.assertEqual(response.context['user_notes'][0].content_path, user_note.content_path)
        self.assertEqual(response.context['user_notes'][0].note_title, user_note.note_title)
