from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
import json

from .models import Post, Group
from .forms import PostForm
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


def post_page(request, slug):
    template = 'posts/post_page.html'
    post_list = get_object_or_404(Post, slug=slug)
    groups = Group.objects.all()
    context = {'groups': groups,
               'post_list': post_list}
    return render(request, template , context)


def search_list(request):
    template = 'posts/search.html'
    search = Post.objects.filter(title__icontains=request.GET.get('q'))
    groups = Group.objects.all()
    context = {'search': search,
               'groups': groups}
    return render(request, template, context)


def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    groups = Group.objects.all()
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect('posts:index')
    context = {'groups': groups,
               'form': form,}
    return render(request, 'posts/create_post.html', context)


def post_edit(request, slug):
    post_list = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,
                    files=request.FILES or None,
                    instance=post_list)
    author = post_list.author
    groups = Group.objects.all()
    if author != request.user:
        return redirect('posts:index')
    if form.is_valid():
        form.save()
        return redirect('posts:index')
    context = {
        'groups': groups,
        'post_list': post_list,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'posts/create_post.html', context)


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('posts:index') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Неправильный логин или пароль')
        return self.render_to_response(self.get_context_data(form=form))    


    
    