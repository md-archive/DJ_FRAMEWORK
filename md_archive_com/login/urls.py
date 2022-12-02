from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.signin, name="login"),
    path("create", views.create, name="create")
    ]
