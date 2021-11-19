from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('service_terms', views.terms, name="service_terms"),
    path('privacy_policy', views.privacy, name="privacy_policy"),
    # privacy-policy

]
