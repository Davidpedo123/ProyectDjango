from django.shortcuts import render
from django.http import HttpResponse as HR
from isort import code

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
