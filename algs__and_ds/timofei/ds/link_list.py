a = [1]
a.append([2])
a[1].append([3])
a[1][1].append([4])
a[1][1][1].append(None)

# Iter
p = a
while p is not None:
    print(p[0])
    p = p[1]

class LinkedList:
    def __init__(self) -> None:
        self._begin = None
    def insert(self, item):
        self._begin = [item, self._begin]
    def pop(self):
        assert self._begin is not None, "List is empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x

