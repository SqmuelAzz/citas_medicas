from database_connection import DatabaseConnection

class Medico:
    def __init__(self):
        self.db = DatabaseConnection()
    

    def crear_medico(self,medico):
        #print(paciente)
        nombre,especialidad,telefono,email = medico
        query= """INSERT INTO medicos (
            nombre,especialidad,telefono,email) 
            VALUES(?,?,?,?)"""
        self.db.execute_query(query, (
            nombre,
            especialidad,
            telefono,
            email))

    def mostrar_medicos(self):
        query = "SELECT id,nombre,especialidad FROM medicos" 
        medicos = self.db.execute_query(query)
        return medicos

    def mostrar_un_medico(self,id):
        query = "SELECT id,nombre FROM medicos WHERE id = ?"
        medico = self.db.execute_query(query,(id,))
        return medico[0]
    
    def mostrar_citas_medicas(self):
        query = """SELECT c.id,c.fecha,c.estado,m.id,m.nombre
                    FROM citas c
                    INNER JOIN  medicos m
                    ON c.id_medico = m.id 
                    WHERE c.estado = 'pendiente' """
        citas = self.db.execute_query(query)
        if citas:
            return citas
        else: 
            return None
    
    def cancelar_cita(self,datos):
        idCita,motivo,mensaje=datos
        query = "UPDATE citas SET estado = 'cancelada', motivo = ?, modificado_por = ? WHERE id = ? "
        self.db.execute_query(query, (motivo,mensaje,idCita))