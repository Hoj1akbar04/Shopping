from django.contrib.auth.models import User
from django import forms


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

