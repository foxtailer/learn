import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server (IP and Port)
s.connect(("127.0.0.1", 65432)) 

s.sendall(b"""Hello Serwer!
I'm client.
How are you?""")

s.close()
