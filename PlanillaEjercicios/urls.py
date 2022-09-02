from django.urls import path
from .views import EjercicioDetalladoView, EjerciciosListView


urlpatterns = [
    path('ejercicios/', EjerciciosListView.as_view(), name='ejercicios_list'),
    path('ejercicios/<int:pk>', EjercicioDetalladoView.as_view(), name='ejercicios_process')
     
    
]