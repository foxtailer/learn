from abc import ABC, abstractmethod

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

# DisplayElement Interface
class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass
