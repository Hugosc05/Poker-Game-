import socket
import threading
from database.db_manager import DatabaseManager

class PokerServer:
    def __init__(self, host='localhost', port=5555):
        
        #Inicializa el servidor de póker y establece la configuración inicial.
        #:param host: Dirección del servidor (por defecto localhost).
        #:param port: Puerto en el que el servidor escuchará conexiones (por defecto 5555).
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)  # Escucha hasta 5 conexiones simultáneas
        self.clients = []  # Lista para almacenar los clientes conectados
        self.db = DatabaseManager("poker_game.db")  # Conexión a la base de datos

    def handle_client(self, client_socket, addr):
        
        #Maneja la comunicación con un cliente conectado.
        #:param client_socket: Socket del cliente conectado.
        #:param addr: Dirección del cliente.
        
        print(f"Conexión establecida con {addr}")
        self.clients.append(client_socket) # Añadimos el cliente a la lista de clientes

        while True:
            try:
                # Recibimos datos del cliente
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Mensaje recibido de {addr}: {message}")
                    self.broadcast(message, client_socket)  # Envía el mensaje a todos los clientes
                else:
                    break  # Salimos si el cliente ha cerrado la conexión
            except Exception as e:
                print(f"Error en la comunicación con {addr}: {e}")
                break

        # Cerramos la conexión cuando el cliente se desconecta
        client_socket.close()
        self.clients.remove(client_socket)
        print(f"Conexión cerrada con {addr}")

    def broadcast(self, message, sender_socket):
        
        #Envía un mensaje a todos los clientes conectados, excepto al que envió el mensaje.
        #:param message: Mensaje a enviar.
        #:param sender_socket: Socket del cliente que envió el mensaje.
        
        for client in self.clients:
            if client != sender_socket:  # No enviar al que lo envió
                try:
                    client.send(message.encode('utf-8'))
                except Exception as e:
                    print(f"Error al enviar mensaje a un cliente: {e}")
                    client.close()
                    self.clients.remove(client)

    def run(self):
        
        #Inicia el servidor y comienza a aceptar conexiones de clientes.
        
        print("Servidor de póker en ejecución...")
        while True:
            client_socket, addr = self.server_socket.accept()  # Acepta una nueva conexión
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, addr)) # Inicia un hilo para manejar el cliente
            client_thread.start()  # Inicia un nuevo hilo para manejar al cliente

if __name__ == "__main__":
    poker_server = PokerServer()
    poker_server.run()
