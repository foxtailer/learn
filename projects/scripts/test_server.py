import socket

# Define the IP address and port to listen on
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 334  # Port to listen on (should match the port you're forwarding on the router)

def start_server():
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))  # Bind to the IP and port
        server_socket.listen(1)  # Allow one connection at a time
        print(f"Listening for incoming connections on port {PORT}...")

        # Wait for a connection
        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connection received from {client_address}")
                # Send a message to the client (optional)
                client_socket.sendall(b"Connection received, router is forwarding properly.\n")
                print("Response sent to client.")
                break  # Close after handling one connection

if __name__ == "__main__":
    start_server()
