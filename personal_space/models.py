from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articles.models import Article
from video_classes.models import VideoClass


class UserBookmarkArticle(models.Model):
    article = models.ForeignKey(Article, default=None, null=True, on_delete=models.CASCADE)
    content_title = models.CharField(max_length=254)
    content_path = models.CharField(max_length=256, null=False, blank=False)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=256, null=False, blank=False)


class UserProfile(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=800, null=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)


class UserNoteFromVideoClass(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    video_class = models.ForeignKey(VideoClass, default=None, null=True, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024, null=False, blank=True)
