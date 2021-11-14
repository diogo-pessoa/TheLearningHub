from django.conf import settings
from django.contrib import admin

# Register your models here.
from personal_space.models import UserProfile, UserBookmarkArticle, UserNoteFromVideoClass

if settings.DEVELOPMENT:
    admin.site.register(UserBookmarkArticle)
    admin.site.register(UserProfile)
    admin.site.register(UserNoteFromVideoClass)
