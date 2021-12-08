from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from video_classes.models import VideoClass


class TestVideoClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user', is_staff=True)

    def test_create_user_notes(self):
        video_class = VideoClass.objects.create(
            author=self.user,
            title="test_video",
            video_path='/thisisATestpath/',
            description="quick description to show on browse for content card page",
            premium_content=False,
            draft=False,
            last_update_at=timezone.now()
        )
        video_class.save()
        video_classes_list = VideoClass.objects.all()
        for video_class in video_classes_list:
            self.assertEqual('test_video', video_class.title)
            self.assertEqual(self.user, video_class.author)
            self.assertEqual(video_class.video_path, '/thisisATestpath/')
            self.assertEqual(video_class.description, 'quick description to show on browse for content card page')
