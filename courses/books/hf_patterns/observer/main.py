from weather_data import WeatherData
from visual_element import CurrentConditionsDisplay


def main():
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay(weather_data)
    # Placeholders for additional displays
    # statistics_display = StatisticsDisplay(weather_data)
    # forecast_display = ForecastDisplay(weather_data)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

if __name__ == "__main__":
    main()
