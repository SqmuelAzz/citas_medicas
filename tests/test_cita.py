import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.cita import Cita
from unittest.mock import MagicMock

# Crear una clase de prueba para Cita
class TestCita:
    def setup_method(self):
        # Configuración previa a cada prueba
        self.cita = Cita()
        self.cita.db = MagicMock()  # Mockear la conexión a la base de datos

    def test_crear_cita(self):
        datos = ('2024-09-21', 1, 1, 'Consulta general', 30)
        self.cita.crear_cita(datos)
        self.cita.db.execute_query.assert_called_once_with(
            """INSERT INTO citas (
            fecha,id_paciente,id_medico,detalle,duracion) 
            VALUES(?,?,?,?,?)""", datos)

    def test_mostrar_citas(self):
        self.cita.db.execute_query.return_value = [(1, 'Juan', 'Dr. Smith', 'Consulta')]
        citas = self.cita.mostrar_citas()
        assert citas == [(1, 'Juan', 'Dr. Smith', 'Consulta')]
        self.cita.db.execute_query.assert_called_once()

    def test_cancelar_cita(self):
        self.cita.cancelar_cita(1)
        self.cita.db.execute_query.assert_called_once_with(
            "UPDATE citas SET estado = 'Cancelada' WHERE id = ? ", (1,))

    def test_notificar_cita_paciente(self):
        self.cita.db.execute_query.return_value = [(1, '2024-09-21', 1, 'Juan', 'juan@example.com', '123456789', 'email')]
        notificacion = self.cita.notificar_cita_paciente(1)
        assert notificacion == (1, '2024-09-21', 1, 'Juan', 'juan@example.com', '123456789', 'email')
        self.cita.db.execute_query.assert_called_once_with(
            """SELECT c.id,c.fecha,c.id_paciente,p.nombre,p.email,p.telefono,p.preferencia_notificacion
                    FROM citas c
                    INNER JOIN  pacientes p
                    ON c.id_paciente = p.id 
                    WHERE c.id = ?""", (1,))

    def test_crear_notificacion(self):
        datos = (1, 1, 'Recordatorio de cita', 'email', 'pendiente')
        self.cita.crear_notificacion(datos)
        self.cita.db.execute_query.assert_called_once_with(
            """INSERT INTO notificaciones (
            id_paciente,id_cita,mensaje,medio,estado) 
            VALUES(?,?,?,?,?)""", datos)

    def test_cargar_una_cita(self):
        self.cita.db.execute_query.return_value = [('Dr. Smith',)]
        cita = self.cita.cargar_una_cita(1)
        assert cita == ('Dr. Smith',)
        self.cita.db.execute_query.assert_called_once_with(
            """SELECT m.nombre
                    FROM citas c
                    INNER JOIN  medicos m
                    ON c.id_medico = m.id 
                    WHERE c.id = ?""", (1,))

