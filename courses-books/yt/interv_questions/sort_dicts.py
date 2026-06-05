users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

users.sort(key=lambda x: x["age"])
print(users)

a = [5, 2, 9, 1, 5, [4]]
def custom_sort(l:list):
    return sorted(a, key=lambda x: str(x))

b = custom_sort(a)
print(b)
b[5].append(3)
print(a)