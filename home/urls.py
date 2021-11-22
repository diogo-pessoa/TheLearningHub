from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.main_pages, name="home"),
    path('about', views.main_pages, name="about"),
    path('edit_page/<int:page_id>/', views.edit_page, name='edit_page'),
    path('terms_of_service', views.main_pages, name="terms_of_service"),
    path('privacy_policy', views.main_pages, name="privacy_policy")
]
