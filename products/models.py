from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stripe_product_id = models.CharField(max_length=100, null=True)
    stripe_product_mode = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    subscription = models.CharField(max_length=128, null=False, default=None)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=None)
    order = models.CharField(max_length=800, null=True)

    def __str__(self):
        return f'{self.subscription.name} for {self.user.username}'
