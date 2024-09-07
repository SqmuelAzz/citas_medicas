from database_connection import DatabaseConnection

class Medico:
    def __init__(self):
        self.db = DatabaseConnection()
    

    def crear_medico(self,medico):
        #print(paciente)
        nombre,especialidad,id_ageda,id_disponibilidad = medico
        query= """INSERT INTO medicos (
            nombre,especialidad,id_agenda,id_disponibilidad) 
            VALUES(?,?,?,?)"""
        self.db.execute_query(query, (
            nombre,
            especialidad,
            id_ageda,
            id_disponibilidad))

    def mostrar_medicos(self):
        query = "SELECT id,nombre,especialidad FROM medicos" 
        medicos = self.db.execute_query(query)
        return medicos