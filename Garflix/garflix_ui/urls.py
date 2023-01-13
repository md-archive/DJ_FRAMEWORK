from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('browse/', views.browse, name="browse"),
    path('details/', views.details, name="details"),
    path('profile/', views.profile, name="profile"),
    path('logged/', views.logged, name="logged"),
    path('streams/', views.streams, name="streams"),
    path('signup/', views.signup, name="signup"),
]
