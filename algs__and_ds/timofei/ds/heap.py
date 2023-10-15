class Heap:
    def __init__(self) -> None:
        self.values=[]
        self.size=0
    
    def insert (self, x):
        self.values.append(x)
        self.size += 1
        self.shift_up(self.size-1)

    def shift_up(self, i):
        stop = False
        while i!=0 and stop==False:
            if self.values[i] < self.values[i//2]:
                self.values[i],self.values[i//2] = self.values[i//2],self.values[i]
            else:
                stop = True
            i = i//2
    
    def extract_min(self):
        if not self.size:
            return None

        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size-=1
        self.shift_down(0)
        return tmp

    def shift_down(self, i):
        while i+1 < self.size:
            j=i
            if self.values[2*i+1] < self.values[i]:
                j = 2*i+1
            if 2*i+2 < self.size and self.values[2*i+2] < self.values[j]:
                j = 2*i+2
            if i == j:
                break
            self.values[i],self.values[j] = self.values[j],self.values[i]

if __name__ == "__main__":
    h = Heap()
    h.insert(3)
    h.insert(5)
    h.insert(2)
    h.insert(8)
    h.insert(1)
    print(h.values)
    print(h.extract_min())
    print(h.values)