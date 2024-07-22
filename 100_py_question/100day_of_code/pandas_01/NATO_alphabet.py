import pandas as pd

data = pd.read_csv(r"E:\YD\git\learn\pandas_01\nato_phonetic_alphabet.csv")
NATO_ALPHABET = {row.letter : row.code for (index, row) in data.iterrows()}

# while True:
#     word = input("Word for translate: ")
#     # result = []
#     # for i in word:
#     #     if i.upper() in NATO_ALPHABET:
#     #         result.append(NATO_ALPHABET[i.upper()])
#     try:
#         result = [NATO_ALPHABET[letter.upper()] for letter in word]
#         print(result, "\n")
#     except KeyError:
#         print("Something wrong!")


def nato_translator():
    word = input("Word for translate: ")

    try:
        result = [NATO_ALPHABET[letter.upper()] for letter in word]
    except KeyError:
        print("Something wrong!", "\n")
        nato_translator()
    else:
        print(result, "\n")
    finally:
        nato_translator()


nato_translator()