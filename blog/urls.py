from django.urls import path
from .views import (
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    FilterPostListView,
    post_detail_view
)

urlpatterns = [
    path('', FilterPostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/', post_detail_view, name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view() , name='post-delete'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    ]
