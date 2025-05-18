import random
import time

class WeatherStation:
    def __init__(self):
        self.data = []

    def read_sensors(self):
        temperature = round(random.uniform(-10, 40), 2)  # °C
        humidity = round(random.uniform(10, 90), 2)      # %
        pressure = round(random.uniform(950, 1050), 2)   # hPa
        return {
            "temperature": temperature,
            "humidity": humidity,
            "pressure": pressure,
            "timestamp": time.time()
        }

    def collect_data(self):
        reading = self.read_sensors()
        self.data.append(reading)
        return reading

    def get_latest_reading(self):
        return self.data[-1] if self.data else None

    def get_all_readings(self):
        return self.data
