from weather_station import WeatherStation
import time


def main():
    station = WeatherStation()
    print("Weather Station is running... (press Ctrl+C to stop)")

    try:
        while True:
            reading = station.collect_data()
            print(f"Latest Reading: {reading}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nStopping Weather Station...")
        print(f"Total Readings Collected: {len(station.get_all_readings())}")


if __name__ == "__main__":
    main()
