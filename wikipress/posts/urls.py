from django.urls import path
from django.contrib.auth.views import LoginView

from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.group_list, name='index'),
    path('post/<slug:slug>/', views.post_page, name='posts_page'),
    path('posts/<slug:slug>/', views.post_list, name='posts'),
    path('post/<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('create/', views.post_create, name='post_create'),
    path('login/', views.MyLoginView.as_view(template_name='posts/login.html'), name='login'),
    path('search/', views.search_list, name='search'),
    
]