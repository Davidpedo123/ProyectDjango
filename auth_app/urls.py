# auth_app/urls.py
from django.urls import path
from auth_app.views import *

urlpatterns = [
    path('login/', login_view, name='login_view'),
    # Otras rutas...
]