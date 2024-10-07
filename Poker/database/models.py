# Definiciones de tablas para la base de datos

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    total_chips INTEGER DEFAULT 1000,    # Fichas iniciales del jugador
    games_played INTEGER DEFAULT 0,      # Cantidad de partidas jugadas
    games_won INTEGER DEFAULT 0,         # Cantidad de partidas ganadas
    last_login TEXT                      # Última vez que se inició sesión
);
"""

CREATE_GAMES_TABLE = """
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,            # ID del jugador (relacionado con la tabla users)
    timestamp TEXT NOT NULL,             # Fecha y hora en que se jugó la partida
    result TEXT NOT NULL,                # Resultado de la partida (ganado, perdido, empate)
    chips_won INTEGER DEFAULT 0,         # Fichas ganadas o perdidas en esa partida
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

CREATE_SETTINGS_TABLE = """
CREATE TABLE IF NOT EXISTS settings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,            # ID del jugador (relacionado con la tabla users)
    volume REAL DEFAULT 0.5,             # Preferencia de volumen (0.0 a 1.0)
    theme TEXT DEFAULT 'dark',           # Preferencia de tema ('light' o 'dark')
    language TEXT DEFAULT 'es',          # Preferencia de idioma ('es' para español)
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# Explicación:
# - `users`: Tabla que almacena información sobre los usuarios, como nombre, email, contraseña y estadísticas generales.
# - `games`: Almacena el historial de partidas jugadas, relacionando cada partida con un jugador en particular.
# - `settings`: Almacena las preferencias personalizadas del usuario, como el volumen y el tema visual.
