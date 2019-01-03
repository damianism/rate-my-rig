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
    # path('about/',views.about, name='blog-about')
    ]
    
    
"""
class based views need the method ".as_view()" at the end to convert them
into actual views

    general convention for the list_template of class views
    
    <app>/<model>_<viewtype>.html - blog/posts_list.html 
    
    in this case:   
        blog/posts_list.html    - blog being the app, posts being the model, and list being the viewtype
    
"""