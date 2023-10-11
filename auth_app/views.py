from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser  # Asegúrate de importar tu modelo CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página deseada después de iniciar sesión
            return redirect('login_view')
        else:
            # Crear un nuevo usuario si la autenticación falla
            new_user = CustomUser.objects.create_user(
                email=username,
                password=password,
                # Puedes agregar aquí los demás campos que quieras guardar
            )
            new_user.save()
            return redirect('login_view')  # Redirige a la página que quieras después de registrar al usuario
    elif request.method == 'GET':
        # Manejar el caso en que la solicitud es GET
        return render(request, 'login.html')
