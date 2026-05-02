import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('messages.txt', 'rb') as f:
    print('Read by 8 bytes.')

    n = 1
    while True:
        chunk = f.read(8)
        if not chunk:
            break
        
        bin_str = ' '.join(f'{b:08b}' for b in chunk)
        dec_str = ' '.join(f'{b:3d}' for b in chunk)

        # hex: ' '.join(chunk.hex()[i:i+2] for i in range(0, len(chunk.hex()), 2))
        print(f'''Chunk #{n}:
    chunk: {object.__repr__(chunk)};
    hex: {chunk.hex(' ')};
    dec: {dec_str};
    bin: {bin_str};
    str: {chunk.decode('utf-8', errors='replace')};''') 
        n += 1