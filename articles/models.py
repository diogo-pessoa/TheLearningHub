from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.ManyToManyField(User)
    title = models.CharField(max_length=120, null=False)
    content = models.CharField(max_length=10000, null=True)
    description = models.CharField(max_length=256, null=True)
    restricted_access = models.BooleanField(default=False, null=False, blank=False)
    draft = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.title

# @receiver(post_save, sender=User)
# def create_article(sender, instance, created, **kwargs):
#     """
#     Create or update the user profile
#     """
#     if created:
#         Article.objects.create(article=instance)
#     # Editing Articles
