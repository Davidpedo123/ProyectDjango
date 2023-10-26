# generador_contrasena/views.py
from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def generar_contraseña_view(request):
    if request.method == 'POST':
        longitud_contraseña = int(request.POST.get('longitud_contraseña', 12))
        contraseña_generada = generar_contraseña(longitud_contraseña)
        return render(request, 'generador_contrasena/resultado.html', {'contraseña_generada': contraseña_generada})
    return render(request, 'generador_contrasena/generador.html')
