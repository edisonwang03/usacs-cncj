import socket


def encrypt(message: str) -> str:
    """Encrypts a message using a simple Caesar cipher

    Args:
        message (str): The message to encrypt

    Returns:
        str: The encrypted message
    """
    # IMPLEMENT FUNCTION HERE
    return ""


def udp_client():
    """Starts a client that sends messages to a server and receives echos"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 12345)

    try:
        while True:
            message = input("Enter message to send: ")
            message = encrypt(message)
            client_socket.sendto(message.encode(), server_address)
            print(f"Sent message: {message}")
            data, _ = client_socket.recvfrom(1024)
            print(f"Received echo: {data.decode()}")
    except KeyboardInterrupt:
        print("Client exiting")
    finally:
        client_socket.close()
        print("Client socket closed")


if __name__ == "__main__":
    udp_client()
