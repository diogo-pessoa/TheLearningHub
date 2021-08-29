from datetime import datetime

from django.conf import settings
from django.db import models


# Create your models here.
class Topic(models.Model):
    class Meta:
        verbose_name_plural = 'Topic'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Article(models.Model):
    topic = models.ForeignKey('Topic', null=True, blank=True,
                              on_delete=models.SET_NULL)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField(max_length=80, null=False)
    content = models.TextField()
    description = models.TextField()
    restricted_access = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, null=False)

    def __str__(self):
        return self.name
