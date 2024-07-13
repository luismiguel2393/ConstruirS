from django.contrib import admin
from .models import Departamento, Municipio, Asesor

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Campos a mostrar en la lista de registros

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento')  # Campos a mostrar en la lista de registros
    list_filter = ('departamento',)  # Filtros laterales basados en campos

@admin.register(Asesor)
class AsesorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','tipo_documento','numero_identificacion','correo')  # Campos a mostrar en la lista de registros
    search_fields = ('nombre''numero_identificacion',)  # Campos por los que se puede buscar
