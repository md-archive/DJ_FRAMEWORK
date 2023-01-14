from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# from .forms import TaskForm
from .forms import RegistrationForm
# miau
from django.contrib.auth.decorators import login_required


def index(response):
    return render(response, "garflix_ui/base.html", {})


def browse(response):
    return render(response, "garflix_ui/browse.html", {})


def details(response):
    return render(response, "garflix_ui/details.html", {})


def streams(response):
    return render(response, "garflix_ui/streams.html", {})


def profile(request):
    if request.method == 'GET':
        return render(request, 'garflix_ui/profile.html', {
            'form': RegistrationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(logged)
            except IntegrityError:
                return render(request, 'garflix_ui/profile.html', {
                    'form': RegistrationForm,
                    "error": 'User already exists'
                })

        return render(request, 'garflix_ui/profile.html', {
            'form': RegistrationForm,
            "error": 'Password do not match'
        })


@login_required
def signout(request):
    logout(request)
    return redirect('/browse')


def loginX(request):
    if request.method == 'GET':
        return render(request, 'garflix_ui/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],
            password=request.POST['password'])

        if user is None:
            return render(request, 'garflix_ui/login.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect(profile)


# MIAU MIAU NIGGA!!


def signup(request):
    return render(request, "gato")
