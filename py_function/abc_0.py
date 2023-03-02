# Absolute value

class ImpleventAbs:
    def __init__(self, string):
        self.string = string
    
    def __abs__(self):
        return self.string.lower()

custom_obj = ImpleventAbs("HELLO")

print(abs(-9))
print(abs(-39.8))
print(abs(custom_obj))