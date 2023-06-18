from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Producto(models.Model):
    #nombre = models.CharField("Nombre", max_length=30, unique=False)
    nombre = models.ForeignKey(
        "productos.TipoProducto",
        verbose_name="Nombre",
        on_delete=models.CASCADE)
    precio = models.DecimalField(
        'Precio',
        max_digits=6,
        decimal_places=2,
        validators=[
            MinValueValidator(0)])
    cantidad = models.PositiveIntegerField('Cantidad', default=1)
    descripcion = models.CharField(
        'Descripción',
        max_length=50,
        null=True,
        blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    #def get_precio_total(self):
    #s    return cantidad * precio


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)

    DISPONIBLE_CHOICES = [
        ('Disponible', 'D'),
        ('No disponible','ND'),
    ]
    disponibilidad = models.CharField(
        "Disponibilidad",
        max_length=20,
        choices=DISPONIBLE_CHOICES,
    )

    def __str__(self):
        return self.nombre
