import sqlite3

class Create_db:
    def __init__(self):
        self.conexion = sqlite3.connect('citas_medicas.sqlite3')
        self.cursor = self.conexion.cursor()
    
    
    def Crear_Tablas(self):
        resp = input("Desea crear la estructura de la base de datos, se elliminaran todos los datos existentes, <S/N>: ")
        if resp.upper() == 'S':
            print("Creando estructura de la base de datos BIBLIOTECA")
            print()
            print("Creando tabala usuarios ...")
            #self.cursor.execute("""
            #    DROP TABLE IF EXISTS pacientes;
            #""")

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS pacientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL,
                telefono TEXT NOT NULL,
                direccion TEXT,
                preferencia_notificacion TEXT NOT NULL,
                fecha_creacion date DEFAULT (DATE('now'))
                );
            """)

            print()
            print("Creando tabala medicos ...")
            #self.cursor.execute("""
            #    DROP TABLE IF EXISTS medicos;
            #""")

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS medicos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                especialidad TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT
                );
            """)
            print()
            print("Creando tabala citas ...")
            #self.cursor.execute("""
            #    DROP TABLE IF EXISTS citas;
            #""")

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS citas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha  date DEFAULT (DATE('now')),
                id_paciente INTEGER NOT NULL,
                id_medico INTEGER NOT NULL,
                detalle TEXT,
                estado TEXT NOT NULL DEFAULT 'pendiente',
                duracion INTEGER NOT NULL,
                fecha_creacion date DEFAULT (DATE('now')),
                FOREIGN KEY (id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY (id_medico) REFERENCES medicos(id)
                );
            """)

            print()
            print("Creando tabala horario ...")
            #self.cursor.execute("""
            #    DROP TABLE IF EXISTS horario;
            #""")
            
            #hora_inicio: '14:30:00'
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS horario(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dia TEXT NOT NULL,
                hora_inicio TEXT NOT NULL, 
                hora_fin TEXT NOT NULL,
                id_medico INTEGER NOT NULL,
                FOREIGN KEY (id_medico) REFERENCES medicos(id)
                );
            """)

            print()
            print("Creando tabala administrador ...")
            #self.cursor.execute("""
            #    DROP TABLE IF EXISTS administrador;
            #""")
            
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS administrador(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                email TEXT NOT NULL,
                telefono TEXT NOT NULL,
                cargo TEXT NOT NULL,               
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            print()
            print("Creando tabala notificaciones ...")
            #self.cursor.execute("""
            #    DROP TABLE IF EXISTS notificaciones;
            #""")

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notificaciones(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_paciente INTEGER NOT NULL,
                id_cita INTEGER NOT NULL,
                mensaje TEXT NOT NULL,
                medio TEXT NOT NULL,
                fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                estado TEXT NOT NULL,    
                FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
                FOREIGN KEY(id_cita) REFERENCES citas(id)
                );
            """)

            print()
            print("Creando tabala reportes ...")
            self.cursor.execute("""
                DROP TABLE IF EXISTS reportes;
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reportes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_adm INTEGER NOT NULL,
                prg_envio TEXT NOT NULL,
                fecha TEXT NOT NULL,
                paciente TEXT NOT NULL,
                medico TEXT NOT NULL,
                especialidad TEXT,
                estado TEXT,
                modifico TEXT NOT NULL DEFAULT 'N/A',
                motivo TEXT NOT NULL DEFAULT 'N/A',
                fecha_generacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(id_adm) REFERENCES administrador(id)
                );
            """)
    
db=Create_db()
db.Crear_Tablas()
