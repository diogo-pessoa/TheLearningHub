from django.conf import settings
from django.contrib import admin

# Register your models here.
from articles.models import Article, Topic

if settings.DEBUG:
    admin.site.register(Article)
    admin.site.register(Topic)
