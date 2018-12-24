from django.shortcuts import render


# Create your views here.
def home(request):
    """ a view to render blog's home page """
    context = {
        
    }
    
    return render(request, "blog/home.html", context)
    
    
    
def about(request):
    """ view to render blog's about page  """
    context = {
        
    }
    return render(request, "blog/about.html", context)