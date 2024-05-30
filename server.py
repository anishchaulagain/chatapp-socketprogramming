import socket
import threading

def handle_client(conn, address, server_name):
    print(f"Connection from: {address}")
    client_name = conn.recv(1024).decode()
    conn.send(server_name.encode())

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"{client_name}: {data}")
            response = input(f'{server_name} -> ')
            conn.send(response.encode())
        except ConnectionResetError:
            print(f"Connection lost from {address}")
            break
    conn.close()

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)

    server_name = input("Enter your server name: ")
    print(f"Server listening on {host}:{port}")

    while True:
        conn, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, address, server_name)).start()

if __name__ == '__main__':
    server_program()
