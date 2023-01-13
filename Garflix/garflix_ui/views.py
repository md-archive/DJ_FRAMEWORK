from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
# from .forms import TaskForm
from .forms import RegistrationForm


def index(response):
    return render(response, "garflix_ui/base.html", {})


def browse(response):
    return render(response, "garflix_ui/browse.html", {})


def details(response):
    return render(response, "garflix_ui/details.html", {})


def streams(response):
    return render(response, "garflix_ui/stream.html", {})


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
                return HttpResponse('User created succesfully'), redirect('logged')
            except IntegrityError:
                return render(request, 'garflix_ui/profile.html', {
                    'form': RegistrationForm,
                    "error": 'User already exists'
                })

        return render(request, 'garflix_ui/profile.html', {
            'form': RegistrationForm,
            "error": 'Password do not match'
        })


'''
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()

    form = RegistrationForm()
    return render(response, "garflix_ui/profile.html", {"form": form})
'''
# MIAU MIAU NIGGA!!
# Sign Up


def logged(request):
    return render(request, 'logged.html')


def signup(request):
    return render(request, "gato")
'''
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
                return HttpResponse('User created succesfully')
            except IntegrityError:
                return render(request, 'garflix_ui/profile.html', {
                    'form': RegistrationForm,
                    "error": 'User already exists'
                })

        return render(request, 'garflix_ui/profile.html', {
            'form': RegistrationForm,
            "error": 'Password do not match'
        })



#  SignOut
@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'],
            password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('tasks')
'''
