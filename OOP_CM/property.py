class Simbol():
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        print('Done!')
        return self._name
    
    @name.setter
    def name(self, name):
        if name not in ['A', 'B', 'C']:
            raise ValueError('Invalid simbol')
        self._name = name


simbol = Simbol("A")
print(simbol.name)
simbol.name = 'B'
print(simbol._name)
simbol._name = 'g'
print(simbol.name)