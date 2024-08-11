from django.test import TestCase
from .models import Curso, Profesor, Estudiante, Entregable

class CursoModelTest(TestCase):
    def setUp(self):
        Curso.objects.create(nombre="Curso 1", comision=1234)

    def test_curso_str(self):
        curso = Curso.objects.get(nombre="Curso 1")
        self.assertEqual(str(curso), "Curso 1 - 1234")
