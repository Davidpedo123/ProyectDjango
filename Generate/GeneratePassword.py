import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    longitud_contraseña = int(input("Ingrese la longitud de la contraseña deseada: "))
    
    if longitud_contraseña <= 0:
        print("Por favor, ingrese una longitud válida.")
    else:
        contraseña_generada = generar_contraseña(longitud_contraseña)
        print(f"Contraseña generada: {contraseña_generada}")
