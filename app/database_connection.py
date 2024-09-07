import sqlite3
class Singleton:
    __instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__new__(cls)
        return cls.__instances[cls]

class DatabaseConnection(Singleton):
    connection = None

    def __init__(self):
        if self.connection is None:
            self.connection = sqlite3.connect("citas_medicas.sqlite3", check_same_thread=False)

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.connection.commit()
        return cursor.fetchall()
    
    def close(self):
        self.connection.close()

