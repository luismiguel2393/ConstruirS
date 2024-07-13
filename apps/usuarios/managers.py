from django.contrib.auth.models import BaseUserManager  # Importa la clase BaseUserManager de Django
from django.utils.crypto import get_random_string  # Importa la función get_random_string de Django para generar cadenas aleatorias

# Define el administrador personalizado CustomUserManager que hereda de BaseUserManager
class CustomUserManager(BaseUserManager):
    # Método para crear un usuario
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError("El campo correo debe establecerse")  # Lanza un ValueError si no se proporciona el correo
        correo = self.normalize_email(correo)  # Normaliza el correo electrónico
        user = self.model(correo=correo, **extra_fields)  # Crea una instancia del modelo de usuario con el correo electrónico y campos adicionales
        if password:
            user.set_password(password)  # Establece la contraseña del usuario si se proporciona
        else:
            password = get_random_string(length=12)  # Genera una contraseña aleatoria si no se proporciona
        user.save(using=self._db)  # Guarda el usuario en la base de datos
        return user  # Devuelve el usuario creado

    # Método para crear un superusuario
    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # Establece is_staff como True por defecto para el superusuario
        extra_fields.setdefault('is_superuser', True)  # Establece is_superuser como True por defecto para el superusuario
        # Obtén una instancia válida del modelo Rol (supongamos que el rol de administrador tiene ID 1)
        from .models import Rol
        admin_rol = Rol.objects.get(pk=1)
        extra_fields.setdefault('rol', admin_rol)  # Establece el rol del superusuario como el rol de administrador
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')  # Lanza un ValueError si is_staff no es True
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')  # Lanza un ValueError si is_superuser no es True
        return self.create_user(correo, password, **extra_fields)  # Crea un usuario con los campos proporcionados y devuelve el usuario creado
