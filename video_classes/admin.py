from django.conf import settings
from django.contrib import admin

from video_classes.models import VideoClass

if settings.DEBUG:
    admin.site.register(VideoClass)
