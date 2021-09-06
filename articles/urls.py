from django.contrib import admin
from django.urls import path

from articles import views

urlpatterns = [
    path('', views.index, name="articles"),
    path('write_article', views.write_article, name="write_article"),
    path('<int:article_id>/', views.article, name="article"),

]
