from src.modelo.declarative_base import Session, Base, engine
from src.logica.AlumnoManager import AlumnoManager

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()
manager = AlumnoManager(session)

# Crear alumnos
alumno1 = manager.crear_alumno("Carlos Tovar")
alumno2 = manager.crear_alumno("Alex Cueva")

# Agregar cursos
manager.agregar_curso(alumno1.id, "Redes y computadores")
manager.agregar_curso(alumno2.id, "Construcción de software")
manager.agregar_curso(alumno2.id, "Conmutación y enrutamiento")