from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    )
from django.contrib.auth import get_user_model

from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
            }
        )
    )
    nickname = forms.CharField(
        label='Nickname',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )        
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control',
            }),
    )
    password2 = forms.CharField(
        label="Password confirm",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control'
            }),
        strip=False,
    ) 
    
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'nickname', 'password1', 'password2', )


class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'id': 'username',
            },
        ),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'class': 'form-control'}),
    )


class CustomProfileForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ('nickname', 'image', )