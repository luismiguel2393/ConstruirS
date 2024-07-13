from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  # Importa las clases AbstractBaseUser y PermissionsMixin
from django.db import models  # Importa el módulo models de Django
from .managers import CustomUserManager  # Importa el administrador personalizado de usuario
from django.db.models.signals import post_save  # Importa la señal post_save
from django.dispatch import receiver  # Importa el decorador receiver
from django.contrib.auth.models import Group  # Importa el modelo Group de usuarios
from django.utils.text import slugify  # Importa la función slugify para crear slugs

# Define el modelo TipoDocumento
class TipoDocumento(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)  # Define el campo nombre como CharField

    def __str__(self):
        return self.nombre  # Devuelve el nombre del tipo de documento como representación en cadena

    class Meta:
        db_table = "usuarios.TipoDocumento"  # Define el nombre de la tabla en la base de datos
        verbose_name = "Tipo de documento"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "Tipos de documentos"  # Define el nombre plural del modelo para la interfaz de administración

# Define el modelo Rol
class Rol(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)  # Define el campo nombre como CharField

    def __str__(self):
        return self.nombre  # Devuelve el nombre del rol como representación en cadena

    class Meta:
        db_table = "usuarios.Rol"  # Define el nombre de la tabla en la base de datos
        verbose_name = "Rol"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "Roles"  # Define el nombre plural del modelo para la interfaz de administración

# Define el modelo Usuario que hereda de AbstractBaseUser y PermissionsMixin
class Usuario(AbstractBaseUser, PermissionsMixin):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, blank=True)  # Define una relación ForeignKey con el modelo TipoDocumento
    numero_identificacion = models.CharField(max_length=255, unique=True, null=True, blank=True)  # Define el campo numero_identificacion como CharField
    correo = models.EmailField(unique=True)  # Define el campo correo como EmailField
    nombre = models.CharField(max_length=30)  # Define el campo nombre como CharField
    apellido = models.CharField(max_length=30)  # Define el campo apellido como CharField
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Define el campo fecha_creacion como DateTimeField
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Define el campo fecha_actualizacion como DateTimeField
    slug = models.SlugField(unique=True)  # Define el campo slug como SlugField
    archivo_excel = models.FileField(upload_to='archivos_excel/', blank=True, null=True)  # Define el campo archivo_excel como FileField

    # Acceso
    is_active = models.BooleanField("Habilitado", default=True)  # Define el campo is_active como BooleanField
    is_staff = models.BooleanField("Administrador", default=False)  # Define el campo is_staff como BooleanField

    # Relaciones
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True, default=2)  # Define una relación ForeignKey con el modelo Rol
    foto_perfil = models.ImageField('Foto de perfil', upload_to='usuario/perfil', null=True, blank=True)  # Define el campo foto_perfil como ImageField
    objects = CustomUserManager()  # Asigna el administrador personalizado CustomUserManager a objects

    USERNAME_FIELD = 'correo'  # Define el campo USERNAME_FIELD como 'correo'
    REQUIRED_FIELDS = ['numero_identificacion', 'nombre', 'apellido']  # Define los campos requeridos para la creación del usuario

    def __str__(self):
        return self.correo  # Devuelve el correo del usuario como representación en cadena

    class Meta:
        db_table = "usuarios.Usuario"  # Define el nombre de la tabla en la base de datos
        verbose_name = "Usuario"  # Define el nombre singular del modelo para la interfaz de administración
        verbose_name_plural = "Usuarios"  # Define el nombre plural del modelo para la interfaz de administración

    # Método para generar slugs únicos
    def save(self, *args, **kwargs):
        if not self.slug:
            campos_para_slug = f"{self.nombre} {self.apellido}"  # Concatenar los campos deseados
            self.slug = self.generate_unique_slug(campos_para_slug)
        super().save(*args, **kwargs)

    def generate_unique_slug(self, campos_para_slug):
        slug = slugify(campos_para_slug)
        nuevo_slug = slug
        contador = 1

        # Verifica si ya existe un slug con el mismo nombre en la base de datos
        while Usuario.objects.filter(slug=nuevo_slug).exclude(id=self.id).exists():
            nuevo_slug = f"{slug}-{contador}"
            contador += 1
        
        return nuevo_slug
        
