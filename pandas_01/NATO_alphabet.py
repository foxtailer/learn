import pandas as pd

data = pd.read_csv(r"C:\Users\User\Desktop\glovo\git\learn\pandas_01\nato_phonetic_alphabet.csv")
NATO_ALPHABET = {row.letter : row.code for (index, row) in data.iterrows()}

while True:
    word = input("Word for translate: ")
    # result = []
    # for i in word:
    #     if i.upper() in NATO_ALPHABET:
    #         result.append(NATO_ALPHABET[i.upper()])
    result = [NATO_ALPHABET[letter.upper()] for letter in word]
    print(result)