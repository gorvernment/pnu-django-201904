from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post
from .widgets import TextCounterInput

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ['message']
        widgets = {
            'message':forms.Textarea(attrs={'rows':3})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': TextCounterInput,
            'content': SummernoteWidget,
        }
