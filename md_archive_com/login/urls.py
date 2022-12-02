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
    path("Ejercicio 1.1", views.ejercicio11, name="Ejercicio 1.1"),
    path("Ejercicio 1.2", views.ejercicio12, name="Ejercicio 1.2"),
    path("Ejercicio 1.3", views.ejercicio13, name="Ejercicio 1.3"),
    path("Ejercicio 1.4", views.ejercicio14, name="Ejercicio 1.4"),
    path("Ejercicio 1.5", views.ejercicio15, name="Ejercicio 1.5"),
    path("Ejercicio 1.6", views.ejercicio16, name="Ejercicio 1.6"),
    path("Ejercicio 1.7", views.ejercicio17, name="Ejercicio 1.7"),
    path("Ejercicio 1.8", views.ejercicio18, name="Ejercicio 1.8"),
    path("Ejercicio 2.1", views.ejercicio21, name="Ejercicio 2.1"),
    path("Ejercicio 2.2", views.ejercicio22, name="Ejercicio 2.2"),
    path("Ejercicio 2.3", views.ejercicio23, name="Ejercicio 2.3"),
    path("Ejercicio 2.4", views.ejercicio24, name="Ejercicio 2.4"),
    path("Ejercicio 2.5", views.ejercicio25, name="Ejercicio 2.5"),
    path("Ejercicio 2.6", views.ejercicio26, name="Ejercicio 2.6"),
    ]