def caesar_cipher_encriptor(string, key):
    new_letters = []
    new_key = key % 26

    for letter in string:
        new_letter_code = ord(letter) + new_key
        new_letters.append(chr(new_letter_code)) if new_letter_code <= 122 else new_letters.append(chr(96 + new_letter_code % 122))

    return ''.join(new_letters)

def caesar_cipher_decriptor(string, key):
    new_letters = []
    new_key = key % 26

    for letter in string:
        new_letter_code = ord(letter) - new_key
        new_letters.append(chr(new_letter_code)) if new_letter_code >=97 else new_letters.append(chr(123 - (97 - new_letter_code)))

    return ''.join(new_letters)

word = 'helloworld'
print(f'Primary word: {word}\n\
      Encripted word: {caesar_cipher_encriptor(word, 2)}\n\
      Decripted word: {caesar_cipher_decriptor(caesar_cipher_encriptor(word, 2), 2)}')
