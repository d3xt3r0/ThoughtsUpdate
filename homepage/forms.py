from cProfile import label
from importlib.metadata import requires
from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):

    content = forms.TextInput(attrs={'required':False, 'name':''})

    class Meta:
        model = Post
        fields = ['content']

        widgets = {
            'content': forms.TextInput(attrs={
                               'placeholder':"What's Happening",
                               'label': '',
                               'required': 'True'})
        }
    
