from django.urls import path
from . import views
from .views import (
    HomeListView, CreatePostView, DetailPostView, UpdatePostView, DeletePostView, UserPostListView
)

urlpatterns = [
    path('', HomeListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='post-delete'),
    path('post/<int:pk>/', DetailPostView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about')
]