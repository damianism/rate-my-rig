from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import UserRegisterForm, UserUpdateFrom, ProfileUpdateFrom
from django.contrib.auth.decorators import login_required


# All types of messages
# messages.debug, messages.info, messages.success, messages.warning, messages.error

def register_original(request):
    """ view function that uses django's "UserCreationForm" class to
    display the register template """
    
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save() # form has been validated to be error free, we can now SAVE!
        username = form.cleaned_data.get("username")
        messages.success(request, "Account create for {}!".format(username))
        return redirect("blog-home")    
    
    return render(request, 'users/register.html', {'form':form})
    


def register(request):
    """ view function that uses the custom "UserRegisterForm" class (Email field added)
    to display the registration page """

    form = UserRegisterForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        messages.success(request, "Account '{}' was successfuly created! You can now login".format(username))
        form.save()     # save form if successfully validated 
        return redirect("user-login")    
        
    return render(request,'users/register.html', {'form': form})


@login_required
def profile(request):
    """ view to display user's profile  """
    
    # cant pass in User in here (instance=User) becuase User the entire OBJECT MODEL
    # if we do "<django.db.models.query_utils.DeferredAttribute object at 0x7f08da4159e8>" will be displayed in the form fields
    # since it doesnt hold any user data! it's the User MODEL!
    # in order to populate the form with the user data, we gotta pass in an INSTANCE of the CURRENT USER!
    # "request.user" is the currently logged in user. we pass it in as an instance of the User model which holds the user data
    # request is the equivalent of session in Flask

    if request.method == "POST":
        user_form = UserUpdateFrom(request.POST, instance=request.user)
        user_profile_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
    else:
        user_form = UserUpdateFrom(instance=request.user)
        user_profile_form = ProfileUpdateFrom(instance=request.user.profile)        
    
    
    context = {
        "user_form": user_form,
        "user_profile_form": user_profile_form
    }
    
    return render(request, "users/profile.html", context)
    
