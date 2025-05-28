import unittest
from src.modelo.declarative_base import Session, Base, engine
from src.logica.AlumnoManager import AlumnoManager

class TestAlumnoManager(unittest.TestCase):
    def setUp(self):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        self.session = Session()
        self.manager = AlumnoManager(self.session)

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_crear_alumno(self):
        alumno = self.manager.crear_alumno("Cristian Cueva")
        self.assertIsNotNone(alumno.id)
        self.assertEqual(alumno.nombre, "Cristian Cueva")

    def test_leer_alumno(self):
        alumno = self.manager.crear_alumno("Luana Armas")
        alumno_leido = self.manager.leer_alumno(alumno.id)
        self.assertEqual(alumno_leido.nombre, "Luana Armas")

    def test_actualizar_alumno(self):
        alumno = self.manager.crear_alumno("Willy")
        actualizado = self.manager.actualizar_alumno(alumno.id, "Willy Rojas")
        self.assertEqual(actualizado.nombre, "Willy Rojas")

    def test_eliminar_alumno(self):
        alumno = self.manager.crear_alumno("Alumno Eliminado")
        eliminado = self.manager.eliminar_alumno(alumno.id)
        self.assertIsNone(self.manager.leer_alumno(eliminado.id))

    def test_agregar_curso(self):
        alumno = self.manager.crear_alumno("Alumno con Curso")
        curso = self.manager.agregar_curso(alumno.id, "Programación")
        self.assertEqual(curso.nombre, "Programación")
        self.assertEqual(curso.alumno_id, alumno.id)

    def test_leer_cursos(self):
        alumno = self.manager.crear_alumno("Alumno Cursos")
        self.manager.agregar_curso(alumno.id, "Curso 1")
        self.manager.agregar_curso(alumno.id, "Curso 2")
        cursos = self.manager.leer_cursos(alumno.id)
        self.assertEqual(len(cursos), 2)
        self.assertEqual(cursos[0].nombre, "Curso 1")
        self.assertEqual(cursos[1].nombre, "Curso 2")

if __name__ == "__main__":
    unittest.main()