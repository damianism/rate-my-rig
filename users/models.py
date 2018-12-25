from django.db import models
from django.contrib.auth.models import User
# third party package to resize images
from django_resized import ResizedImageField




class Profile(models.Model):
    """ expanding on User class to be able to add profile pictures """
    
    # one-to-one relationship between user and the profile - a user has only one profile and a profile belongs to only one user
    # for one-to-one relationship for user "models.OneToOneField" is used
    # on_delete=models.CASCADE  - means that if the user was deleted, delete his/her profile with it
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ResizedImageField(default='defaults/default_profile_pic.png',upload_to='profile_pics', size=[250, 250])
    # image = models.ImageField(default='defaults/default_profile_pic.png',upload_to='profile_pics')
    
    
    def __str__(self):
        return "{}'s Profile".format(self.user.username)

