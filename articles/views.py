from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ArticlesForm
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {'articles': articles})


def write_article(request):
    """
        Allows content Manager to write his own articles
    :param request:
    """
    # TODO Check if is superuser before publish

    if request.method == 'POST':
        if request.user:
            form = ArticlesForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Article Stored')
            return redirect('articles')
    else:
        form = ArticlesForm()
    return render(request, 'write_article.html', {'form': form})
