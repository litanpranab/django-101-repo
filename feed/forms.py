from cProfile import label
from django import forms


class PostForm(forms.Form):
    text = forms.CharField(label='Title')
    image = forms.FileField()
