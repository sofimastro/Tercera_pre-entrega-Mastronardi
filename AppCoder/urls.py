from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('curso_formulario/', views.curso_formulario, name='curso_formulario'),
    path('profesor_formulario/', views.crear_profesor, name='profesor_formulario'),
    path('estudiante_formulario/', views.crear_estudiante, name='estudiante_formulario'),
    path('entregable_formulario/', views.crear_entregable, name='entregable_formulario'),
    path('profesores/', views.profesores_list, name='profesores_list'),
    path('estudiantes/', views.estudiantes_list, name='estudiantes_list'),
    path('entregables/', views.entregables_list, name='entregables_list'),
    path('buscar/', views.buscar, name='buscar'),
]

