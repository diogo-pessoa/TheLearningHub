from tinymce import HTMLField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Topic(models.Model):
    class Meta:
        verbose_name_plural = 'topics'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Article(models.Model):
    topic = models.ForeignKey('Topic', null=True, blank=True,
                              on_delete=models.SET_NULL)
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=False)
    content = HTMLField('Content')
    description = models.CharField(max_length=256, null=True)
    premium_content = models.BooleanField(default=False, null=False, blank=False)
    draft = models.BooleanField(default=True, null=False, blank=False)
    last_update_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.title
