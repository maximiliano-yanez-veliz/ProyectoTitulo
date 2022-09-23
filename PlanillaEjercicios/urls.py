from django.urls import path
from PlanillaEjercicios.views import EjercicioListView, registrar_ejercicio, eliminar_ejercicio, edicion_ejercicio, editar_ejercicio, registro_ejercicio, creacion_ejercicio, habilidad_ejercicios

urlpatterns = [
    path('', EjercicioListView.as_view(), name='gestion_ejercicios'),
    path('eliminacionEjercicios/<int:id>', eliminar_ejercicio),
    path('registrarEjercicio/', registrar_ejercicio),
    path('edicionEjercicios/<int:id>', edicion_ejercicio),
    path('editarEjercicio/', editar_ejercicio),
    path('registroEjercicio/', registro_ejercicio),
    path('creacionEjercicio/', creacion_ejercicio),
    path('habilidadEjercicios/', habilidad_ejercicios),
    
]

