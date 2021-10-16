from django.contrib.auth.models import User
from personal_space.models import UserDetail, UserBookmark
from django.test import TestCase


class TestUserDetails(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user', is_staff=True)

        self.user_details = UserDetail(user=self.user,
                                        bio="Testing user Bio")
        self.user_details.save()

        # Creating Bookmarking
        self.bookmark = UserBookmark.objects.create(user=self.user, content_title='content_title',
                                                     content_path='articles/8/')
        self.bookmark.save()

    def test_create_user_details(self):
        user_info = UserDetail.objects.get(user=self.user)
        self.assertEqual(user_info.user, self.user)
        self.assertIsNotNone(user_info.bio)

    def test_create_user_bookmarks(self):
        user_bookmarks = UserBookmark.objects.all()
        for bookmark in user_bookmarks:
            self.assertEqual('content_title', bookmark.content_title)
            self.assertEqual(self.user, bookmark.user)


