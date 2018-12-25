from django.db.models.signals import post_save  # the SIGNAL - this is the signal that gets fired after an image is saved!
from django.contrib.auth.models import User     # the SENDER - User will be the sender! it is the model that's going to be sending the signal
from django.dispatch import receiver            # the RECEIVER - is a function(DECORATOR) that receives the signal that was sent by the SENDER (the User in this case) and carry out a TASK (creating a profile)
from .models import Profile                     # the Profile - needed since we'll be creating a profile in our function


"""
IMPORTANT NOTES:
we want to get a post_save signal, when a user is created!
The "SENDER"(User) will send a "SIGNAL"(post_save) to the "RECEIVER" (decorator function) when a user is created.

@receiver
      takes in the SIGNAL and SENDER
      When a user(SENDER) is saved then send the "SIGNAL" (post_save) to the "@receiver"
      the SIGNAL is then received by the "@receiver" which triggers the TASK ( create_profile() )

create_profile(sender, instance, created, **kwargs)
    sender:     User 
    instance:   is the instance of the User (user that was just created)
    created:    conditional to check if the user was created 
    **kwargs:   accepts ANY additional arguments into the fucntion
"""



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ creates a user profile, when a user is created """
    if created:
        Profile.objects.create(user=instance)   # only need an instance to create a profile - will use the default-image set in the "Profile" model


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """ saves the created user profile when a user is created """

    instance.profile.save() # instance being the user (instance of the User)  sample structure:  user --> profile --> image --> url