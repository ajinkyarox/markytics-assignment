# pages/urls.py

from django.urls import path
from .views import view

from facerecog import views

urlpatterns = [
path('form',view,name='form')
    #path('auth/login',login,name='login')
]

