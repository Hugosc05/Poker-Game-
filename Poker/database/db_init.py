from db_manager import DatabaseManager
from models import CREATE_USERS_TABLE, CREATE_GAMES_TABLE, CREATE_SETTINGS_TABLE

def initialize_database():
    # Inicializa la base de datos creando las tablas necesarias.
    
    db = DatabaseManager("poker_game.db")  # Nombre de la base de datos SQLite

    # Crear las tablas en la base de datos
    db.execute_query(CREATE_USERS_TABLE) # Tabla de usuarios
    db.execute_query(CREATE_GAMES_TABLE) # Tabla de partidas
    db.execute_query(CREATE_SETTINGS_TABLE) # Tabla de settings

if __name__ == "__main__":  # Ejecutar el script si es el archivo principal
    initialize_database() # Inicializamos la base de datos
    print("Base de datos inicializada con éxito.") 
