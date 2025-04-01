list_1 = [5,1,3,4,7,2]
list_2 = ["a", "b", "c", "d", "e", "f", "g", "h"]

def merge(keys:list, vlues:list) -> dict:
    return dict(sorted(zip(keys, vlues)))

print(merge(list_1, list_2))  # {1: 'b', 2: 'f', 3: 'c', 4: 'd', 5: 'a', 7: 'e'}