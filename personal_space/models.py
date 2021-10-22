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
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)


class UserNote(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=96, null=False, blank=False)
    body = models.CharField(max_length=800, null=False)
    content_path = models.CharField(max_length=128, null=False, blank=False)
    content_title = models.CharField(max_length=128, null=False, blank=False)
