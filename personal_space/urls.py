from django.urls import path

from personal_space import views

urlpatterns = [
    path('', views.profile_index, name="profile"),
    path('update_personal_details', views.update_personal_details, name="update_personal_details"),
    # Article bookmark
    path('add_bookmark/', views.add_bookmark, name="add_bookmark"),
    path('remove_bookmark/<int:bookmark_id>/', views.remove_bookmark, name="remove_bookmark"),
    # video_bookmarks
    path('add_video_bookmark/', views.add_video_class_bookmark, name="add_video_bookmark"),
    path('remove_video_bookmark/<int:bookmark_id>/', views.remove_video_bookmark, name="remove_video_bookmark")
]
