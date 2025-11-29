# Find common letters between two strings

def common_letters(str_1:str, str_2:str) -> set:
    return set(str_1) & set(str_2)

print(common_letters('tara', 'boro'))