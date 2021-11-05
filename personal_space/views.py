from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from articles.models import Article
from personal_space.forms import PersonalDetailsForm
from personal_space.models import UserBookmarkArticle, UserProfile, UserNoteFromVideoClass


@login_required(redirect_field_name='home')
def profile_index(request):
    user_bookmarks = UserBookmarkArticle.objects.filter(user=request.user)
    user_profile_info = UserProfile.objects.filter(user=request.user)
    user_notes = UserNoteFromVideoClass.objects.filter(user=request.user)
    context = {
        "user_bookmarks": user_bookmarks,
        "user_profile_info": user_profile_info,
        "user_notes": user_notes
    }
    return render(request, 'profile_index.html', context)


@login_required(redirect_field_name='home')
def update_personal_details(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=user_profile[0])
        if form.is_valid():
            form.save()
            messages.success(request, 'Personal Details were updated!')
            return redirect(reverse('profile'))
    else:

        form = PersonalDetailsForm(instance=user_profile[0])
        return render(request, 'update_personal_details.html', {
            'form': form,
            'instance': user_profile
        })


@login_required()
def add_bookmark(request, article_id):
    """
    Adds User bookmark
    :param request:
    :param article_id
    :return:
    """
    if request.method == 'POST':
        article = Article.objects.filter(id=article_id)
        # Creating bookmark
        if article:
            UserBookmarkArticle.objects.get_or_create(user=request.user, article=article[0])
            messages.success(request, 'Article added to your favorites!')
            return HttpResponse(status=200)
        else:
            messages.error(request, 'Article Not found, please try Again.')
            return HttpResponse(status=404)
    else:
        messages.error(request, 'Sorry there was an issue when bookmarking this Article. Try again later!')
        HttpResponse(status=503)


@login_required()
def remove_bookmark(request, article_id):
    if request.method == 'POST':
        article = Article.objects.filter(id=article_id)
        # Creating bookmark
        if article:
            bookmark = get_object_or_404(UserBookmarkArticle, article=article[0])
            bookmark.delete()
            messages.success(request, 'Removed from your bookmarks')
            return HttpResponse(status=200)
        else:
            messages.error(request, 'Article Not found, please try Again.')
            return HttpResponse(status=404)
    else:
        messages.error(request, 'Sorry there was an issue when removing this from bookmark. Try again later!')
        HttpResponse(status=503)
