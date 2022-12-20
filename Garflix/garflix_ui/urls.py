from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('browse/', views.browse, name="browse"),
    path('details/', views.details, name="details"),
    path('profile/', views.profile, name="profile"),
    path('streams/', views.streams, name="streams"),
]
