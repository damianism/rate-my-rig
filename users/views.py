from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .forms import UserRegisterForm, UserUpdateFrom, ProfileUpdateFrom
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# All types of messages -  messages.debug, messages.info, messages.success, messages.warning, messages.error


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
    """ view to display currenly logged in user's profile  """
    
    # cant pass in User in here (instance=User) becuase User the entire OBJECT MODEL
    # if we do "<django.db.models.query_utils.DeferredAttribute object at 0x7f08da4159e8>" will be displayed in the form fields
    # since it doesnt hold any user data! it's the User MODEL!
    # in order to populate the form with the user data, we gotta pass in an INSTANCE of the CURRENT USER!
    # "request.user" is the currently logged in user. we pass it in as an instance of the User model which holds the user data
    # request is the equivalent of session in Flask

    if request.method == "POST":
        user_form = UserUpdateFrom(request.POST, instance=request.user) # request.POST being the data pushed with the post
        user_profile_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)   # request.FILES being the files(image in this case) pushed with the post
        user_db = User.objects.get(id=request.user.id)      # get the current user data in the database

        # save both forms if they are validated successfully
        if user_form.is_valid() and user_profile_form.is_valid():
            
            if request.user.username != user_db.username:
                messages.success(request, "Your 'username' was successfully updated.")
            if request.user.email != user_db.email:
                messages.success(request, "Your 'email' was successfully updated.")
            if request.user.profile.image.url != user_db.profile.image.url:
                messages.success(request, "Your 'image' was successfully updated.")
            
            # save into db
            user_form.save()
            user_profile_form.save()

            return redirect("user-profile")   # redirecting back to "user-profile" to avoid post-get direct pattern
    else:
        user_form = UserUpdateFrom(instance=request.user)
        user_profile_form = ProfileUpdateFrom(instance=request.user.profile)        
    
    
    context = {
        "user_form": user_form,
        "user_profile_form": user_profile_form
    }
    
    return render(request, "users/profile.html", context)
    
