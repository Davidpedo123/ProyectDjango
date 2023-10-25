from django.shortcuts import render
from django.http import HttpResponse as HR
# Create your views here.
def hola(request):
    return HR("<h1/>Hola bro</h1>")
def simple(request):
    return render(request,'mysite\Templates\simple.html')
