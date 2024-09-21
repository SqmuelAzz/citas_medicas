import sys
import os
from unittest.mock import MagicMock
import pytest
from app.reportes import Reporte

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_guardar_reporte_citas_programadas():
    reporte = Reporte()
    reporte.db = MagicMock()  # Mockear la conexión a la base de datos

    datos = (1, '2024-09-21 10:00:00', '2024-09-21', 'Juan', 'Dr. Smith', 'General', 'Pendiente')
    reporte.guardar_reporte_citas_programadas(*datos)

    reporte.db.execute_query.assert_called_once_with(
        """INSERT INTO reportes (
            id_adm, prg_envio, fecha, paciente, medico, especialidad, estado) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", datos)

def test_guardar_reporte_citas_canceladas():
    reporte = Reporte()
    reporte.db = MagicMock()  # Mockear la conexión a la base de datos

    datos = (1, '2024-09-21 10:00:00', '2024-09-21', 'Juan', 'Dr. Smith', 'Reprogramado', 'No disponible')
    reporte.guardar_reporte_citas_canceladas(*datos)

    reporte.db.execute_query.assert_called_once_with(
        """INSERT INTO reportes (
            id_adm, prg_envio, fecha, paciente, medico, modifico, motivo) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", datos)
