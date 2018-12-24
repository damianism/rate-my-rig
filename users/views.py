from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def register(request):
    """ view to display the registration page """
    form = UserCreationForm()   # blank form 
    return render(request,'users/register.html', {'form': form})