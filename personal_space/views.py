from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from personal_space.models import UserBookmark, UserProfile, UserNote


@login_required(redirect_field_name='home')
def profile_index(request):
    user_bookmarks = UserBookmark.objects.filter(user=request.user)
    user_profile_info = UserProfile.objects.filter(user=request.user)
    user_notes = UserNote.objects.filter(user=request.user)
    context = {
        "user_bookmarks": user_bookmarks,
        "user_profile_info": user_profile_info,
        "user_notes": user_notes
    }
    return render(request, 'profile_index.html', context)


@login_required(redirect_field_name='home')
def update_personal_details(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
# if request.method == 'POST':
#     form = PersonalDetailsForm(request.POST, instance=user_profile )
#     if form.is_valid():
#         form.save()
#         messages.success(request, '')
#         return redirect(reverse('profile_index'))
#     else:
#         messages.error(request,
#                        'Failed to update your details. Please try again!')
