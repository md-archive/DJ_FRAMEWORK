from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.login, name="login"),
    path("create", views.create, name="create"),
    path("submenu1" views.submenu1, name="submenu1"),
    path("submenu2" views.submenu2, name="submenu2"),
    path("submenu3" views.submenu3, name="submenu3"),
    path("submenu4" views.submenu4, name="submenu4"),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    path("", views., name=""),
    ]