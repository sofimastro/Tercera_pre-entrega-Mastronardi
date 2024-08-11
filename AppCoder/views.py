from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor, Entregable

def inicio(request):
    return HttpResponse("Vista inicio")

def cursos(request):
    return HttpResponse("Vista cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")

def curso_formulario(request):
    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        curso.save()
        return render(request, "AppCoder/index.html")
    return render(request, "AppCoder/curso_formulario.html")

