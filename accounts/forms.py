from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    UserChangeForm,

    )
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

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
                'id': 'nickname',
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

class CustomUserChangeForm(UserChangeForm):
    nickname = forms.CharField(
        label='Nickname',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )    
    password = None

    class Meta:
        model = User
        fields = ('nickname',)

class CheckPasswordForm(forms.Form):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 
                }
        ),
    )
    def __init__(self, user, *args, **kwargs): #?????? ???????????? ???????????? password ???????????? ?????? init ???????????? user?????? ??????
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self): #clean ???????????? form??? ????????? password?????? init?????? ????????? ?????? ???????????? password ?????? check_password ?????? ??????
        cleaned_data = super().clean()
        print(cleaned_data)
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '??????????????? ???????????? ????????????.')