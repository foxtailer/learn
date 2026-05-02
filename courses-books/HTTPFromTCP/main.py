import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def get_lines(file):
    # Like if we read file as string
    # open('messages.txt, 'r') as f

    tmp = ''
    result = []

    while True:
        chunk = f.read(1)

        if not chunk:
            break
        
        if (str_chunk := chunk.decode('utf-8', errors='replace')) != '\n':
            tmp += str_chunk
        else:
            result.append(tmp)
            tmp = ''

    # If file doesn't end with new line
    if tmp:
        result.append(tmp) 

    return result


with open('messages.txt', 'rb') as f:
    lines = get_lines(f)

    for line in lines:
        print(line)    
