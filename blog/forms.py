from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = (
            
            'title', 
            'cpu',
            'gpu',
            'ram',
            'psu',
            'primary_storage',
            'secondary_storage',
            'mainboard',
            'description',
            'image' 
            
        )