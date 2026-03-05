# Observers
from interfaces import Observer, DisplayElement


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self._temperature = 0.0
        self._pressure = 0.0
        self._humidity = 0.0
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.display()

    def display(self):
        print(f"Current conditions: {self._temperature}F degrees and {self._humidity}% humidity")
