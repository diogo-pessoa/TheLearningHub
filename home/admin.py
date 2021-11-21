from django.contrib import admin

from TheLearningHub.settings import DEVELOPMENT
from home.models import Page

if DEVELOPMENT:
    admin.site.register(Page)
