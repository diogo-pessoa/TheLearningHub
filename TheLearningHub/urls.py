"""TheLearningHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from filebrowser.sites import site

urlpatterns = [
                  path('accounts/', include('allauth.urls')),
                  path('', include('home.urls')),
                  path('articles/', include('articles.urls')),
                  path('personal_space/', include('personal_space.urls')),
                  path('video_class/', include('video_classes.urls')),
                  path('products/', include('products.urls')),
                  # tinyMCE & filebrowser
                  url(r'^admin/filebrowser/', site.urls),
                  re_path(r'^tinymce/', include('tinymce.urls')),
                  path('admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
