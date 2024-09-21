import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.medico import Medico

def test_create_medico():
    medico = Medico('Joaquin Steven', '3155869336', 'Auxiliar', 'prueba@gmail.com')
    assert medico.nombre == 'Joaquin Steven'
    assert medico.especialidad == '3155869336'
    assert medico.telefono == 'Auxiliar'
    assert medico.email == 'prueba@gmail.com'
    







