from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articles.models import Article


class UserBookmarks(models.Model):
    content_title = models.CharField(max_length=254)
    content_path = models.CharField(max_length=256, null=True, blank=True)
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)


class UserDetails(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    bookmarks = models.ForeignKey('UserBookmarks', null=True, blank=True,
                                  on_delete=models.SET_NULL)
    bio = models.CharField(max_length=800, null=True)
