import socket
import threading

# Client configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Function to handle sending messages to the server
def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Main function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start threads for sending and receiving messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket,)).start()

if __name__ == "__main__":
    start_client()
