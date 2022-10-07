from django.urls import path
from PlanillaEjercicios.views import EjercicioListView, eliminar_ejercicio,creacion_ejercicio,registro_ejercicio,editar_ejercicio,ejercicio,ver_ejercicio

urlpatterns = [
    path('', EjercicioListView.as_view(), name='gestion_ejercicios'),
    path('ejercicio/editarEjercicio/<int:ejercicio_id>', editar_ejercicio,name="editar_ejercicio"),
    path('ejercicio/verEjercicio/<int:ejercicio_id>', ver_ejercicio, name="ver_ejercicio"),
    path('ejercicio/', ejercicio, name="ejercicio"),
    path('registroEjercicio/', registro_ejercicio, name="registroEjercicio"),
    path('eliminar_ejercicio/<int:ejercicio_id>', eliminar_ejercicio, name="eliminar_ejercicio"),
    path('creacionEjercicio/', creacion_ejercicio),
]

