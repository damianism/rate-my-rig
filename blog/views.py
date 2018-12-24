from django.shortcuts import render
from posts.models import Post


# Create your views here.
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