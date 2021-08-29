from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "articles.html")


def write_article(request):
    return render(request, 'write_article.html')
