from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Group
# Create your views here.

def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.select_related('author', 'group').all()
    group = Group.objects.all()
    context = {'post_list': post_list,
               'group': group}
    return render(request, template , context)

