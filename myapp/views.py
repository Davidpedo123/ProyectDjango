from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.http import HttpResponse as HR
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from isort import code
from Generate.views import generar_contraseña
from CalculadoraPrimo.views import calculadora
from Stream.views import video_stream
from clima.views import clima


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
def cal(request):
    resultado = None

    if request.method == 'POST':
        num = int(request.POST.get('numero', 0))

        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    resultado = f'{num} no es primo'
                    break
            else:
                resultado = f'{num} es primo'

    return render(request, 'calculadora.html', {'resultado': resultado})

@csrf_exempt
@gzip.gzip_page
def Envivo(request):
    return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')
def MapsApi(request):
    return render(request, 'Maps.html')

def Clima(request):
    mapa_del_clima = clima()
    
    return render(request, 'clima.html', {'mapa_del_clima': mapa_del_clima})
def React(request):
    return render(request, 'contador.html')