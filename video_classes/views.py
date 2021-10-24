from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(redirect_field_name='home')
def create_video_class(request):
    return render(request, 'new_video_class.html')


def video_class(request):

    return render(request, 'video_class.html')


@login_required(redirect_field_name='home')
def delete_video_class(request):
    return None


@login_required(redirect_field_name='home')
def edit_video_class(request):
    return None
