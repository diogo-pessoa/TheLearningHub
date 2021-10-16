from django.contrib import admin

# Register your models here.
from articles.models import Article, Topic
from personal_space.models import UserDetail, UserBookmark

admin.site.register(UserBookmark)
admin.site.register(UserDetail)