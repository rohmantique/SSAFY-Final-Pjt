from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from accounts.forms import CustomProfileForm, CustomUserCreationForm
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
)

from .models import User
from .forms import CustomAuthenticationForm

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('movies:select_mood')
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
    return redirect('movies:home')


def profile(request, username):
    person = get_object_or_404(User, username=username)
    # person = User.objects.filter(username=username)
    context = {
        'person': person,
        # 'profile_status': profile_status,
    }
    return render(request, 'accounts/profile.html', context)


def create_profile(request, username):
    if request.method == 'POST':
        form = CustomProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return redirect('accounts:profile', username)
    else:
        form = CustomProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/create_profile.html', context)


def update_profile(request, username):
    pass


def follow(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    you = request.user
    response = {
        'followed': False,
        'count': 0
    }

    if user.followers.filter(pk=you.pk).exists():
        user.followers.remove(you)
        response['followed'] = False
    else:
        user.followers.add(you)
        response['followed'] = True

    response['count'] = user.followers.count()

    return JsonResponse(response)
    


