
# from django.http import HttpResponse
from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import render, redirect
from .models import Ejercicios, HabilidadEjercicio, Habilidades
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

def registrar_ejercicio(request):
    titulo=request.POST['txtTitulo']
    descripcion=request.POST['txtDescripcion']
    dificultad=request.POST['numDificultad']
    
    ejercicio=Ejercicios.objects.create(titulo=titulo, descripcion=descripcion, dificultad=dificultad)
    return redirect('/')

def eliminar_ejercicio(request,id):
    ejercicio = Ejercicios.objects.get(id=id)
    ejercicio.delete()
    return redirect('/')

def edicion_ejercicio(request,id):
    ejercicio = Ejercicios.objects.get(id=id)
    data = {
        'titulo':'Edicion de Ejercicios',
        'ejercicio' : ejercicio

    }
    return render(request,"edicionEjercicios.html", data)

def editar_ejercicio(request):
    id =int(request.POST['id'])
    titulo=request.POST['txtTitulo']
    descripcion=request.POST['txtDescripcion']
    dificultad=request.POST['numDificultad']
    
    ejercicio = Ejercicios.objects.get(id=id)
    ejercicio.titulo=titulo
    ejercicio.descripcion=descripcion
    ejercicio.dificultad=dificultad
    ejercicio.save()
    
    return redirect('/')

def registro_ejercicio(request):
    data = {
        'titulo':'Edicion de Ejercicios',

    }
    return render(request,"registroEjercicio.html")

def creacion_ejercicio(request):
    titulo=request.POST['txtTitulo']
    descripcion=request.POST['txtDescripcion']
    dificultad=request.POST['numDificultad']
    
    ejercicio=Ejercicios.objects.create(titulo=titulo, descripcion=descripcion, dificultad=dificultad)
    return redirect('/')

def habilidad_ejercicios(request):
    habilidListado = Habilidades.objects.all()
    
    data = {
        'titulo':'Gestion de Habilidades',
        'jercicio' : habilidListado

    }
    # return render(request,"gestionEjercicios.html",{"jercicio": habilidListado})
    return render(request,"habilidadesEjercicios.html", data)
class HabilidadesListView(ListView):
    model = Habilidades
    template_name = 'gestionEjercicios.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Ejercicios'
        return context