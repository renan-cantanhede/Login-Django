from django.urls import path, include
from . import views
from django.contrib import admin
from .views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("Login", views.Login, name="Login"),
    path("Cadastro", views.cadastro, name="Cadastro"),
    path("Logout", views.Logout, name="Logout"),
]
