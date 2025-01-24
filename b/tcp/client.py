import socket


def tcp_client():
    """Starts a client that sends messages to a server and receives echos"""
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Client connected to server")

    try:
        while True:
            message = input("Enter message to send: ")
            client_socket.sendall(message.encode())
            print(f"Sent message: {message}")
            data = client_socket.recv(1024)
            print(f"Received echo: {data.decode()}")
    except KeyboardInterrupt:
        print("Client exiting")
    finally:
        client_socket.close()
        print("Client socket closed")


if __name__ == "__main__":
    tcp_client()
