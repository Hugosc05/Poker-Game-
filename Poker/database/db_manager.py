import sqlite3
from sqlite3 import Error

class DatabaseManager:
    def __init__(self, db_file):
        
        #Inicializa el administrador de la base de datos y establece la conexión.
        #:param db_file: La ruta al archivo de base de datos SQLite.
        
        self.connection = None
        try:
            # Conectamos con la base de datos SQLite
            self.connection = sqlite3.connect(db_file)
            print("Conexión a la base de datos SQLite exitosa.")
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")

    def execute_query(self, query, params=()):
        
        #Ejecuta una consulta SQL (INSERT, UPDATE, DELETE).
        #:param query: La consulta SQL a ejecutar.
        #:param params: Parámetros opcionales para la consulta.
        
        cursor = self.connection.cursor()  # Creamos un cursor para la consulta
        try:
            cursor.execute(query, params)  # Ejecutamos la consulta
            self.connection.commit()  # Aplicamos los cambios
            print("Consulta ejecutada exitosamente.")
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def execute_read_query(self, query, params=()):
        
        #Ejecuta una consulta SQL de lectura (SELECT) y devuelve los resultados.
        #:param query: La consulta SQL a ejecutar.
        #:param params: Parámetros opcionales para la consulta.
        #:return: Los resultados de la consulta.
    
        cursor = self.connection.cursor() # Creamos un cursor para la consulta
        result = None
        try:
            cursor.execute(query, params)  # Ejecutamos la consulta
            result = cursor.fetchall()  # Obtenemos todos los resultados
            return result
        except Error as e:
            print(f"Error al leer de la base de datos: {e}")
            return None
