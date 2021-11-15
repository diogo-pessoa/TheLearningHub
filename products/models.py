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
    subscription = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.subscription.name
