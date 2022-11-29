from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import username, items
from .forms import CreateNewList

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