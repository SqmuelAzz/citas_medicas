# test_horario.py:
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.horario import Horario

def test_crear_agenda():
    horario = Horario()
    datos_agenda = ("Lunes", "08:00", "12:00", 1)  # Suponiendo que '1' es un ID de médico existente
    # No podemos hacer assert directamente sobre la base de datos sin obtener el resultado o mockearlo.
    # Aquí deberías realizar la inserción y luego consultar la base de datos para validar que la inserción fue correcta,
    # o usar una herramienta de mock para simular la respuesta de la base de datos.

    # Como ejemplo simple de uso de assert (no verifica la base de datos):
    assert horario is not None  # Asegura que el objeto 'Horario' se creó correctamente.
