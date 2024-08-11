from django.shortcuts import render, redirect
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm, SearchForm
from .models import Curso, Estudiante, Profesor, Entregable

# Vista para crear objetos
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_cursos')  # Redirige a una página de listado de cursos
    else:
        form = CursoForm()
    return render(request, 'AppCoder/crear_curso.html', {'form': form})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_estudiantes')  # Redirige a una página de listado de estudiantes
    else:
        form = EstudianteForm()
    return render(request, 'AppCoder/crear_estudiante.html', {'form': form})

def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_profesores')  # Redirige a una página de listado de profesores
    else:
        form = ProfesorForm()
    return render(request, 'AppCoder/crear_profesor.html', {'form': form})

def crear_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_entregables')  # Redirige a una página de listado de entregables
    else:
        form = EntregableForm()
    return render(request, 'AppCoder/crear_entregable.html', {'form': form})

def curso_formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito
    else:
        form = CursoForm()
    
    return render(request, 'AppCoder/curso_formulario.html', {'form': form})

# Vista para buscar objetos
def buscar(request):
    form = SearchForm(request.GET)
    results = {
        'cursos': [],
        'estudiantes': [],
        'profesores': [],
        'entregables': []
    }
    if form.is_valid():
        query = form.cleaned_data['query']
        results = {
            'cursos': Curso.objects.filter(nombre__icontains=query),
            'estudiantes': Estudiante.objects.filter(nombre__icontains=query),
            'profesores': Profesor.objects.filter(nombre__icontains=query),
            'entregables': Entregable.objects.filter(nombre__icontains=query)
        }
    return render(request, 'AppCoder/buscar.html', {'form': form, 'results': results})

def index(request):
    return render(request, 'AppCoder/index.html')

# Vista para listar profesores
def profesores_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'AppCoder/profesores_list.html', {'profesores': profesores})

# Vista para listar estudiantes
def estudiantes_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/estudiantes_list.html', {'estudiantes': estudiantes})

# Vista para listar entregables
def entregables_list(request):
    entregables = Entregable.objects.all()
    return render(request, 'AppCoder/entregables_list.html', {'entregables': entregables})
