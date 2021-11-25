from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from personal_space.forms import UserNotesFromClassForm
from personal_space.models import UserNoteFromVideoClass
from video_classes.forms import VideoClassForm
from video_classes.models import VideoClass


@login_required(redirect_field_name='home')
def video_class(request, video_class_id):
    videos_class = get_object_or_404(VideoClass, id=video_class_id)
    user_note = UserNoteFromVideoClass.objects.get_or_create(user=request.user, video_class=videos_class)
    if request.method == 'POST':
        form = UserNotesFromClassForm(request.POST, instance=user_note[0])
        if form.is_valid():
            form.save()
            messages.success(request, 'note saved!')
    else:
        form = UserNotesFromClassForm(instance=user_note[0])
    context = {
        'video_class': videos_class,
        'user_note': user_note,
        'form': form
    }

    return render(request, 'video_class.html', context)


@login_required(redirect_field_name='home')
def delete_video_class(request, video_class_id):
    """ Only allows to delete video if staff """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, you are not allowed to remove content')
        return redirect(reverse('learning_area'))

    video_class = get_object_or_404(VideoClass, pk=video_class_id)
    video_class.delete()
    messages.success(request, 'Video Class Deleted successfully!')
    return redirect(reverse('learning_area'))


@login_required(redirect_field_name='home')
def create_video_class(request):
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only content Managers can create video_class.')
        return redirect(reverse('learning_area'))

    if request.method == 'POST':
        form = VideoClassForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Video Class created')
        else:
            messages.success(request, 'Sorry, there was an issue creating this Video class. Please Try again.')
        return redirect('learning_area')
    else:
        form = VideoClassForm()
    return render(request, 'video_class_form.html', {'form': form})


@login_required(redirect_field_name='home')
def edit_video_class(request, video_class_id):
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only content Managers can manage video_classes')
        return redirect(reverse('learning_area'))
    video_class = get_object_or_404(VideoClass, pk=video_class_id)
    if request.method == 'POST':
        form = VideoClassForm(request.POST, request.FILES, instance=video_class)
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video Class updated.')
        else:
            messages.success(request, 'Sorry, there was an issue editing this Video class. Please Try again.')
        return redirect('learning_area')
    else:
        form = VideoClassForm(instance=video_class)
    return render(request, 'video_class_form.html', {'form': form})
