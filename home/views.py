from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def terms(request):
    return render(request, "terms-of-service.html")


def privacy(request):
    return render(request, "privacy-policy.html")