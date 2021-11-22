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
        messages.info(request, f'Editing {page.title}')
        return render(request, 'edit_page.html', {
            'form': form,
            'page': page,
        })


def index(request):
    """ Redirecting root path to home"""
    return redirect('home')
