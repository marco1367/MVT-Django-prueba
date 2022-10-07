from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def add_curso(request):

    curso = Curso(nombre="Data Science", camada=50)
    curso.save()

    return HttpResponse(f'creamos el curso: <br> nombre: {curso.nombre} <br> camada: {curso.camada}')
