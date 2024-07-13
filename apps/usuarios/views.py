from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect
from .models import  TipoDocumento
from apps.asesores.models import Asesor
from django.views import View  # Importa la clase View de Django para vistas genéricas basadas en clases

# Vista para el registro de administradores
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        tipo_documento = TipoDocumento.objects.all()  # Obtiene todos los tipos de documento

        return render(request, 'sesion/register.html', {'tipo_documento': tipo_documento})  # Renderiza la plantilla de registro con los tipos de documento disponibles

    def post(self, request):
        # Obtiene los datos del formulario de registro enviado mediante POST
        tipo_documento = request.POST.get('tipo_documento')
        numero_identificacion = request.POST.get('numero_identificacion')
        correo = request.POST.get('correo')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
       
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Realiza validaciones adicionales según tus necesidades
        if Asesor.objects.filter(correo=correo).exists():
            messages.error(request, 'El correo electrónico ya está en uso. Por favor, elige otro.')
            return redirect('register')  # Redirecciona de vuelta al formulario de registro
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')  # Agrega un mensaje de error si las contraseñas no coinciden
            return redirect('register')  # Redirecciona de vuelta a la página de registro

        # Convierte los ID de tipo de documento y centro a enteros
        tipo_documento_id = int(tipo_documento)
        
        # Obtiene las instancias del tipo de documento 
        tipo_documento = TipoDocumento.objects.get(pk=tipo_documento_id)
        
        # Crea un nuevo usuario (Funcionario)
        user = Asesor.objects.create_user(correo=correo, password=password1)
        user.tipo_documento = tipo_documento
        user.numero_identificacion = numero_identificacion
        user.nombre = nombre
        user.apellido = apellido
        
        # Guarda el usuario
        user.save()
        messages.success(request, f'Bienvenidos, {user.correo}!')  # Agrega un mensaje de éxito
        return redirect('login')  # Redirecciona a la página de inicio de sesión

def Login(request):
    # Obtener todos los centros y tipos de documento disponibles
    tipos_documento = TipoDocumento.objects.all()

    if request.method == 'GET':
        
        return render(request, 'sesion/login.html', {'tipo_documento': tipos_documento })
                                                    
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')  

        # Autenticar al usuario
        user = authenticate(request, correo=correo, password=password)

        if user is not None:
            # Iniciar sesión para el usuario autenticado
            login(request, user)
            # Agregar mensaje de éxito
            messages.success(request, f'Bienvenido, {user.correo.split("@")[0]}!')  # Se muestra solo el nombre de usuario
            # Obtener la URL de redirección
            next_url = request.GET.get('next', None)
            if next_url:
                return redirect(next_url)
            else:
                # Redirigir según el rol del usuario
                if user.rol.id == 1: # rol 1 = Socio (a)
                    print ("estoy aki")
                    return redirect('index')
                   
                elif user.rol.id == 2: # rol 2 = Secretaria (a)
                    return redirect('index')
        else:
            # Agregar mensaje de error en caso de autenticación fallida
            messages.error(request, 'Correo o contraseña incorrectos.')

    # Si no se ha realizado ninguna acción (GET) o la autenticación falló (POST), renderizar la página de inicio de sesión
    return render(request, 'sesion/login.html', {'tipo_documento': tipos_documento})

# Vista para cerrar sesión
# @never_cache
def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirecciona a la página de inicio de sesión