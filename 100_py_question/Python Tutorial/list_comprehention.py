matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]
]
 
odd_numbers = [element for row in matrix for element in row if element % 2 != 0]
 
print(odd_numbers)