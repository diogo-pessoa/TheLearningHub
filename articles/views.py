from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ArticlesForm


def index(request):
    return render(request, "articles.html")


@login_required
def write_article(request):
    """
        Allows content Manager to write his own articles
    :param request:
    """
    # TODO Check if is superuser before publish
    if request.method == 'POST':
        if request.user:
            form = ArticlesForm(request.POST, request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Article Stored')
            return redirect('articles')
    else:
        form = ArticlesForm()
    return render(request, 'write_article.html', {'form': form})
