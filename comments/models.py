from django.db import models
from blog.models import Post
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    """ create model for a comments  """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author.username)
        
    def __unicode(self):
        str(self.author.username)
        
        
