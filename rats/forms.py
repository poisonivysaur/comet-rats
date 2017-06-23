from django import forms
from .models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username',)
    
    password = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)