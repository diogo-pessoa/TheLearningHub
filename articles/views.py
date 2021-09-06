from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ArticlesForm
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "articles.html", {'articles': articles})


def article(request, article_id):
    """ Display the user's profile.
    :param request:
    :param article_id:
    """
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article,
    }

    return render(request, 'article.html', context)


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
