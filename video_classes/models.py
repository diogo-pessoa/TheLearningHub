from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from articles.models import Topic


class VideoClass(models.Model):
    topic = models.ForeignKey(Topic, null=True, blank=True,
                              on_delete=models.SET_NULL)
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=False)
    video_path = models.FileField(null=True)
    description = models.CharField(max_length=256, null=True)
    restricted_access = models.BooleanField(default=False, null=False, blank=False)
    draft = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.title
