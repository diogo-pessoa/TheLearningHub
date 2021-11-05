from django.urls import path

from personal_space import views

urlpatterns = [
    path('', views.profile_index, name="profile"),
    path('update_personal_details', views.update_personal_details, name="update_personal_details"),
    path('add_bookmark/<int:article_id>/', views.add_bookmark, name="add_bookmark")
]
