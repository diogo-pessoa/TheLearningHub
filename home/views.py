from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.urls import reverse

from home.forms import PageForm
from home.models import Page


def main_pages(request):
    """
    Based on request.path, gets content and renders page accordingly
    :param request:
    :return:
    """
    page_content = Page.objects.get_or_create(title=request.path.strip('/'))
    context = {'page': page_content[0]}
    return render(request, "main_pages_template.html", context)


def terms(request):
    return render(request, "terms-of-service.html")


def privacy(request):
    return render(request, "privacy-policy.html")
