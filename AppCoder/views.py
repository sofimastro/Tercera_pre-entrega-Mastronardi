from django.shortcuts import render, redirect
from .models import Curso, Profesor, Estudiante, Entregable
from .forms import CursoForm

def index(request):
    return render(request, 'AppCoder/index.html')

def curso_formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'AppCoder/curso_formulario.html', {'form': form})

def profesores_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'AppCoder/profesores_list.html', {'profesores': profesores})

def estudiantes_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/estudiantes_list.html', {'estudiantes': estudiantes})

def entregables_list(request):
    entregables = Entregable.objects.all()
    return render(request, 'AppCoder/entregables_list.html', {'entregables': entregables})

