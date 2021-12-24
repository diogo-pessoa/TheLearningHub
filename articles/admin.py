from django.conf import settings
from django.contrib import admin

# Register your models here.
from articles.models import Article, Topic

# Keeping Topic enabled in Admin interface until a new Form is available on Control Panel
admin.site.register(Topic)
if settings.DEVELOPMENT:
    admin.site.register(Article)

