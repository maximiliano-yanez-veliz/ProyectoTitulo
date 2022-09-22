
# from django.http import HttpResponse
from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import render, redirect
from .models import Ejercicios
from django.views.generic import ListView

def home(request):
    habilidListado = Ejercicios.objects.all()
    
    data = {
        'titulo':'Gestion de Ejercicios',
        'jercicio' : habilidListado

    }
    # return render(request,"gestionEjercicios.html",{"jercicio": habilidListado})
    return render(request,"gestionEjercicios.html", data)

class EjercicioListView(ListView):
    model = Ejercicios
    template_name = 'gestionEjercicios.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Ejercicios'
        return context
    
def eliminar_ejercicio(request,id):
    ejercicio = Ejercicios.objects.get(id=id)
    ejercicio.delete()
    return redirect('/')






