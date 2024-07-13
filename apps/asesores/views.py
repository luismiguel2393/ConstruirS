# Importaciones de Django

from django.views.generic import TemplateView  # Importa la clase View para crear vistas basadas en clases
from django.shortcuts import render, redirect, get_object_or_404  # Importa funciones para renderizar plantillas, redirigir y obtener objetos de la base de datos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Importa clases para facilitar la paginación de resultados de consulta
from django.db.models import Q  # Importa el objeto Q para realizar consultas complejas
from django.contrib import messages  # Importa la función messages para mostrar mensajes de error, éxito, etc.

# Importaciones de la aplicación local
#from .forms import InventarioForm  # Importa el formulario necesario desde el archivo forms.py en el mismo directorio
#from .models import Inventario  # Importa el modelo necesario desde el archivo models.py en el mismo directorio


# Otras importaciones
import pandas as pd  # Importa la librería pandas para el manejo de datos tabulares
from django.utils.decorators import method_decorator  # Importa el decorador method_decorator para modificar el comportamiento de métodos de clase
from django.views.decorators.cache import never_cache  # Importa el decorador never_cache para evitar el almacenamiento en caché de la vista
from django.contrib.auth.mixins import LoginRequiredMixin  # Importa la clase LoginRequiredMixin para requerir autenticación del usuario
from django.urls import reverse_lazy


# Define la vista de inicio para el experto
# El siguiente decorador se aplica al método dispatch(),
    # asegurando que las respuestas de las solicitudes HTTP no se almacenen en caché.
    # Esto es importante para garantizar que cada solicitud reciba la información más reciente.
@method_decorator(never_cache, name='dispatch')
class homeView(LoginRequiredMixin,TemplateView):
    template_name = 'base_web/body.html'  # Nombre del template para la vista

    def get(self, request, *args, **kwargs):
        # Realiza cualquier lógica adicional aquí si es necesario
        return super().get(request, *args, **kwargs)