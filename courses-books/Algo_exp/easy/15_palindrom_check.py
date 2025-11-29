# O(n) time | O(n) space
def is_palindrom(string):
    if len(string) == 1:
        return True
    else:
        return string[0]==string[-1] and is_palindrom(string[1:-1])
    

def is_palindrom2(string):
    reversed_string = ''
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return reversed_string == string


def is_palindrom3(string, i=0):
    j = len(string)-1 - i
    return True if i>=j else string[i] == string[j] and is_palindrom3(string, i+1)

# tail recursion
def is_palindrom4(string, i=0):
    j = len(string)-1 - i
    if i>=j:
        return True
    if string[i] != string[j]:
        return False
    return is_palindrom4(string, i+1)

# O(n) time | O(1) space
def is_palindrom5(string):
    left_indx = 0
    right_indx = len(string)-1

    while left_indx < right_indx:
        if string[left_indx] != string[right_indx]:
            return False
        else:
            left_indx += 1
            right_indx -= 1
    return True


string1 = 'abcdcba'
string2 = 'abcdgcba'

print(is_palindrom(string1))
print(is_palindrom(string2))
print('@')
print(is_palindrom2(string1))
print(is_palindrom2(string2))
print('@')
print(is_palindrom3(string1))
print(is_palindrom3(string2))
print('@')
print(is_palindrom4(string1))
print(is_palindrom4(string2))
print('@')
print(is_palindrom5(string1))
print(is_palindrom5(string2))