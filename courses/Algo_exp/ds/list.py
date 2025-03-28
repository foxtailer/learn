# list/array

lst = [1, 2, 3]
lst2 = [4, 5]

lst[1]	# return 2. O(1)
lst.append(8)  # lst -> [1, 2, 3, 8]. O(1)
lst.insert(1, 8)  # lst -> [1, 8, 2, 3]. O(n). insert(index, value)
lst.extend(lst2)  # lst -> [1, 2, 3, 4, 5]. O(k) (where k is len of lst2)
del lst[-1]  # lst -> [1, 2]. O(n). By index
lst.remove(2)  # lst -> [1, 3]. O(n). By value
lst.pop()  # return 3, lst -> [1, 2]. O(1)
lst.pop(1)  # return 2, lst -> [1, 3] O(n). By index
len(lst)  # return 3. O(1)
lst.sort()  # lst -> [1, 2, 3]. O(n log n)
lst.reverse()  # lst -> [3, 2, 1]. O(n)
lst.copy()  # return [1, 2, 3]. O(n). *Shallow copy

# List Comprehension
[x*2 for x in lst]  # lst -> [2, 4, 6]. O(n)
[x for x in lst if x > 0]  # lst -> [1, 2, 3]. O(n)

# Slicing
lst[:]  # O(n). *Shallow copy
lst[1:2]  # O(k) (where k = b - a)

# Other List Methods
lst.count(1)  # return 1. O(n)
lst.index(1)  # return 0. O(n)
lst.clear()	  # lst -> []. O(n)
