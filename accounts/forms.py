from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,

    )
from django.contrib.auth import get_user_model

from django import forms
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField()
    realname = forms.CharField()
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'realname', 'password1', 'password2', )

class CustomAuthenticationForm(AuthenticationForm):
    pass
