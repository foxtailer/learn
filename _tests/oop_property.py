class A:
    first_name:str
    last_name:str

    def __init__(self, first, last) -> None:
        self.first_name = first
        self.last_name = last
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

a = A("a", "b")

print(a.get_full_name)