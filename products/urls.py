from django.urls import path

from products import views

urlpatterns = [
    path('create_checkout_session/<int:product_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
    path('webhook', views.stripe_webhook, name="webhook"),
    path('manage_subscription', views.manage_subscriptions_portal, name="manage_subscription"),
    # Register the stripe subscription id into LearningHub DB
    path('new_stripe_subscription', views.manage_stripe_subscriptions, name="manage_stripe_subscriptions")

]
