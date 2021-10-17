from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articles.models import Article


class UserBookmark(models.Model):
    content_title = models.CharField(max_length=254)
    content_path = models.CharField(max_length=256, null=False, blank=False)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=256, null=False, blank=False)


class UserProfile(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=800, null=True)


class UserNote(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    note_content = models.CharField(max_length=800, null=True)
    content_path = models.CharField(max_length=128, null=False, blank=False)
