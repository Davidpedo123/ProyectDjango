from django.contrib import admin
from django.urls import path
from flask.views import View
from myapp.views import mi_vista
from myapp.views import cal
from myapp.views import Envivo
from myapp.views import MapsApi
from . import views

urlpatterns = [
  
    path('', views.index1, name='index'),
    path('Home/', views.hola),
    path('Web/', views.simple),
    path('Dinamico/<str:name>', views.dinamico, name='dinamico' ),
    path('Estaticos', views.estaticos), 
    path('Login', views.login),
    path('index', views.index),
    path('Generate/', mi_vista, name='mi_vista'),
    path('cal/', cal, name='cal'),
    path('Stream/', Envivo, name='Envivo'),
    path('Maps/', MapsApi, name='MapsApi'),
    

]
