from ast import If
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import CursoFOrmulario, ProfesorFormulario

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

def curspFormulario(request):
    if request.method == 'POST':

        miFormulario = CursoFOrmulario(request.POST)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/inicio.html") ##Vuelvo al inicio o a donde quiera
    else:
        miFormulario = CursoFOrmulario() #formulario vacio par acontruir el html
    return render(request, "AppCoder/formulario.html", {"miFormulario":miFormulario})


def profesorFormulario(request):
    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid:
            print(miFormulario)

            informacion = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=informacion['nombre'], 
                apellido=informacion['apellido'],
                email=informacion['email'],
                profesion=informacion['profesion']
            )
            profesor.save()
            return render(request, "AppCoder/inicio.html") ##Vuelvo al inicio o a donde quiera
    else:
        miFormulario = ProfesorFormulario() #formulario vacio par acontruir el html
    return render(request, "AppCoder/formulario-profesor.html", {"miFormulario":miFormulario})


def busquedaCamada(request):
    pass