from src.modelo.modelo import Alumno, Curso

class AlumnoManager:
    def _init_(self, session):
        self.session = session

    def crear_alumno(self, nombre):
        alumno = Alumno(nombre=nombre)
        self.session.add(alumno)
        self.session.commit()
        return alumno

    def leer_alumno(self, alumno_id):
        return self.session.query(Alumno).filter_by(id=alumno_id).first()

    def actualizar_alumno(self, alumno_id, nuevo_nombre):
        alumno = self.leer_alumno(alumno_id)
        if alumno:
            alumno.nombre = nuevo_nombre
            self.session.commit()
        return alumno

    def eliminar_alumno(self, alumno_id):
        alumno = self.leer_alumno(alumno_id)
        if alumno:
            self.session.delete(alumno)
            self.session.commit()
        return alumno

    def agregar_curso(self, alumno_id, nombre_curso):
        alumno = self.leer_alumno(alumno_id)
        if alumno:
            curso = Curso(nombre=nombre_curso, alumno=alumno)
            self.session.add(curso)
            self.session.commit()
            return curso
        return None

    def leer_cursos(self, alumno_id):
        alumno = self.leer_alumno(alumno_id)
        return alumno.cursos if alumno else None