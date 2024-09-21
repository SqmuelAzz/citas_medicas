# horario.py:
from app.database_connection import DatabaseConnection

class Horario:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def crear_agenda(self, datos):
        dia, hora_inicio, hora_fin, idMedico = datos
        query = """INSERT INTO horario (
            dia, hora_inicio, hora_fin, id_medico) 
            VALUES (?, ?, ?, ?)"""
        self.db.execute_query(query, (
            dia,
            hora_inicio,
            hora_fin,
            idMedico))
