from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

from personal_space.models import UserBookmark, UserProfile, UserNote


@login_required
def profile_index(request):
    user_bookmarks = UserBookmark.objects.filter(user=request.user)
    user_profile_info = UserProfile.objects.filter(user=request.user)
    user_notes = UserNote.objects.filter(user=request.user)
    user_role_information = request.user
    context = {
        "user_bookmarks": user_bookmarks,
        "user_profile_info": user_profile_info,
        "user_role_information": user_role_information,
        "user_notes": user_notes
    }
    return render(request, 'profile_index.html', context)
