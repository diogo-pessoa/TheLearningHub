from django.urls import path

from personal_space import views

urlpatterns = [
    path('', views.profile_index, name="profile"),
    path('update_personal_details', views.update_personal_details, name="update_personal_details"),
    path('add_bookmark/', views.add_bookmark, name="add_bookmark"),
    path('remove_bookmark/<int:bookmark_id>/', views.remove_bookmark, name="remove_bookmark")
]
