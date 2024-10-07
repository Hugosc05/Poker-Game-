# ---------------------- CONFIGURACIONES DEL JUEGO ----------------------

GAME_SETTINGS = {
    'max_players': 6,            # Número máximo de jugadores permitidos en una partida
    'min_players': 2,            # Número mínimo de jugadores para empezar la partida
    'starting_chips': 1000,      # Cantidad inicial de fichas para cada jugador
    'small_blind': 10,           # Tamaño del "small blind" en cada ronda de apuestas
    'big_blind': 20,             # Tamaño del "big blind"
    'betting_rounds': 4,         # Número de rondas de apuestas en el juego
    'deck_type': 'poker',        # Tipo de baraja a usar (en este caso baraja estándar de póker)
    'time_limit_turn': 60,       # Límite de tiempo en segundos para cada turno
}

# Explicación:
# - 'max_players' y 'min_players' definen el número de jugadores que pueden unirse a una partida.
# - 'starting_chips' define la cantidad de fichas con la que comienza cada jugador.
# - 'small_blind' y 'big_blind' son las apuestas obligatorias en el póker.
# - 'betting_rounds' define cuántas rondas de apuestas habrá (preflop, flop, turn, river).
# - 'deck_type' indica el tipo de baraja que se usará en el juego (póker estándar).
# - 'time_limit_turn' es el tiempo que tiene cada jugador para tomar una decisión en cada turno.

# ---------------------- AJUSTES DE LA IA ----------------------

AI_SETTINGS = {
    'difficulty': 'medium',      # Dificultad de la IA (fácil, media, difícil)
    'aggressiveness': 0.5,       # Nivel de agresividad de la IA (0.0 - 1.0)
    'bluff_frequency': 0.3,      # Probabilidad de que la IA haga "bluff" (0.0 - 1.0)
}

# Explicación:
# - 'difficulty' define el nivel de inteligencia de la IA (fácil, media, difícil). Afecta la toma de decisiones.
# - 'aggressiveness' indica cuán agresiva será la IA al subir apuestas.
# - 'bluff_frequency' establece con qué frecuencia la IA hará "bluff" (apostar fuerte con una mano débil).

# ---------------------- CONFIGURACIONES DE RED ----------------------

NETWORK_SETTINGS = {
    'server_ip': 'localhost',    # Dirección IP del servidor para partidas online (localhost para pruebas locales)
    'server_port': 5555,         # Puerto del servidor
    'client_timeout': 30,        # Tiempo máximo de espera para el cliente al conectarse al servidor (en segundos)
}

# Explicación:
# - 'server_ip' es la dirección del servidor. En un entorno de producción, podría ser una dirección IP pública.
# - 'server_port' es el puerto en el que el servidor acepta conexiones.
# - 'client_timeout' define cuántos segundos un cliente intentará conectarse al servidor antes de desistir.

# ---------------------- AJUSTES DE PERSONALIZACIÓN ----------------------

USER_PREFERENCES = {
    'volume': 0.5,               # Volumen de la música y efectos de sonido (0.0 - 1.0)
    'theme': 'dark',             # Tema visual del juego ('light', 'dark')
    'language': 'es',            # Idioma del juego ('es' para español, 'en' para inglés, etc.)
}

# Explicación:
# - 'volume' define el nivel de volumen para la música y efectos de sonido.
# - 'theme' es el tema visual del juego. Aquí los usuarios pueden elegir entre un tema claro ('light') o oscuro ('dark').
# - 'language' especifica el idioma del juego. Puede ser útil para la internacionalización (i18n).
