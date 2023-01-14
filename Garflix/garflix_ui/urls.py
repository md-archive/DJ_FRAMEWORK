from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('browse/', views.browse, name="browse"),
    path('details/', views.details, name="details"),
    path('profile/', views.profile, name="profile"),
    path('loginX/', views.loginX, name="loginX"),
    path('signout/', views.signout, name="signout"),
    path('streams/', views.streams, name="streams"),
]
