from django.urls import path

from . import views


app_name = 'posts'


urlpatterns = [
    path('', views.group_list, name='index'),
    path('posts/<int:post_id>/', views.post_page, name='posts_page'),
    path('posts/<slug:slug>/', views.post_list, name='posts'),
]