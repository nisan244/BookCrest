from django import forms
from . import models

class Comment_Form(forms.ModelForm):
    class Meta:
        model = models.Comment_model
        fields = ('name', 'email', 'body')
        