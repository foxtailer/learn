# O(n) time | O(n) space
def spiralTraverse(array):
    result = []
    start_row, end_row = 0, len(array)-1
    start_col, end_col = 0, len(array[0])-1

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])
        
        for col in reversed(range(start_col, end_col)):
            result.append(array[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            result.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return result


def spiralTraverse2(array):
    result = []
    spiral_fill(array, 0, len(array)-1, 0, len(array[0])-1, result)

    return result

def spiral_fill(array, start_row, end_row, start_col, end_col, result):
    if start_row > end_row or start_col > end_col:
        return
    
    for col in range(start_col, end_col + 1):
        result.append(array[start_row][col])

    for row in range(start_row + 1, end_row + 1):
        result.append(array[row][end_col])
    
    for col in reversed(range(start_col, end_col)):
        result.append(array[end_row][col])

    for row in reversed(range(start_row + 1, end_row)):
        result.append(array[row][start_col])
    
    spiral_fill(array, 
                start_row + 1, 
                end_row - 1, 
                start_col + 1, 
                end_col - 1, 
                result)


array = [[1,2,3,4],
         [12,13,14,5],   
         [11,16,15,6],
         [10,9,8,7]]

print(spiralTraverse(array))
print(spiralTraverse2(array))
