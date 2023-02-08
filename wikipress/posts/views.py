from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Group
# Create your views here.

def group_list(request):
    template = 'posts/group_list.html'
    post_list = Post.objects.select_related('author', 'group').all()
    groups = Group.objects.all()
    context = {'post_list': post_list,
               'groups': groups}
    return render(request, template , context)


def post_list(request, slug):
    template = 'posts/post_list.html'
    post_list = Post.objects.select_related('author', 'group').all()
    groups = Group.objects.all()
    group = get_object_or_404(Group, slug=slug)
    context = {'groups': groups,
               'post_list': post_list,
               'group': group}
    return render(request, template , context)


def post_page(request, post_id):
    template = 'posts/post_page.html'
    post_list = get_object_or_404(Post, id=post_id)
    groups = Group.objects.all()
    context = {'groups': groups,
               'post_list': post_list,}
    return render(request, template , context)
