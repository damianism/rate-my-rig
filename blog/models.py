from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .helper_funcs import RAM_CHOICES, PSU_CHOICES, CPU_CHOICES, GPU_CHOICES
from decimal import Decimal
# third party package to resize images
from django_resized import ResizedImageField

class Post(models.Model):
    """ Create model for a typical build """
    
    title = models.CharField(max_length=60)
    cpu   = models.CharField(max_length=30, choices=CPU_CHOICES, default='i5 Gen-8')
    gpu   = models.CharField(max_length=30, choices=GPU_CHOICES, default='GTX 1080')
    ram   = models.CharField(max_length=30, choices=RAM_CHOICES, default='8GB')
    psu   = models.CharField(max_length=30, choices=PSU_CHOICES,default='750W')

    primary_storage   = models.CharField(max_length=120)
    secondary_storage = models.CharField(max_length=120, blank=True)
    mainboard         = models.CharField(max_length=120)
    description       = models.TextField(blank=True)
    date_posted       = models.DateTimeField(default=timezone.now)
    views             = models.IntegerField(default=0)
    image             = ResizedImageField(default='defaults/default_rig_pic.png', upload_to='posts_pics', size=[500, 500], blank=True)
    price             = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal(100.00))
    author            = models.ForeignKey(User, on_delete=models.CASCADE)     #  if the user was deleted - delete all his/her post
                                                                              #  if the post of deleted - user will remain intact
    # difference between redirect() and reverse()
    # redirect:  redirects you to a specific route
    # reverse:   returns the full url as string to a specific route 
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk}) 
    
    def __str__(self):
        return self.title
    
