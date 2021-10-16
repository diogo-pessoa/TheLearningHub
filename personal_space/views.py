from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from personal_space.models import UserBookmark, UserDetail


@login_required
def profile_index(request):
    user_bookmarks = UserBookmark.objects.filter(user=request.user)
    user_details = UserDetail.objects.filter(user=request.user)
    print(user_bookmarks)
    context = {
        "user_bookmarks": user_bookmarks,
        "user_details": user_details
    }
    return render(request, 'profile_index.html', context)
