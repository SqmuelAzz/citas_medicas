from app.database_connection import DatabaseConnection

class Paciente:
    def __init__(self, nombre, telefono, especialidad, email):
        self.nombre = nombre
        self.telefono = telefono
        self.especialidad = especialidad
        self.email = email
        self.db = DatabaseConnection()

    def crear_paciente(self):
        query= """INSERT INTO pacientes (
            nombre, email, telefono, direccion, preferencia_notificacion) 
            VALUES (?, ?, ?, ?, ?)"""
        self.db.execute_query(query, (
            self.nombre,
            self.email,
            self.telefono,
            "",  # Asumiendo que la dirección y medio de notificación son opcionales
            ""))  # y están pendientes de añadir a los atributos de clase.

    def mostrar_pacientes(self):
        query = "SELECT id, nombre FROM pacientes" 
        pacientes = self.db.execute_query(query)
        return pacientes
