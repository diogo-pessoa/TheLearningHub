from django.urls import path

from articles import views

urlpatterns = [
    path('', views.index, name="articles"),
    path('<int:article_id>/', views.article, name="article"),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
    # path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('write_article', views.write_article, name="write_article")
]
