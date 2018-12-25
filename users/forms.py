from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegisterForm(UserCreationForm):
    """ expand on django's UserCreationForm class to add a new field (email)
    """    

    # Fields to add/edit
    email = forms.EmailField()
    
    class Meta:
        
        # model = User - simply means that the model that's going to be affected is the "User" model
        model = User  # so whenever form.save() is carried out, it will save it to this "User" model
        
        # fields - taking the desired fields to show on the form in ORDER!
        fields = [
            'username',
            'email',
            'password1',
            'password2'
            ]