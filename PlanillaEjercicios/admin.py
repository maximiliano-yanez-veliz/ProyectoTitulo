from pydoc import ModuleScanner
from django.contrib import admin

from PlanillaEjercicios.models import Ejercicios
from .models import Ejercicios, Habilidades, HabilidadEjercicio
from django.contrib import admin

class HabilidadEjercicioInline(admin.TabularInline):
    model = HabilidadEjercicio
    extra = 1
    autocomplete_fields = ['habilidades']

class HabilidadesAdmin(admin.ModelAdmin):
    inlines = (HabilidadEjercicioInline,)
    search_fields = ('hablidad'),
    ordering = ['hablidad']

class EjercicioAdmin(admin.ModelAdmin):
    inlines = [HabilidadEjercicioInline,]
    list_display = (
        'titulo',
        'subtitulo',
        'descripcion',
    )
    #


# Register your models here.
admin.site.register(Habilidades, HabilidadesAdmin)
admin.site.register(Ejercicios,EjercicioAdmin)