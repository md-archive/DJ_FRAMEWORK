from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import username, items
from .forms import CreateNewList
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def index(response, id):
    ls = username.objects.get(id=id)
    
    if response.method == "POST":
        if response.POST.get("save"):
            for items in ls.items_set.all():
                if response.POST.get("c" + str(items.id)) == "clicked":
                    items.complete = True
                else:
                    items.complete = False
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            
            if len(txt) > 2:
                ls.items_set.create(text=txt, complete=False)
            else:
                print("Incomplete")
    return render(response, "login/list.html", {"ls":ls})

def home(response):
    return render(response, "login/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = username(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "login/create.html", {"form":form})


# miau
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'La contraseña no coincide'
        })


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
