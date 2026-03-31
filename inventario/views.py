from django.http import HttpResponse
from django.shortcuts import render
from  .models import Categoria
# Create your views here.

def index(request):
  return HttpResponse("Hola Mundo")

def contact(request, name):
  return HttpResponse(f"Hola {name} bienvenido a la clase django")

def categorias(request):
  categorias = Categoria.objects.all()
  return render(request, 'form_categorias.html', {
    "categorias": categorias
  })

 