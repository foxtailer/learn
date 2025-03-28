# AND
print('AND')
print(f'{1 & 1 = }')  # 1
print(f'{1 & 0 = }')  # 0
print(f'{0 & 1 = }')  # 0
print(f'{0 & 0 = }')  # 0
print()

# OR
print('OR')
print(f'{1 | 1 = }')  # 1
print(f'{1 | 0 = }')  # 1
print(f'{0 | 1 = }')  # 1
print(f'{0 | 0 = }')  # 0
print()

# NOT
print('NOT')
print(f'{1 - 1 = }')  # 0
print(f'{1 - 0 = }')  # 1
print()

# NOR
print('NOR')
print(f'{1 - (1 | 1) = }')  # 0
print(f'{1 - (1 | 0) = }')  # 0
print(f'{1 - (0 | 1) = }')  # 0
print(f'{1 - (0 | 0) = }')  # 1
print()
'''
NOR = AND with NOT on each input
print(f'{1-1 & 1-1 = }')  # 0
print(f'{1-1 & 1-0 = }')  # 0
print(f'{1-0 & 1-1 = }')  # 0
print(f'{1-0 & 1-0 = }')  # 1
'''

# NAND
print('NAND')
print(f'{1 - (1 & 1) = }')  # 0
print(f'{1 - (1 & 0) = }')  # 1
print(f'{1 - (0 & 1) = }')  # 1
print(f'{1 - (0 & 0) = }')  # 1
print()
'''
NAND = OR with NOT on each input
print(f'{1-1 | 1-1 = }')  # 0
print(f'{1-1 | 1-0 = }')  # 1
print(f'{1-0 | 1-1 = }')  # 1
print(f'{1-0 | 1-0 = }')  # 1
'''

# XOR 
print('XOR')
print(f'{1 ^ 1 = }')  # 0
print(f'{1 ^ 0 = }')  # 1
print(f'{0 ^ 1 = }')  # 1
print(f'{0 ^ 0 = }')  # 0
print()

# XNOR 
print('XNOR')
print(f'{1 - (1 ^ 1) = }')  # 1
print(f'{1 - (1 ^ 0) = }')  # 0
print(f'{1 - (0 ^ 1) = }')  # 0
print(f'{1 - (0 ^ 0) = }')  # 1
print()
