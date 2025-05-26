import base64


x = '{"showpassword":"yes","bgcolor":"#ffffff"}'  # no
y = 'DWoe'


def xor_encrypt(text, key):
    out_bytes = bytearray()
    for i in range(len(text)):
        out_bytes.append(ord(text[i]) ^ ord(key[i % len(key)]))
    return base64.b64encode(out_bytes).decode('utf-8')


def xor_decrypt(text, key):
    encrypted_bytes = base64.b64decode(text)
    return ''.join(chr(b ^ ord(key[i % len(key)])) for i, b in enumerate(encrypted_bytes))


print(tmp:= xor_encrypt(`, y))
print(xor_decrypt(tmp, y))
