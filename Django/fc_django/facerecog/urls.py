# pages/urls.py

from django.urls import path
from .views import view,post


from facerecog import views

urlpatterns = [
path('form',view,name='form'),
path('post',post,name='post')
    #path('auth/login',login,name='login')
]

