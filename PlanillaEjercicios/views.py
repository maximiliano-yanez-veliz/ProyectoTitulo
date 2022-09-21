
# from django.http import HttpResponse
from django.shortcuts import render
from .models import Habilidades

def home(request):
    habilidListado = Habilidades.objects.all()
    return render(request,"gestionEjercicios.html",{"jercicio": habilidListado})