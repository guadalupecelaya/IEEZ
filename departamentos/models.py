from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Departamentos(models.Model):
    nombre = models.CharField(
        'nombre',
        max_length=100,
        null=True,
        blank=True)