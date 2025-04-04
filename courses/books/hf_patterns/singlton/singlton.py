class Singleton:
    _unique_instance = None

    def __new__(cls):
        if cls._unique_instance is None:
            cls._unique_instance = super().__new__(cls)
            # You can add any initialization code here if needed
        return cls._unique_instance

    # Other methods...

x = Singleton()
print(id(x))
y = Singleton()
print(id(y))

##########################################

import threading

class Singleton:
    _unique_instance = None
    _lock = threading.Lock()  # Class-level lock

    def __new__(cls):
        if cls._unique_instance is None:
            with cls._lock:  # Lock only around the first check
                if cls._unique_instance is None:  # Double-checked locking
                    cls._unique_instance = super().__new__(cls)
        return cls._unique_instance

    def __init__(self):
        # You can initialize only once, if needed
        pass