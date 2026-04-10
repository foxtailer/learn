import socket
import threading
import sys

if len(sys.argv) != 3:
    print("Usage: python chat.py <my_port> <peer_port>")
    sys.exit(1)

MY_PORT = int(sys.argv[1])
PEER_PORT = int(sys.argv[2])
PEER_IP = "127.0.0.1"  # localhost

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", MY_PORT))

print(f"Listening on port {MY_PORT}...")

def receive():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\n{addr[1]}: {data.decode()}\n>>> ", end="", flush=True)

def send():
    while True:
        msg = input(">>> ")
        if msg:
            sock.sendto(msg.encode(), (PEER_IP, PEER_PORT))

# старт потоков
threading.Thread(target=receive, daemon=True).start()
send()



"""
import asyncio
import sys

if len(sys.argv) != 3:
    print("Usage: python chat_async.py <my_port> <peer_port>")
    sys.exit(1)

MY_PORT = int(sys.argv[1])
PEER_PORT = int(sys.argv[2])
PEER_IP = "127.0.0.1"


class ChatProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        self.transport = transport
        print(f"Listening on port {MY_PORT}...")

    def datagram_received(self, data, addr):
        print(f"\n{addr[1]}: {data.decode()}\n>>> ", end="", flush=True)


async def send_loop(transport):
    loop = asyncio.get_running_loop()
    while True:
        # input() блокирует → запускаем в отдельном thread pool
        msg = await loop.run_in_executor(None, input, ">>> ")
        transport.sendto(msg.encode(), (PEER_IP, PEER_PORT))


async def main():
    loop = asyncio.get_running_loop()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: ChatProtocol(),
        local_addr=("0.0.0.0", MY_PORT),
    )

    await send_loop(transport)


asyncio.run(main())
"""
