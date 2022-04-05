from django.urls import path

from posts import views

urlpatterns = [
    path('posts', views.posts, name='posts-list')
]