from django.shortcuts import render

posts = [
    {
        'author': 'admin',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted': 'May 13, 2018'
    },
    {
        'author': 'damian R',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted': 'May 14, 2018'        
    }

]



# Create your views here.
def home(request):
    """ a view to render blog's home page """
    context = {
        'posts': posts
    }
    
    return render(request, "blog/home.html", context)
    
    
    
def about(request):
    """ view to render blog's about page  """
    context = {
        
    }
    return render(request, "blog/about.html", context)