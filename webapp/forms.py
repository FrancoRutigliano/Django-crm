from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

# Registros de usuarios y creacion de usuarios


class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# Logeo de usuarios

class LoginForm(forms.Form):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
