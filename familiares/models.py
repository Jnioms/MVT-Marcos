from statistics import mode
from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length=20)
    hijos = models.IntegerField()
    fecha_nac = models.DateField()