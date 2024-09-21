import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.paciente import Paciente
from app.database_connection import DatabaseConnection  

def test_create_paciente():
    paciente = Paciente('Joaquin Steven', '3155869336', 'Auxiliar', 'prueba@gmail.com')
    assert paciente.nombre == 'Joaquin Steven'
    assert paciente.telefono == '3155869336'
    assert paciente.especialidad == 'Auxiliar'
    assert paciente.email == 'prueba@gmail.com'
