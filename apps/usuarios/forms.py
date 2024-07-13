from django import forms  # Importa el módulo forms de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # Importa los formularios de creación de usuario y autenticación de Django

# Importa el modelo Usuario desde el archivo models.py del directorio actual
from .models import Usuario

# Define una clase para el formulario de registro que hereda de UserCreationForm
class RegistroForm(UserCreationForm):

    # Define la clase Meta para configurar el modelo, los campos y los widgets del formulario
    class Meta:
        model = Usuario  # Utiliza el modelo Usuario
        fields = ('tipo_documento', 'numero_identificacion', 'correo', 'nombre', 'apellido', 'password1', 'password2')  # Define los campos que estarán en el formulario

# Define una clase para el formulario de inicio de sesión que hereda de AuthenticationForm
class LoginForm(AuthenticationForm):
    correo = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # Define un campo personalizado para el correo electrónico con un widget de TextInput
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # Define un campo personalizado para la contraseña con un widget de PasswordInput

    # Define la clase Meta para configurar el modelo y los campos del formulario
    class Meta:
        model = Usuario  # Utiliza el modelo Usuario
        fields = ['correo', 'password']  # Define los campos que estarán en el formulario
