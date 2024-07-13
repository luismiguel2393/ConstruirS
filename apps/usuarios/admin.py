from django.contrib import admin
from import_export import resources  
from import_export.admin import ImportExportModelAdmin
from .models import Usuario,TipoDocumento,Rol
from django.contrib.auth.admin import UserAdmin

class UsuarioResource(resources.ModelResource):  
    class Meta:  
        model=Usuario

class TipoDocumentoResource(resources.ModelResource):  
    class Meta:  
        model=TipoDocumento
        
class RolResource(resources.ModelResource):  
    class Meta:  
        model=Rol

class UsuarioAdmin(ImportExportModelAdmin,UserAdmin):

    model = Usuario
        
    list_display = ("numero_identificacion","nombre","correo",  "rol","is_active","is_staff")
    
    #Campos para editar
    fieldsets = (
        (None, {'fields': ('tipo_documento', 'numero_identificacion', 'correo', 'nombre', 'apellido', 'rol', 'password')}),
    )
    #Campos para crear
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('tipo_documento', 'numero_identificacion', 'correo', 'nombre', 'apellido', 'rol','password1', 'password2')}),
            )
    exclude = ("slug",)
    ordering = ("correo",)
    resource_class=UsuarioResource

admin.site.register(Usuario, UsuarioAdmin)

class TipoDocumentoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
  list_display="nombre",
  resource_class=TipoDocumentoResource
admin.site.register(TipoDocumento, TipoDocumentoAdmin)

class RolAdmin(ImportExportModelAdmin,admin.ModelAdmin):
  list_display="nombre",
  resource_class=RolResource
  
admin.site.register(Rol, RolAdmin)