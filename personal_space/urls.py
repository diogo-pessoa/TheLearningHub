from django.urls import path

from personal_space import views

urlpatterns = [
    path('', views.profile_index, name="profile")
]
