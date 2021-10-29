from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from personal_space.forms import PersonalDetailsForm, UserNotesForm
from personal_space.models import UserBookmark, UserProfile, UserNoteFromVideoClass
from video_classes.models import VideoClass


@login_required(redirect_field_name='home')
def profile_index(request):
    user_bookmarks = UserBookmark.objects.filter(user=request.user)
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
