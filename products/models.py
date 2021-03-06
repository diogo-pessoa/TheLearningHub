from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stripe_product_id = models.CharField(max_length=100, null=True)
    stripe_product_mode = models.CharField(max_length=100, null=True, default='subscription')

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    subscription = models.CharField(max_length=128, null=True, default=None)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=None)
    stripe_customer_id = models.CharField(max_length=128, null=True, default=None)
    subscription_active = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f'stripe subscription active {self.subscription_active} for {self.user}'

    def is_subscription_active(self):
        return self.subscription_active
