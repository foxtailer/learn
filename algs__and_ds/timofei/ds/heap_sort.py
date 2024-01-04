import heap, math
from io import StringIO

def show_tree(tree, total_width=60, fil=" "):
    output = StringIO()
    last_row = -1
    for i,n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1,2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')    
        columns = 2**row
        col_width = int(math.floor((total_width*1)/columns))
        output.write(str(n).center(col_width, fil))
        last_row = row
    print(output.getvalue())
    print('-'*total_width)
    return



arr = [2,5,6,17,24,53,12,3,8,5]

hp = heap.Heap()

for i in arr:
    hp.insert(i)
#show_tree(hp.values)


sorted_arr = []

while hp.size:
    sorted_arr.append(hp.extract_min())
    print(show_tree(hp.values))
