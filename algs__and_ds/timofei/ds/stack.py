class Stack:
    def __init__(self):
        self.__index = []
    def __len__(self):
        return len(self.__index)
    def push(self, item):
        self.__index.append(item)
    def pop(self):
        return self.__index.pop()
    def top(self):
        return self.__index[-1]

