from django import forms
from .models import Post

class BlogPostFrom(forms.ModelForm):
    class Meta:
        model = Post 
        fields =  ('title',  'content', 'image')