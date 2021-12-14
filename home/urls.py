from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.main_pages, name="home"),
    path('about', views.main_pages, name="about"),
    path('pricing', views.main_pages, name="pricing"),
    path('edit_page/<int:page_id>/', views.edit_page, name='edit_page'),
    path('terms_of_service', views.main_pages, name="terms_of_service"),
    path('privacy_policy', views.main_pages, name="privacy_policy"),
    path('search/', views.search, name="search"),
    path('learning_area/', views.learning_area, name="learning_area"),
    path('upload_file', views.upload_file, name='upload_file'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('content_management', views.content_management, name="content_management"),
]
