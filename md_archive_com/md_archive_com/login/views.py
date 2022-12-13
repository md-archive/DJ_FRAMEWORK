from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CreateToDoList, items
from .forms import CreateNewList
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
def index(response, id):
    ls = CreateToDoList.objects.get(id=id)
    
    if ls in response.user.tdlist.all():
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
    return render(response, "login/view.html", {"ls":ls})

def home(response):
    return render(response, "login/home.html", {})

def create(response):
    
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = CreateToDoList(name=n)
            t.save()
            response.user.tdlist.add(t)
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "login/create.html", {"form":form})

def register(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()
    
    form = RegistrationForm()
    return render(response, "login/register.html", {"form": form })

def view(response):
    return render(response, "login/view.html", {})