# medico.py:
from app.database_connection import DatabaseConnection

class Medico:
    def __init__(self, nombre, especialidad, telefono, email):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.email = email
        self.db = DatabaseConnection()

    def crear_medico(self):
        query= """INSERT INTO medicos (
            nombre, especialidad, telefono, email) 
            VALUES (?, ?, ?, ?)"""
        self.db.execute_query(query, (
            self.nombre,
            self.especialidad,
            self.telefono,
            self.email))
