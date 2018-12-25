from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    """ view to display the registration page """

    form = UserRegisterForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        messages.success(request, "Account '{}' was successfuly created! You can now login".format(username))
        form.save()     # save form if successfully validated 
        return redirect("user-login")    
        
    return render(request,'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, "users/profile.html")