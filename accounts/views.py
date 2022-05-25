from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from accounts.forms import  CustomUserCreationForm
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .forms import (
    CustomAuthenticationForm, 
    CustomUserChangeForm,
    CheckPasswordForm,
    )

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
            

def login(request):

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next_url = request.GET.get('next')
            return redirect(next_url or 'movies:select_mood')
    else:
        form = CustomAuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def profile(request, username):
    person = get_object_or_404(User, username=username)

    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


def update_profile(request, username):

    if request.method == 'POST':
        form1 = CustomUserChangeForm(request.POST, instance=request.user)
        password_form = CheckPasswordForm(request.user, request.POST)
        if form1.is_valid():
            if password_form.is_valid():
                updated = form1.save(commit=False)
                updated.save()
                return redirect('accounts:profile', username)
    else:
        form1 = CustomUserChangeForm(instance=request.user)
        password_form = CheckPasswordForm(request.user)
    context = {
        'form1': form1,
        'password_form': password_form,
    }
    return render(request, 'accounts/update_profile.html', context)


@login_required
def userdelete(request, username):

    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.add_message(request, messages.ERROR, '성공적으로 회원 탈퇴되었습니다! 서비스 이용을 위해 재가입해주세요')
            return redirect('accounts:signup')
    else:
        password_form = CheckPasswordForm(request.user)

    context = {
        'password_form': password_form,
        'username': username,
    }
    return render(request, 'accounts/update_profile.html', context)