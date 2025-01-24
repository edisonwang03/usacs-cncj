import socket


def tcp_server():
    """Starts a server that listens for messages and echos them back"""
    # IMPLEMENT FUNCTION HERE

    # STEP 1: Create a TCP socket

    # STEP 2: Listen for one incoming connection

    while True:
        # STEP 3: Accept the incoming connection
        conn = None

        try:
            # STEP 4: Create a loop to receive messages and echo them back
            while True:
                pass
        except ConnectionResetError:
            print("Connection closed by client")
        finally:
            conn.close()
            print("Connection closed")


if __name__ == "__main__":
    tcp_server()
