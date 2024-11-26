# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:

# hello world! 123
# Then, the output should be:

# LETTERS 10
# DIGITS 3

import re

data = input('...')

letters = re.findall('[a-zA-Z]', data)
numbers = re.findall('\d', data)

print('LETTERS', len(letters))
print('NUMBERS', len(numbers))

#2
word = input()
letter,digit = 0,0
for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))

#3
word = input()
letter, digit = 0,0

for i in word:
    if i.isalpha(): # returns True if alphabet
        letter += 1
    elif i.isnumeric(): # returns True if numeric
        digit += 1
print(f"LETTERS {letter}\n{digit}") # two different types of formating method is shown in both solution