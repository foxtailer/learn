itarable_obj = (1,2,3,4,5)

new_iterator = iter(itarable_obj)

while True:
    try:
        print(next(new_iterator))
    except:
        print("Stop iteration")
        break
print("***********")
#################################


class Reverse():
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
    
rev = Reverse("spam")
print(type(iter(rev)))
print()

for char in rev:
    print(char)

print("__next__" in dir(iter([1,2])))
