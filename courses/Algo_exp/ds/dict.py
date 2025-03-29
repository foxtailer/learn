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
dct.keys()  # return dict_keys(['a', 'z', 'd']). O(n)
dct.values()  # return dict_values([1, 8, 4]). O(n)
dct.items()  # return dict_items([('a', 1), ('z', 8), ('d', 4)]). O(n)
dct.get('a')  # return 1. O(1)
dct.get('x', 'default')  # return 'default'. O(1)
dct.setdefault('y', 10)  # dct -> {'a': 1, 'z': 8, 'd': 4, 'y': 10}. O(1)
dct.clear()  # dct -> {}. O(n)

# Dictionary Comprehension
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}. O(n)
{x: x for x in dct if dct[x] > 0}  # Filter positive values. O(n)

# Other Methods
dct.pop('z')  # return 8, dct -> {'a': 1, 'd': 4, 'y': 10}. O(1)
