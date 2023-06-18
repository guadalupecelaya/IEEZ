from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField("Nombre", max_length=40, unique=False)
    direccion = models.CharField("Dirección", max_length=40, unique=False)
    telefono = models.IntegerField("Teléfono")
    #nombre = models.ForeignKey("materiales.TipoMaterial", verbose_name="Nombre", on_delete=models.CASCADE) 

    def __str__ (self):
        return self.nombre

    
