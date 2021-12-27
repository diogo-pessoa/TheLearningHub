from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from home.forms import UploadFileForm
from home.models import LearningFileStorage
from personal_space.models import UserBookmarkArticle
from .forms import ArticlesForm
from .models import Article


def article(request, article_id):
    """ Display the user's profile.
    :param request:
    :param article_id:
    """

    article = get_object_or_404(Article, id=article_id)
    user_bookmark = None
    if request.user.is_authenticated:
        user_bookmark = UserBookmarkArticle.objects.filter(user=request.user, article=article)

    context = {
        'article': article,
        'user_bookmark': user_bookmark
    }

    return render(request, 'article.html', context)


@login_required(redirect_field_name='home')
def write_article(request):
    """
        Allows content Manager to write his own articles
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only content Managers can create new content Articles.')
        return redirect(reverse('learning_area'))

    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article Stored')
        return redirect('learning_area')
    else:
        form = ArticlesForm()
        file_form = UploadFileForm()
        files_on_page = LearningFileStorage.objects.all()

        context = {'form': form,
                   'file_form': file_form,
                   'files': files_on_page
                   }
    return render(request, 'write_article.html', context)


@login_required(redirect_field_name='home')
def edit_article(request, article_id):
    """
        Allows content Managers to edit articles
        :param request:
        :param article_id:
        :return:
    """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, You are not authorized to do this action.')
        return redirect(reverse('learning_area'))

    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = ArticlesForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article changes are saved.')
            return redirect(reverse('article', args=[article.id]))
        else:
            messages.error(request,
                           'Failed to update Article. Please try again!')
    else:
        form = ArticlesForm(instance=article)
        file_form = UploadFileForm()
        files_on_page = LearningFileStorage.objects.all()
        context = {
            'form': form,
            'article': article,
            'file_form': file_form,
            'files': files_on_page
        }
        return render(request, 'write_article.html', context)


@login_required(redirect_field_name='home')
def delete_article(request, article_id):
    """ Check if is is_staff user or author before deleting article"""
    if not request.user.is_staff:
        messages.error(request, 'Sorry, you are not allowed to remove an article')
        return redirect(reverse('home'))

    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    messages.success(request, 'Article removed Successfully!')
    return redirect(reverse('learning_area'))
