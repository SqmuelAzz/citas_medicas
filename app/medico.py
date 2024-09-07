from database_connection import DatabaseConnection

class Medico:
    def __init__(self):
        self.db = DatabaseConnection()
    



    def mostrar_medicos(self):
        query = "SELECT id,nombre,especialidad FROM medicos" 
        medicos = self.db.execute_query(query)
        return medicos