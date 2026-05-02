import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import socket

# AF_INET = IPv4
# SOCK_STREAM = TCP (reliable stream)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 65432))


def get_lines(file):
    # Like if we read file as string
    # open('messages.txt, 'r') as f

    tmp = ''
    result = []

    for byte in file:
        byte = bytes([byte])
        
        if (str_chunk := byte.decode('utf-8', errors='replace')) != '\n':
            tmp += str_chunk
        else:
            result.append(tmp)
            tmp = ''

    # If file doesn't end with new line
    if tmp:
        result.append(tmp) 

    return result


# Start listening (allow 1 connection in queue)
s.listen(1)
print("Waiting for a connection...")


# Accept a new connection
conn, addr = s.accept()

with conn:
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data: break
        
        lines = get_lines(data)
        for line in lines:
            print(line)
