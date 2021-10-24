from django.contrib.auth.models import User
from django.test import TestCase

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
        response = self.client.get(f'/video_class/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('new_video_class.html')

    def test_get_video_class_page(self):
        self.video_class.save()
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
