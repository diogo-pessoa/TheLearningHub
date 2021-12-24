from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.urls import reverse

from articles.models import Article, Topic
from home.forms import PageForm, UploadFileForm
from home.models import Page, LearningFileStorage
from src.http_helper.http_meta import parser_http_referer
from video_classes.models import VideoClass


def main_pages(request):
    """
    Based on request.path, gets content and renders page accordingly
    :param request:
    :return:
    """
    page_content = Page.objects.get_or_create(title=request.path.strip('/'))
    context = {'page': page_content[0]}
    return render(request, "main_pages_template.html", context)


@login_required(redirect_field_name='login')
def edit_page(request, page_id):
    """
        Allows content Managers to Site Main Pages
        :param request:
        :param page_id:
        :return:
    """

    if not request.user.is_staff:
        messages.error(request, 'Sorry, You are not authorized to do this action.')
        return redirect(reverse('home'))

    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, 'Page updated!')
            return redirect(reverse(page.title))
        else:
            messages.error(request,
                           'Failed to update Page. Please try again!')
    else:
        form = PageForm(instance=page)
        file_form = UploadFileForm()
        # TODO Add a filter relating file to page being edited.
        files_on_page = LearningFileStorage.objects.all()
        messages.info(request, f'Editing {page.title}')
        return render(request, 'edit_page.html', {
            'form': form,
            'page': page,
            'file_form': file_form,
            'files': files_on_page
        })


def index(request):
    """ Redirecting root path to home"""
    return redirect('home')


def search(request):
    # TODO refactor this View

    articles = Article.objects.all()
    topics = Topic.objects.all()
    video_classes = VideoClass.objects.all()
    query = None
    search_result = None

    if request.GET:
        if request.GET['search_query'] == 'nav_learning_videos':
            context = {
                'search_result': video_classes,
                'search_term': query,
                'topics': topics
            }
            return render(request, "learning_area.html", context)
        elif request.GET['search_query'] == 'nav_learning_articles':
            context = {
                'search_result': articles,
                'search_term': query,
                'topics': topics
            }
            return render(request, "learning_area.html", context)

        if 'search_query' in request.GET:
            query = request.GET['search_query']
            if 'topic' in request.GET:
                articles = articles.filter(topic__name__in=topics)
                video_classes = video_classes.filter(topic__name__in=topics)
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('search'))

            queries = Q(title__icontains=query) | Q(description__icontains=query)
            video_classes = video_classes.filter(queries)
            articles = articles.filter(queries)
        video_classes = [x for x in video_classes]
        articles = [x for x in articles]
        search_result = video_classes + articles

    context = {
        'search_result': search_result,
        'search_term': query,
        'topics': topics
    }
    return render(request, "learning_area.html", context)


def learning_area(request):
    articles = Article.objects.all()
    topics = Topic.objects.all()
    video_classes = VideoClass.objects.all()
    video_classes = [x for x in video_classes]
    articles = [x for x in articles]
    search_result = video_classes + articles

    context = {
        'search_result': search_result,
        'topics': topics
    }
    return render(request, "learning_area.html", context)


# File management views

@login_required(redirect_field_name='home')
def upload_file(request):
    """
    Uploads file to server side and Add a Reference to Learning File Storage model.
    :param request:
    :return: redirect to page where file was uploaded from
    """
    if request.method == 'POST' and request.FILES:
        file_form = UploadFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()
            messages.success(request, 'file uploaded')
            redirect_url = parser_http_referer(request.META['HTTP_REFERER'])
            if redirect_url['id'] == "write_article":
                # Write article is a new object and doesnt have the id argument
                return redirect(reverse(f"{redirect_url['id']}"))
            return redirect(reverse(redirect_url['path'], args=[redirect_url['id']]))
        else:
            messages.error(request, 'Error, Insert a file!')
            HttpResponse(500)


@login_required(redirect_field_name='home')
def delete_file(request, file_id):
    """ Deletes file from filesystem and remove reference fom file Storage Model"""
    content = get_object_or_404(LearningFileStorage, pk=file_id)
    content.delete()
    messages.success(request, 'file removed')
    redirect_url = parser_http_referer(request.META['HTTP_REFERER'])
    if redirect_url['id'] == "write_article":
        # Write article is a new object and doesnt have the id argument
        return redirect(reverse(f"{redirect_url['id']}"))
    return redirect(reverse(redirect_url['path'], args=[redirect_url['id']]))


@login_required(redirect_field_name='home')
def content_management(request):
    pages = Page.objects.all()
    context = {
        'pages': pages
    }
    return render(request, 'control_panel.html', context)
