import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('messages.txt', 'rb') as f:
    # Like if we read file as string
    # open('messages.txt, 'r') as f
    
    tmp = ''
    while True:
        chunk = f.read(1)

        if not chunk:
            break
        
        if (str_chunk := chunk.decode('utf-8', errors='replace')) != '\n':
            tmp += str_chunk
        else:
            print(tmp)
            tmp = ''

    # If file doesn't end with new line
    if tmp:
        print(tmp) 