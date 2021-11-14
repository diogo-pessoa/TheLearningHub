from django.conf import settings
from django.contrib import admin

from video_classes.models import VideoClass

if settings.DEVELOPMENT:
    admin.site.register(VideoClass)
