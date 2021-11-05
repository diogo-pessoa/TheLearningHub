from django.contrib import admin
from django.urls import path

from payments import views

urlpatterns = [
    path('pricing', views.pricing, name="pricing"),
    path('checkout', views.create_checkout_session, name="checkout")
]
