from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.login, name="login"),
    path("create", views.create, name="create"),
    path("submenu1", views.submenu1, name="submenu1"),
    path("submenu2", views.submenu2, name="submenu2"),
    path("submenu3", views.submenu3, name="submenu3"),
    path("submenu4", views.submenu4, name="submenu4"),
    path("", views., name="Ejercicio 1.1"),
    path("", views., name="Ejercicio 1.2"),
    path("", views., name="Ejercicio 1.3"),
    path("", views., name="Ejercicio 1.4"),
    path("", views., name="Ejercicio 1.5"),
    path("", views., name="Ejercicio 1.6"),
    path("", views., name="Ejercicio 1.7"),
    path("", views., name="Ejercicio 1.8"),
    path("", views., name="Ejercicio 2.1"),
    path("", views., name="Ejercicio 2.2"),
    path("", views., name="Ejercicio 2.3"),
    path("", views., name="Ejercicio 2.4"),
    path("", views., name="Ejercicio 2.5"),
    path("", views., name=""),
    ]