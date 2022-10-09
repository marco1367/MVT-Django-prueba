from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

# def add_curso(request):

#     curso = Curso(nombre="Data Science", camada=50)
#     curso.save()

#     return HttpResponse(f'creamos el curso: <br> nombre: {curso.nombre} <br> camada: {curso.camada}')

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def cursos(request):
    # return HttpResponse('vista cursos')
    return render(request, "AppCoder/cursos.html")


def profesores(request):
    return render(request, "AppCoder/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder/entregables.html")
