from database_connection import DatabaseConnection

class Cita:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def crear_cita(self,datos):
        fecha,idPaciente,idMedico,motivo,duracion = datos
        query= """INSERT INTO citas (
            fecha,id_paciente,id_medico,detalle,duracion) 
            VALUES(?,?,?,?,?)"""
        self.db.execute_query(query, (
            fecha,
            idPaciente,
            idMedico,
            motivo,
            duracion))
    
    def mostrar_citas(self):
        query = """SELECT c.id,p.nombre,m.nombre,c.detalle
                    FROM medicos m, citas c
                    INNER JOIN  pacientes p
                    ON c.id_paciente = p.id 
                    AND c.id_medico = m.id
                    WHERE estado = 'pendiente'"""
        citas = self.db.execute_query(query)
        if citas:
            return citas
        else: 
            return None
    
    def cancelar_cita(self,id):
        query = "UPDATE citas SET estado = 'Cancelada' WHERE id = ? "
        self.db.execute_query(query, (id,))
    
    def notificar_cita_paciente(self,id):
        query = """SELECT c.id,c.fecha,c.id_paciente,p.nombre,p.email,p.telefono,p.preferencia_notificacion
                    FROM citas c
                    INNER JOIN  pacientes p
                    ON c.id_paciente = p.id'"""
        citas = self.db.execute_query(query)
        if citas:
            return citas
        else: 
            return None 