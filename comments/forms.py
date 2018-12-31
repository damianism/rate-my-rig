from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    comment = forms.CharField(
                    widget=forms.Textarea(
                        attrs={
                            "placeholder": "Your comment",
                            "rows": 3,
                            "cols": 50
                            }
                        )
                    )
    
    class Meta:
        model = Comment
        fields = ('comment', 'post','author',)
        exclude = ['post','author']