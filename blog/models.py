from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .helper_funcs import *
# third party package to resize images
from django_resized import ResizedImageField

class Post(models.Model):
    """ Create model for a typical post """
    
    title             = models.CharField(max_length=120)
    
    # get choices
    RAM_CHOICES, PSU_CHOICES, CPU_CHOICES, GPU_CHOICES = get_choices()
    
    cpu = models.CharField(max_length=30, choices=CPU_CHOICES, default='i5 Gen-8')
    gpu = models.CharField(max_length=30, choices=GPU_CHOICES, default='GTX 1080')
    ram = models.CharField(max_length=30, choices=RAM_CHOICES, default='8GB')
    psu = models.CharField(max_length=30, choices=PSU_CHOICES,default='750W')

    primary_storage   = models.CharField(max_length=120)
    secondary_storage = models.CharField(max_length=120, blank=True)
    mainboard         = models.CharField(max_length=120)
    description       = models.TextField(blank=True)
    date_posted       = models.DateTimeField(default=timezone.now)
    views             = models.IntegerField(default=0)
    image             = ResizedImageField(default='defaults/default_rig_pic.png', upload_to='posts_pics', size=[500, 500], blank=True)
    author            = models.ForeignKey(User, on_delete=models.CASCADE)     #  if the user was deleted - delete all his/her post
                                                                              #  if the post of deleted - user will remain intact

    # difference between redirect() and reverse()
    # redirect:  redirects you to a specific route
    # reverse:   returns the full url as string to a specific route 
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk}) 
    
    
    def __str__(self):
        return self.title
    

""" 
IMPORTANT NOTES:
    User:
    
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        
        - user are handles in django by default using the "User" table
              from django.contrib.auth.models import User    ---> will import the Uset Table (model)
        - User to posts relationsship is one to many - as one user can post multiple posts but each post has only one author
              https://docs.djangoproject.com/en/2.1/topics/db/examples/many_to_one/              explains many-to-one relationship 
        - on_delete=models.CASCADE 
              simply means that if the user(author) was deleted, delete all his/her posts as well.    
    
    DATABASE STRUCTURE AND SHELL
    
    python3 manage.py shell         # to access shell
    
    from django.contrib.auth.models import User         # import User table
    from blog.models import Post                        # import Post table
    post = Post.objects.first()     # get the first post
    post = Post.objects.get(id=3)   # or any post using id
    post.content                    # get the content of the post
    post.author                     # will return the entire use OBJECT! allowing us to access user based attributes
    post.author.email               # returns the user email - the user whom made the post
    
    
    HOW TO GET ALL THE POSTS BY A USER?
    
    this can be done using Django's very own "QuerySets"
    by default it would take the following form
                    .<modelname>_set   
    examples
    # user.<modelname>_set  
    user.post_set           # will return the an object that includes all the "posts" but we cant use it
    user.post_set.all()     # will return the actual QuerySet - <QuerySet [<Post: Blog 1>, <Post: Blog 2>]>
    
    QUERYSET CAN BE USED TO CREATE POSTS VIA USER
    
    # Post model attributes going in
    user.post_set.create(title='Blog 3', content='Third post content!')     # notice that no author (user) is required!!!!!
                                                                            # django already knowns the user since we're using the user to create the post
                                                                            # .save() isnt required as it automatically adds it to the db
    
    
    # so checking the Post again
    Post.objects.all()   # returns <QuerySet [<Post: Blog 1>, <Post: Blog 2>, <Post: Blog 3>]>
"""
