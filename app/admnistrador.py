from database_connection import DatabaseConnection

class Administrador:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def crear_administrador(self,adm):
        #print(paciente)
        nombre,email,telefono,cargo = adm
        query= """INSERT INTO administrador (
            nombre,email,telefono,cargo) 
            VALUES(?,?,?,?)"""
        self.db.execute_query(query, (
            nombre,
            email,
            telefono,
            cargo))
    
    def mostrar_administradores(self):
        query = "SELECT id,nombre FROM administrador" 
        administradores = self.db.execute_query(query)
        return administradores