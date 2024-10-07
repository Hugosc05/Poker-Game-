import socket
import threading
import pickle  # Para serializar los datos enviados a través de la red

# ---------------------- SERVIDOR ----------------------

class PokerServer:
    def __init__(self, host="localhost", port=5555):
        # Inicializamos el servidor con la dirección del host y el puerto
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))  # Conectar a la dirección IP y el puerto
        self.server.listen()  # Escuchar conexiones entrantes
        print(f"Servidor escuchando en {host}:{port}")
        
        self.clients = []  # Lista de conexiones de los jugadores
        self.lock = threading.Lock()  # Control de concurrencia para múltiples hilos
        self.game_state = {}  # Estado del juego compartido entre los jugadores
    
    def handle_client(self, conn, addr):
        """
        Maneja cada cliente de manera individual en un hilo separado.
        """
        print(f"Conexión establecida con {addr}")
        self.clients.append(conn)

        try:
            while True:
                data = conn.recv(4096)  # Recibe datos del cliente
                if not data:
                    break

                # Deserializa los datos recibidos
                player_action = pickle.loads(data)

                # Manejar la acción del jugador aquí (apostar, retirarse, etc.)
                self.update_game_state(player_action)

                # Enviar el estado del juego actualizado a todos los jugadores
                self.broadcast_game_state()

        except Exception as e:
            print(f"Error con el cliente {addr}: {e}")
        finally:
            conn.close()  # Cerramos la conexión cuando el cliente se desconecta

    def update_game_state(self, player_action):
        """
        Actualiza el estado del juego en función de las acciones de los jugadores.
        """
        with self.lock:
            # Actualiza el estado del juego aquí según la acción recibida del jugador
            # Por ejemplo, podrías modificar el pozo, las apuestas, o las cartas repartidas
            self.game_state[player_action['player']] = player_action

    def broadcast_game_state(self):
        """
        Envía el estado del juego actualizado a todos los jugadores conectados.
        """
        with self.lock:
            for client in self.clients:
                try:
                    # Serializamos el estado del juego para enviarlo
                    data = pickle.dumps(self.game_state)
                    client.sendall(data)
                except Exception as e:
                    print(f"Error enviando el estado del juego: {e}")

    def start(self):
        """
        Inicia el servidor para aceptar conexiones entrantes.
        """
        print("Servidor iniciado, esperando jugadores...")
        while True:
            conn, addr = self.server.accept()  # Aceptar nuevas conexiones
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()  # Iniciar un hilo para manejar la nueva conexión


# ---------------------- CLIENTE ----------------------

class PokerClient:
    def __init__(self, host="localhost", port=5555):
        # Inicializamos el cliente y lo conectamos al servidor
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def send_action(self, action):
        """
        Envía la acción del jugador al servidor (apostar, retirarse, etc.).
        """
        try:
            # Serializa la acción y la envía al servidor
            data = pickle.dumps(action)
            self.client.sendall(data)
        except Exception as e:
            print(f"Error enviando la acción: {e}")

    def receive_game_state(self):
        """
        Recibe el estado del juego desde el servidor.
        """
        try:
            data = self.client.recv(4096)  # Recibe el estado del juego
            if data:
                # Deserializa los datos recibidos para obtener el estado del juego
                game_state = pickle.loads(data)
                return game_state
        except Exception as e:
            print(f"Error recibiendo el estado del juego: {e}")
