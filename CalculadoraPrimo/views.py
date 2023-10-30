from django.shortcuts import render

# Create your views here.
def calculadora(num):
    num = int(input("Ingrese el numero: "))
    if (( num % 2) == 0):
        print("no es primo: ")
    else:
            print("es primo")