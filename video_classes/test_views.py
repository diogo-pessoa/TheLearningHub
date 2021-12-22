from django.contrib.auth.models import User
from django.test import TestCase

from personal_space.models import UserBookmarkVideoClass
from video_classes.models import VideoClass


class TestVideosClassViews(TestCase):

    def setUp(self) -> None:
        test_super_user = User.objects.create_user('john', 'doe@test.com', 'johndoe123', is_staff=True)
        test_customer_user = User.objects.create_user('visitor', 'doe@test.com', 'visitordoe123')
        test_customer_user.save()
        test_super_user.save()
        self.user = User.objects.get(username='john')
        self.visitor = User.objects.get(username='visitor')

        self.video_class = VideoClass.objects.create(title='Test_video',
                                                     author=self.user,
                                                     video_path='/videos/this_is_fun_media')

    def test_content_manager_can_open_video_class_form_page(self):
        self.client.login(username='john', password='johndoe123')
        response = self.client.get(f'/video_class/create_video_class')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('new_video_class.html')

    def test_get_video_class_page(self):
        self.client.login(username='john', password='johndoe123')
        video_class = VideoClass.objects.all()[0]
        response = self.client.get(f'/video_class/{video_class.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('video_class.html')
        self.assertEqual(response.context['video_class'].title, self.video_class.title)
        self.assertIsInstance(response.context['video_class'], VideoClass)

    def test_fail_delete_video_class_unless_logged_in(self):
        self.video_class.save()
        video_class = VideoClass.objects.all()[0]
        response = self.client.get(f'/video_class/delete/{video_class.id}/')
        self.assertEqual(response.status_code, 302)

    def test_fail_delete_video_class_if_visitor(self):
        self.video_class.save()
        self.client.login(username='visitor', password='visitordoe123')
        video_class = VideoClass.objects.all()[0]
        response = self.client.get(f'/video_class/delete/{video_class.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Sorry, you are not allowed to remove content')

    def test_as_staff_delete_video_class(self):
        self.video_class.save()
        self.client.login(username='john', password='johndoe123')
        video_class = VideoClass.objects.all()[0]
        response = self.client.get(f'/video_class/delete/{video_class.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Video Class Deleted successfully!')

    # Bookmark Video:

    def test_bookmark_video_class(self):
        bookmark = UserBookmarkVideoClass(user=self.user, video_class=self.video_class)
        self.video_class.save()  # Saving video_class to make sure it exists in test DB.
        self.client.login(username='john', password='johndoe123')
        response = self.client.post(f'/personal_space/add_video_bookmark/', {'video_class_id': self.video_class.id})
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Class added to your favorites!')
        self.assertRedirects(response, f'/video_class/{self.video_class.id}/')
        bookmark = UserBookmarkVideoClass.objects.all()
        self.assertEqual(bookmark[0].video_class.id, self.video_class.id)

    def test_remove_bookmark(self):
        bookmark = UserBookmarkVideoClass(user=self.user, video_class=self.video_class)
        bookmark.save()
        self.client.login(username='john', password='johndoe123')
        response = self.client.post(f'/personal_space/remove_video_bookmark/{bookmark.id}/')
        self.assertEqual(response.status_code, 302)
        self.assertRaisesMessage(response, 'Removed from your bookmarks')
        self.assertRedirects(response, f'/video_class/{self.video_class.id}/')
        bookmark = UserBookmarkVideoClass.objects.all()
        self.assertQuerysetEqual(bookmark, [])
