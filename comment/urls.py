from django.urls import path


from comment import views

urlpatterns = [
    path('comments/', views.CommentsView.as_view(), name='comment-list'),
    path('create-comment', views.CommentCreateView.as_view(), name='create-comment')
]