# Fib microservice

from socket import *
from threading import Thread

from fib import fib


def fib_server(address: tuple[str, int]):  # address: ('1.1.1.1', 8000)
    sock = socket(AF_INET, SOCK_STREAM)  # AF_INET - use ipv4, SOCK_STREAM - tcp
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)  # Up to 3 conection before refuse next
    
    while True:
        # addr: (IP, port)
        # client: A new socket object used to communicate with the connected client.
        client, addr = sock.accept()  # waiting for client connections. Blocks until a client connects
        print('Conection', addr)
        # fib_handler(client)  # handle one client at a time without concurensy
        Thread(target=fib_handler, args=(client,)).start()  # Start a new thread for each client


def fib_handler(client):
    while True:
        # recv(100) Receives up to 100 bytes of data from the client.
        # If the client disconnects, recv() returns an empty byte string (b''), which will break the loop.
        req = client.recv(100)
        
        if not req:
            break

        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)  # Sends the computed Fibonacci number back to the client.
    print('Closed', client.getpeername())
    client.close()  # Make sure to close the socket


fib_server(('', 25000))
