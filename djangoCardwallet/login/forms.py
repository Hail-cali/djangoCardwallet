#login/forms.py

from django import forms
from cardwallet.models import Userinfo
from django.contrib.auth.models import User

class Authen(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ('u_name', 'pwd')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']