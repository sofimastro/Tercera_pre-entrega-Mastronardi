from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),
    path('curso-formulario/', views.curso_formulario, name="CursoFormulario"),
]
