from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from video_classes.models import VideoClass


@login_required(redirect_field_name='home')
def create_video_class(request):
    return render(request, 'new_video_class.html')


def video_class(request, video_class_id):
    videos_class = get_object_or_404(VideoClass, id=video_class_id)
    context = {
        'video_class': videos_class,
    }

    return render(request, 'video_class.html', context)


@login_required(redirect_field_name='home')
def delete_video_class(request, video_class_id):
    """ Only allows to delete video if staff """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, you are not allowed to remove content')
        return redirect(reverse('articles'))

    video_class = get_object_or_404(VideoClass, pk=video_class_id)
    video_class.delete()
    messages.success(request, 'Video Class Deleted successfully!')
    return redirect(reverse('articles'))


@login_required(redirect_field_name='home')
def edit_video_class(request, video_class_id):
    #TODO
    return None
