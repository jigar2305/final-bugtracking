from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username', 'password','email','phone_number','roleid','picture')

