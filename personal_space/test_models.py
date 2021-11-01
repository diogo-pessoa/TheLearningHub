from django.contrib.auth.models import User
from django.test import TestCase

from personal_space.models import UserProfile, UserBookmarkArticle, UserNoteFromVideoClass
from video_classes.models import VideoClass


class TestUserDetails(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user', is_staff=True)

    def test_create_user_details(self):
        self.user_details = UserProfile(user=self.user,
                                        bio="Testing user Bio",
                                        first_name='test',
                                        last_name='user')
        self.user_details.save()
        user_info = UserProfile.objects.get(user=self.user)
        self.assertIsNotNone(user_info.bio)
        self.assertEquals(user_info.first_name, self.user_details.first_name)

    def test_create_user_bookmarks(self):
        bookmark = UserBookmarkArticle.objects.create(user=self.user,
                                                      content_title='content_title',
                                                      content_path='articles/8/')
        bookmark.save()
        user_bookmarks = UserBookmarkArticle.objects.all()
        for bookmark in user_bookmarks:
            self.assertEqual('content_title', bookmark.content_title)
            self.assertEqual(self.user, bookmark.user)

    def test_create_user_notes_from_video_class(self):
        video_class = VideoClass.objects.create(title='test_class')
        video_class.save()
        user_note = UserNoteFromVideoClass.objects.create(user=self.user,
                                                          video_class=video_class,
                                                          body='About Python')
        user_note.save()
        user_notes = UserNoteFromVideoClass.objects.all()
        for note in user_notes:
            self.assertEqual('About Python', note.body)
            self.assertEqual(self.user, note.user)
            self.assertIsInstance(note.video_class, VideoClass)
