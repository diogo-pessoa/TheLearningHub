from django.contrib import admin

# Register your models here.
from articles.models import Article, Topic
from personal_space.models import UserProfile, UserBookmark

admin.site.register(UserBookmark)
admin.site.register(UserProfile)