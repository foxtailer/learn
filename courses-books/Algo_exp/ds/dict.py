# Dictionary Operations

dct = {'a': 1, 'b': 2, 'c': 3}
dct2 = {'d': 4, 'e': 5}

dct['a']  # return 1. O(1)
dct['z'] = 8  # dct -> {'a': 1, 'b': 2, 'c': 3, 'z': 8}. O(1)
dct.update(dct2)  # dct -> {'a': 1, 'b': 2, 'c': 3, 'z': 8, 'd': 4, 'e': 5}. O(k) (where k is len of dct2)
del dct['c']  # dct -> {'a': 1, 'b': 2, 'z': 8, 'd': 4, 'e': 5}. O(1)
dct.pop('b')  # return 2, dct -> {'a': 1, 'z': 8, 'd': 4, 'e': 5}. O(1)
dct.popitem()  # return ('e', 5), dct -> {'a': 1, 'z': 8, 'd': 4}. O(1)
len(dct)  # return 3. O(1)

# Dictionary Methods
dct.copy()  # return {'a': 1, 'b': 2, 'c': 3}. Shallow copy. O(n)
dct.keys()  # return dict_keys(['a', 'z', 'd']). O(n)
dct.values()  # return dict_values([1, 8, 4]). O(n)
dct.items()  # return dict_items([('a', 1), ('z', 8), ('d', 4)]). O(n)
dct.get('a')  # return 1 or None if 'a' not in dct. O(1)
dct.get('x', 'default')  # return 'default' or 'x' value if 'x' in dict. O(1)
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
dct.setdefault('y', 10)  # dct -> {'a': 1, 'z': 8, 'd': 4, 'y': 10}. O(1)
dct.clear()  # dct -> {}. O(n)
dict.fromkeys(('x', 'y', 'z'), 10)  # return {'x':10, 'y':10, 'z':10}. 10 is optional, by default = None. O(n)

# Dictionary Comprehension
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}. O(n)
{x: x for x in dct if dct[x] > 0}  # Filter positive values. O(n)

"""
* index = hash(key) % size_of_dict_table
"""
