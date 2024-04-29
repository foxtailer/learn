def anagram_checking_off(s1, s2):
    if len(s1) != len(s2):
      return False

    to_check_off = list(s2)

    for char in s1:
      for i, other_char in enumerate(to_check_off):
        if char == other_char:
            to_check_off[i] = None
            break
      else:
          return False

    return True

print(anagram_checking_off('abcd', 'dcba'))  # => True
print(anagram_checking_off('abcd', 'abcc'))  # => False

########################
print()

def anagram_checking_off(s1, s2):
   return sorted(s1) == sorted(s2)

print(anagram_checking_off('abcd', 'dcba'))  # => True
print(anagram_checking_off('abcd', 'abcc'))  # => False

######
print()

from itertools import zip_longest
def anagram_sort_and_compare(s1, s2):
    for a, b in zip_longest(sorted(s1), sorted(s2)):
        if a != b:
            return False
    return True

print(anagram_checking_off('abcd', 'dcba'))  # => True
print(anagram_checking_off('abcd', 'abcc'))  # => False

######
print()

def anagram_count_compare(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for char in s1:
        pos = ord(char) - ord('a')
        c1[pos] += 1

    for char in s2:
        pos = ord(char) - ord('a')
        c2[pos] += 1

    for a, b in zip(c1, c2):
        if a != b:
            return False
    return True

anagram_count_compare('apple', 'pleap')  # => True
anagram_count_compare('apple', 'applf')  # => False

from collections import Counter


def anagram_with_counter(s1, s2):
    return Counter(s1) == Counter(s2)

anagram_with_counter('apple', 'pleap')  # => True
anagram_with_counter('apple', 'applf')  # => False