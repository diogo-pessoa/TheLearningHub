from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

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
            form = ArticlesForm(request.POST, author_id=request.user.id)
            if form.is_valid():
                form.save()
                messages.success(request, 'Article Stored')
            return redirect('articles')
    else:
        form = ArticlesForm(author_id=request.user.id)
    return render(request, 'write_article.html', {'form': form})


# def edit_article(request, article_id):
#     return None


def delete_article(request, article_id):
    """ Check if is super user or author before deleting article"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not allowed to remove an article')
        return redirect(reverse('home'))

    product = get_object_or_404(Article, pk=article_id)
    product.delete()
    messages.success(request, 'Article removed')
    return redirect(reverse('articles'))
