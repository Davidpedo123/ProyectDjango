from django.shortcuts import render
from django.http import HttpResponse as HR
from isort import code
from Generate.views import generar_contraseña


# Create your views here.
def hola(request):
    return HR("<h1/>Hola bro</h1>")

def simple(request):
    return render(request,'simple.html')

def index(request):
    return HR("¡Hola, mundo!")

def dinamico(request, name):
    categories = {'code', 'desing', 'marketing'}
    context = {'name': name, 'categories' : categories}
    return render(request, 'dinamico.html', context)

def estaticos(request):
    return render(request, 'estaticos.html')  

def login(request):
    return render(request, 'login.html')  

def index1(request):
    return render(request, 'index.html')  
def mi_vista(request):
    print("La vista está siendo alcanzada.")
    contraseña_generada = None

    if request.method == 'POST' and 'generar_contraseña' in request.POST:
        longitud_contraseña = int(request.POST.get('longitud_contraseña', 12))
        contraseña_generada = generar_contraseña(longitud_contraseña)

    # Independientemente de si se procesó el formulario o no, renderiza la vista
    if contraseña_generada:
        print("Resultado hecho")
        return render(request, 'resultado.html', {'contraseña_generada': contraseña_generada})
    else:
        return render(request, 'generador.html')
