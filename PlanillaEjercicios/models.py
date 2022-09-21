from pyexpat import model
from django.db import models

class Habilidades(models.Model):
    hablidad = models.CharField('Habilidad', max_length=200)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Ejercicio'
    
    def __str__(self):
        return str(self.id) + '-' + self.hablidad

class Ejercicios(models.Model):
    

    titulo = models.CharField('Titulo', max_length=50)
    descripcion = models.TextField('Descripcion')
    dificultad = models.CharField('Dificultad', max_length=10, default= 1)
    
    habilidades = models.ManyToManyField(
    Habilidades,
    through='HabilidadEjercicio',
    blank=True,
    )

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'
        ordering = ['-titulo']


    def __str__(self):
        return str(self.id) + '-' + self.titulo + '-'  




class HabilidadEjercicio(models.Model):
    description = models.CharField(
        'titulo',
        max_length=100,
        blank=True,
    )
    habilidades = models.ForeignKey(
        Habilidades, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    ejercicio = models.ForeignKey(
        Ejercicios, 
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    
    class meta:
        db_table = 'PlanillaEjercicios_ejercicio_habilidades'
        verbose_name = 'Habilidad Ejercicio'
        verbose_name_plural = 'Habilidades Ejercicios'
    



