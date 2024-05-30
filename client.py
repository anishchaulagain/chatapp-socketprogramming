import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    try:
        client_socket.connect((host, port))
    except ConnectionRefusedError:
        print("Failed to connect to the server. Is the server running?")
        return

    client_name = input("Enter your client name: ")
    client_socket.send(client_name.encode())
    server_name = client_socket.recv(1024).decode()

    print(f"Connected to server: {server_name}")

    message = input(f'{client_name} -> ')

    while message.lower().strip() != 'bye':
        try:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print(f'{server_name}: {data}')
        except BrokenPipeError:
            print("Connection lost to the server.")
            break
        message = input(f'{client_name} -> ')

    client_socket.close()

if __name__ == '__main__':
    client_program()
