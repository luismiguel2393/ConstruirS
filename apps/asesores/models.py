from django.db import models
from apps.usuarios.models import Usuario

class Departamento(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "asesor_departamento"
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

class Municipio(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    departamento = models.ForeignKey(Departamento, verbose_name="Departamento", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "asesor_municipio"
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

class Asesor(Usuario):
   

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "asesor_asesor"
        verbose_name = "Asesor"
        verbose_name_plural = "Asesores"

