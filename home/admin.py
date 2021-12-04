from django.contrib import admin

from TheLearningHub.settings import DEVELOPMENT
from home.models import Page, LearningFileStorage

if DEVELOPMENT:
    admin.site.register(Page)
    admin.site.register(LearningFileStorage)
