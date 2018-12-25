from django.shortcuts import render
from posts.models import Post
from django.views.generic import ListView



# function based views!
def home(request):
    """ a view to render blog's home page """
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, "blog/home.html", context)
    

def about(request):
    """ view to render blog's about page  """
    context = {
        
    }
    return render(request, "blog/about.html", context)
    

# class based views

class PostListView(ListView):
    """ class base view to display all the posts """
    
    # where it looks for the template and what template
    # <app>/<model>_<viewtype>.html     - e.g. blog/posts_list.html
    
    model = Post    # based on what class
    
    template_name = 'blog/home.html'    # to replace the default template (blog/posts_list.html) use "template_name"
    # context_object_name = 'posts'     # to replace the default context name (object_list) use "context_object_name"
    ordering = ['-date_posted']         # change the order  - ['-date_posted'] to reverse the order