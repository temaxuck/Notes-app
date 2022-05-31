from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import logout

def register(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You have been already logged in. Log out if you want to register a new user.')
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'An account for {username} has been created!')
            return redirect('login')
    else:
        form = RegisterForm()
    
    context = {
        'form': form,
        'title': 'Register'
    }

    return render(request, 'users/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You have been already logged in. Log out if you want to change user.')
        return redirect('profile')
    
    defaults = {
        'template_name': 'users/login.html',
        'authentication_form': AuthenticationForm,
        'extra_context': {
            'title': 'Log in',
        },
    }
    return LoginView.as_view(**defaults)(request)

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Вы вышли из учётной записи.')
    return redirect('about')


@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
    
    user_update_form = UserUpdateForm(instance=request.user)
    profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form,
    }
    return render(request, 'users/profile_.html', context)

