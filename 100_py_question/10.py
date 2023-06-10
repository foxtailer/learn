# Write a program that accepts a sequence of whitespace separated words as input and prints 
# the words after removing all duplicate words and sorting them alphanumerically.

# Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again
# Then, the output should be:

# again and hello makes perfect practice world

print(*list(set(input('...').split(' '))))


word = input().split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))
word = input().split()
[word.remove(i) for i in word if word.count(i) > 1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))