from django.shortcuts import render, redirect
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm, SearchForm
from .models import Curso, Estudiante, Profesor, Entregable

# Vista para la página de inicio
def index(request):
    return render(request, 'AppCoder/index.html')

# Vista para crear curso
def curso_formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito (lista de cursos, por ejemplo)
            return redirect('curso_formulario')
    else:
        form = CursoForm()
    return render(request, 'AppCoder/curso_formulario.html', {'form': form})

# Vista para crear estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiantes_list')  # Redirige a la lista de estudiantes
    else:
        form = EstudianteForm()
    return render(request, 'AppCoder/estudiante_formulario.html', {'form': form})

# Vista para crear profesor
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores_list')  # Redirige a la lista de profesores
    else:
        form = ProfesorForm()
    return render(request, 'AppCoder/profesor_formulario.html', {'form': form})

# Vista para crear entregable
def crear_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entregables_list')  # Redirige a la lista de entregables
    else:
        form = EntregableForm()
    return render(request, 'AppCoder/entregable_formulario.html', {'form': form})

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
