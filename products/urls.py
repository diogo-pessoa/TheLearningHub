from django.urls import path

from products import views

urlpatterns = [
    path('create_checkout_session/<int:product_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('', views.pricing, name='pricing'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
    path('webhook', views.my_webhook_view, name="webhook"),
]

