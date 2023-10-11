from django.contrib import admin
from django.urls import path, include
from myapp.views import simple

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('auth/', include('auth_app.urls')),  # Usé 'auth/' como ejemplo, ajusta según tus preferencias.
    path('Web/', simple),
]
