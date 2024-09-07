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
    
    def generar_reporte_citas_programadas(self):
        query = """
            SELECT c.fecha,p.nombre,m.nombre,m.especialidad,c.estado
            FROM citas c, pacientes p
            INNER JOIN medicos m
            ON c.id_paciente = p.id
            AND c.id_medico = m.id
            """
        reporte = self.db.execute_query(query)
        return reporte
    
    def generar_reporte_citas_canceladas(self):
        query = """
            SELECT c.fecha,p.nombre,m.nombre,c.modificado_por,c.motivo
            FROM citas c, pacientes p
            INNER JOIN medicos m
            ON c.id_paciente = p.id
            AND c.id_medico = m.id
            WHERE estado = 'cancelada'
            """
        reporte = self.db.execute_query(query)
        return reporte