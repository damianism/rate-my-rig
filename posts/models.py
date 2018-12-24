from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .helper_funcs import *

# Field.null    - If True, Django will store empty values as NULL in the database. Default is False.
# Field.blank   - If True, the field is allowed to be blank. Default is False.


class Post(models.Model):
    """ Create model for a typical post """
    
    title             = models.CharField(max_length=120)
    
    # get choices
    RAM_CHOICES, PSU_CHOICES, CPU_CHOICES, GPU_CHOICES = get_choices()
    
    cpu = models.CharField(max_length=20, choices=CPU_CHOICES, default='i5 Gen-8')
    gpu = models.CharField(max_length=20, choices=GPU_CHOICES, default='GTX 1080')
    ram = models.CharField(max_length=20, choices=RAM_CHOICES, default='8GB')
    psu = models.CharField(max_length=20, choices=PSU_CHOICES,default='750W')

    primary_storage   = models.CharField(max_length=120, blank=True)
    secondary_storage = models.CharField(max_length=120, blank=True)
    mainboard         = models.CharField(max_length=120, blank=True)
    description       = models.TextField(blank=True)
    short_info        = models.TextField(blank=True)
    date_posted       = models.DateTimeField(default=timezone.now)
    author            = models.ForeignKey(User, on_delete=models.CASCADE)     #  if the user was deleted - delete all his/her post
                                                                              #  if the post of deleted - user will remain intact

    @property
    def get_status(self):
        return CPU_CHOICES[self.cpu][1]
        
    # # take look at "product_list.html" - this thing is FUKCING amazing!
    # def get_absolute_url(self):
    #     # return "../product/dynamic/{}".format(self.id)            # -- HARD-CODED!
        
    #     # reverse("app_name:view_name", kwargs={"myid": self.id}) - "app_name" is defined in the app's urls.py
    #     return reverse("products:detailed_view", kwargs={"myid": self.id})   # -- DYNAMIC!  path('p/dynamic/<int:myid>', dynamic_lookup_view, name="detailed_view"), would still work!
    
    
    def __str__(self):
        return self.title
    

