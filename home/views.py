from django.shortcuts import render



# function based views!
def home(request):
    """ view to render the home template """
    
    return render(request, "home/home.html")
    

def about(request):
    """ view to render blog's about page  """

    return render(request, "home/about.html")
    
