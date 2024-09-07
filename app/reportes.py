from database_connection import DatabaseConnection

class Reporte:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def guardar_reporte_citas_programadas(self,idAdm,prg_envio,fecha,paciente,medico,especialidad,estado):
        #print(reporte)
        #idAdm,fecha,paciente,medico,especialidad,estado = reporte
        query= """INSERT INTO reportes (
            id_adm,prg_envio,fecha,paciente,medico,especialidad,estado) 
            VALUES(?,?,?,?,?,?,?)"""
        self.db.execute_query(query, (
            idAdm,
            prg_envio,
            fecha,
            paciente,
            medico,
            especialidad,
            estado))
        
    def guardar_reporte_citas_canceladas(self,idAdm,prg_envio,fecha,paciente,medico,modifico,motivo):
        #print(reporte)
        #idAdm,fecha,paciente,medico,especialidad,estado = reporte
        query= """INSERT INTO reportes (
            id_adm,prg_envio,fecha,paciente,medico,modifico,motivo) 
            VALUES(?,?,?,?,?,?,?)"""
        self.db.execute_query(query, (
            idAdm,
            prg_envio,
            fecha,
            paciente,
            medico,
            modifico,
            motivo))