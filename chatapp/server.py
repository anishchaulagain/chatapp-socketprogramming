import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345

clients = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# Function to handle each client connection
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break
    print(f"Connection closed from {client_address}")

# Main function to start the server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
