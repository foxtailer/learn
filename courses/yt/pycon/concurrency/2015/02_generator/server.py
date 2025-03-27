# Fib microservice

from socket import *
from concurrent.futures import ProcessPoolExecutor as Pool
from collections import deque
from select import select

from fib import fib


pool = Pool()

tasks = deque()
recv_wait = {}  # Mapping sockets -> task (generators)
send_wait = {}
future_wait = {}

future_notify, future_event = socketpair()


def future_done(future):
    tasks.append(future_wait.pop(future))
    future_notify.send(b'x')


def future_monitor():
    while True:
        yield 'recv', future_event
        future_event.recv(100)

tasks.append(future_monitor())


def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            # No active tasks to run
            # wait for I/O
            can_recv, can_send, [] = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task = tasks.popleft()
        try:
            why, what = next(task)  # Run to the yield 
            if why == 'recv':
                # Must go wait somewhere
                recv_wait[what] = task
            elif why == 'send':
                send_wait[what] = task
            elif why == 'future':
                future_wait[what] = task
                what.add_done_callback(future_done)
            else:
                print(why)
                raise RuntimeError('ARG!')
        except StopIteration:
            print('task done')


def fib_server(address: tuple[str, int]):  # address: ('1.1.1.1', 8000)
    sock = socket(AF_INET, SOCK_STREAM)  # AF_INET - use ipv4, SOCK_STREAM - tcp
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)  # Up to 3 conection before refuse next
    
    while True:
        # addr: (IP, port)
        # client: A new socket object used to communicate with the connected client.
        yield 'recv', sock
        client, addr = sock.accept()  # waiting for client connections. Blocks until a client connects # blocking
        print('Conection', addr)
        tasks.append(fib_handler(client))  # handle one client at a time without concurensy


def fib_handler(client):
    while True:
        # recv(100) Receives up to 100 bytes of data from the client.
        # If the client disconnects, recv() returns an empty byte string (b''), which will break the loop.
        yield 'recv', client
        req = client.recv(100)  # blocking
        
        if not req:
            break

        n = int(req)
        future = pool.submit(fib, n)
        yield 'future', future
        result = future.result()
        resp = str(result).encode('ascii') + b'\n'
        yield 'send', client
        client.send(resp)  # Sends the computed Fibonacci number back to the client. # blocking
    print('Closed', client.getpeername())
    #client.close()  # Make sure to close the socket


tasks.append(fib_server(('', 25000)))
run()
