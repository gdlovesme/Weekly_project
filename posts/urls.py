from django.urls import path


from posts import views

urlpatterns = [
    path('posts/', views.PostCreateView.as_view(), name='posts-list'),
    path('post-create/', views.PostCreateView.as_view(), name='post-create'),
]