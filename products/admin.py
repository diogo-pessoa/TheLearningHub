from django.contrib import admin

from TheLearningHub.settings import DEVELOPMENT
from products.models import Product, UserSubscription

if DEVELOPMENT:
    admin.site.register(Product)
    admin.site.register(UserSubscription)
