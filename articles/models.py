from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=False)
    content = models.CharField(max_length=10000, null=True)
    description = models.CharField(max_length=256, null=True)
    restricted_access = models.BooleanField(default=False, null=False, blank=False)
    draft = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):        # TODO to help on troubleshooting remove on final versions
        return str(self.__dict__)
