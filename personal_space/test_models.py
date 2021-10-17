from django.contrib.auth.models import User
from django.test import TestCase

from personal_space.models import UserProfile, UserBookmark, UserNote


class TestUserDetails(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user', is_staff=True)

    def test_create_user_details(self):
        self.user_details = UserProfile(user=self.user,
                                        bio="Testing user Bio")
        self.user_details.save()
        user_info = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_info.user, self.user)
        self.assertIsNotNone(user_info.bio)

    def test_create_user_bookmarks(self):
        bookmark = UserBookmark.objects.create(user=self.user,
                                               content_title='content_title',
                                               content_path='articles/8/')
        bookmark.save()
        user_bookmarks = UserBookmark.objects.all()
        for bookmark in user_bookmarks:
            self.assertEqual('content_title', bookmark.content_title)
            self.assertEqual(self.user, bookmark.user)

    def test_create_user_notes(self):
        user_note = UserNote.objects.create(user=self.user,
                                            note_content='content_title',
                                            content_path='/articles/8/')
        user_note.save()
        user_notes = UserNote.objects.all()
        for note in user_notes:
            self.assertEqual('content_title', note.note_content)
            self.assertEqual(self.user, note.user)
            self.assertEqual(note.content_path, '/articles/8/')
