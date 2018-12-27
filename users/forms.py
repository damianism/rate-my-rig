from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """ expand on django's UserCreationForm class to add a new field (email)
    """    

    # Fields to add/edit
    email = forms.EmailField()
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=30)
    class Meta:
        
        # model = User - simply means that the model that's going to be affected is the "User" model
        model = User  # so whenever form.save() is carried out, it will save it to this "User" model
        
        # fields - taking the desired fields to show on the form in ORDER!
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
            ]
            
    # to validate individual fields - custom validations
    # validation methods are used which written as -->   def clean_<field>(self):
    def clean_email(self):
        # get the field from the cleaned_data dictionary first!
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email address already exists.")

            
class UserUpdateFrom(forms.ModelForm):
    """ Form to change username and email from user profile template """
    
    email = forms.EmailField()
    
    class Meta:
        model = User  
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
            ]
            
                  
                        
class ProfileUpdateFrom(forms.ModelForm):
    """ Form to change profile pic from user profile template """
    class Meta:
        model = Profile # already contains the image field!
        fields = [
            'image',
            ]
            
            