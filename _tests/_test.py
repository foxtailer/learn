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