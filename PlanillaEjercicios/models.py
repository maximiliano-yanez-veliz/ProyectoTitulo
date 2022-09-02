from django.db import models


# Create your models here.

class Ejercicios(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50 )
    descripcion = models.TextField('Descripcion')
    