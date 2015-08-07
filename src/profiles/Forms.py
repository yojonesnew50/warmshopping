from django import forms
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.conf.global_settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage

class LoginForm(forms.Form):
    
    username =forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)