from django import forms
from .models import Curso, Estudiante, Profesor, Entregable

# Formulario para el modelo Curso
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada', 'comision']

# Formulario para el modelo Estudiante
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

# Formulario para el modelo Profesor
class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']

# Formulario para el modelo Entregable
class EntregableForm(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_de_entrega', 'entregado']

# Formulario para buscar datos en la base de datos
class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)


