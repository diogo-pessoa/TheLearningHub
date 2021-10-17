from django.conf import settings
from django.contrib import admin

# Register your models here.
from personal_space.models import UserProfile, UserBookmark, UserNote

if settings.DEBUG:
    admin.site.register(UserBookmark)
    admin.site.register(UserProfile)
    admin.site.register(UserNote)
