from django.urls import path

from video_classes import views

urlpatterns = [
    path('create', views.create_video_class, name="create"),
    path('<int:video_class_id>/', views.video_class, name="video_class"),
    path('delete/<int:video_class_id>/', views.delete_video_class, name='delete'),
    path('edit/<int:video_class_id>/', views.edit_video_class, name='edit'),
]
