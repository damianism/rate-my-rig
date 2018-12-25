from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    # path('',views.home, name='blog-home'),
    path('', PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('about/',views.about, name='blog-about')
    ]
    
    
"""
class based views need the method ".as_view()" at the end to convert them
into actual views

    general convention for the list_template of class views
    
    <app>/<model>_<viewtype>.html - blog/posts_list.html 
    
    in this case:   
        blog/posts_list.html    - blog being the app, posts being the model, and list being the viewtype
    
"""