from django.contrib import admin
from django.urls import path
from flask.views import View
from . import views

urlpatterns = [
  
    path('', views.index, name='index'),
    path('Home/', views.hola),
    path('Web/', views.simple),
    path('Dinamico/<str:name>', views.dinamico, name='dinamico' ),
    path('Estaticos', views.estaticos), 
    path('Login', views.login)
]
