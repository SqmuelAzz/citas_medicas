from database_connection import DatabaseConnection

class Paciente:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def crear_paciente(self,paciente):
        #print(paciente)
        nombre,email,telefono,direccion,medio_notificacion = paciente
        query= """INSERT INTO pacientes (
            nombre,email,telefono,direccion,preferencia_notificacion) 
            VALUES(?,?,?,?,?)"""
        self.db.execute_query(query, (
            nombre,
            email,
            telefono,
            direccion,
            medio_notificacion))
    
    def mostrar_pacientes(self):
        query = "SELECT id,nombre FROM pacientes" 
        pacientes = self.db.execute_query(query)
        return pacientes
