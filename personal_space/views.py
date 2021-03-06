from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from articles.models import Article
from personal_space.forms import PersonalDetailsForm
from personal_space.models import UserBookmarkArticle, UserProfile, UserNoteFromVideoClass, UserBookmarkVideoClass
from products.models import UserSubscription
from src.personal_space_functions.bookmark import build_unified_bookmark_dict
from video_classes.models import VideoClass


@login_required(redirect_field_name='home')
def profile_index(request):
    user_article_bookmarks = UserBookmarkArticle.objects.filter(user=request.user)
    user_video_bookmarks = UserBookmarkVideoClass.objects.filter(user=request.user)
    user_bookmarks = build_unified_bookmark_dict(user_article_bookmarks, user_video_bookmarks)
    user_profile_info = UserProfile.objects.filter(user=request.user)
    user_notes = UserNoteFromVideoClass.objects.filter(user=request.user)
    user_subscription = UserSubscription.objects.filter(user=request.user).first() or None
    context = {
        'user_profile_info': user_profile_info,
        'user_notes': user_notes,
        'user_subscription': user_subscription,
        'user_bookmarks': user_bookmarks
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


# Article bookmarks
@login_required()
def add_bookmark(request):
    if request.method == 'POST':
        article_id = request.POST['article_id']
        article = Article.objects.filter(id=article_id)
        # Creating bookmark
        if article:
            UserBookmarkArticle.objects.get_or_create(user=request.user, article=article[0])
            messages.success(request, 'Article added to your favorites!')
            return redirect('article', article_id)
        else:
            messages.error(request, 'Sorry there was an issue when bookmarking this Article. Try again later!')
            return redirect('article', article_id)


@login_required()
def remove_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(UserBookmarkArticle, pk=bookmark_id)
    if bookmark:
        bookmark.delete()
        messages.success(request, 'Removed from your bookmarks')
        return redirect('article', bookmark.article.id)
    else:
        messages.error(request, 'Sorry there was an issue when removing this from bookmark. Try again later!')
        return redirect('article', bookmark.article.id)


# Video Classes bookmark
@login_required()
def add_video_class_bookmark(request):
    if request.method == 'POST':
        video_class_id = request.POST['video_class_id']
        video_class = VideoClass.objects.filter(id=video_class_id)
        # Creating bookmark
        if video_class:
            UserBookmarkVideoClass.objects.get_or_create(user=request.user, video_class=video_class[0])
            messages.success(request, 'Class added to your favorites!')
            return redirect('video_class', video_class[0].id)
        else:
            messages.error(request, 'Sorry there was an issue when bookmarking this Video class. Try again later!')
            return redirect('article', video_class[0].id)


@login_required()
def remove_video_bookmark(request, bookmark_id):
    bookmark = get_object_or_404(UserBookmarkVideoClass, pk=bookmark_id)
    if bookmark:
        bookmark.delete()
        messages.success(request, 'Removed from your bookmarks')
        return redirect('video_class', bookmark.video_class.id)
    else:
        messages.error(request, 'Sorry there was an issue when removing this from bookmark. Try again later!')
        return redirect('video_class', bookmark.video_class.id)
