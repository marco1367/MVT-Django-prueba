from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('cursos', cursos, name='cursos'),
    path('profesores', profesores, name='profesores'),
    path('estudiantes', estudiantes, name='estudiantes'),
    path('entregables', entregables, name='entregables'),
    path('formulario', curspFormulario, name='formulario'),
    path('formulario-profesor', profesorFormulario, name='formulario-profesor'),
]
