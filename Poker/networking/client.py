import socket
import threading

class PokerClient:
    def __init__(self, host='localhost', port=5555):
        
        #Inicializa el cliente de póker y establece la conexión con el servidor.
        #:param host: Dirección del servidor al que se conecta (por defecto localhost).
        #:param port: Puerto del servidor (por defecto 5555).
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.connect((host, port))

    def send_message(self, message):
        
        #Envía un mensaje al servidor.
        #:param message: Mensaje a enviar.
        
        self.server_socket.send(message.encode('utf-8')) 

    def receive_messages(self):
        
        #Escucha mensajes del servidor y los imprime.
        
        while True:
            try:
                message = self.server_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Mensaje del servidor: {message}")
                else:
                    break  # Salimos si el servidor ha cerrado la conexión
            except Exception as e:
                print(f"Error al recibir mensajes del servidor: {e}")
                break

        self.server_socket.close()

    def run(self):
        
        #Inicia el cliente y comienza a recibir mensajes del servidor.
        
        threading.Thread(target=self.receive_messages).start()  # Inicia un hilo para recibir mensajes

        while True:
            message = input("Escribe un mensaje para enviar al servidor: ")
            self.send_message(message)  # Envía el mensaje al servidor

if __name__ == "__main__":
    poker_client = PokerClient()
    poker_client.run()
