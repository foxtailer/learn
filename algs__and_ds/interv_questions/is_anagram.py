from collections import defaultdict

def is_anagram(word_1, word_2):
    return sorted(list(word_1)) == sorted(list(word_2))

def is_anagram_2(word_1, word_2):
    temp = defaultdict(lambda: 0)  # lambda:0 == int

    for char in word_1:
        temp[char] += 1
    for char in word_2:
        temp[char] -= 1

    for i in temp.values():
        if i != 0:
            return False
    return True

def is_anagram_3(word_1, word_2):
    count = [0]*26

    for char in word_1:
        count[ord(char) - ord("a")] += 1
    for char in word_2:
        count[ord(char) - ord("a")] -= 1
    
    for i in count:
        if i != 0:
            return False
    return True
    

print(is_anagram('cat', 'tac'))
print(is_anagram('catb', 'tacd'))
print('*')
print(is_anagram_2('cat', 'tac'))
print(is_anagram_2('catb', 'tacd'))
print('*')
print(is_anagram_3('cat', 'tac'))
print(is_anagram_3('catb', 'tacd'))


