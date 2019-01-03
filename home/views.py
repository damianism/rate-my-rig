from django.shortcuts import render



# function based views!
def home(request):

    return render(request, "home/home.html")
    

def about(request):
    """ view to render blog's about page  """
    context = {
        
    }
    return render(request, "home/about.html", context)
    
