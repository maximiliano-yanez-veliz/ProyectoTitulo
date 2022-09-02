from pydoc import ModuleScanner
from django.contrib import admin

from PlanillaEjercicios.models import Ejercicios
from .models import Ejercicios
from django.contrib import admin



# Register your models here.
admin.site.register(Ejercicios)