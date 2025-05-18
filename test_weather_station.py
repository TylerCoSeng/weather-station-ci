import time
from weather_station import WeatherStation


def test_read_sensors():
    ws = WeatherStation()
    reading = ws.read_sensors()

    assert "temperature" in reading
    assert "humidity" in reading
    assert "pressure" in reading
    assert "timestamp" in reading

    assert isinstance(reading["temperature"], float)
    assert isinstance(reading["humidity"], float)
    assert isinstance(reading["pressure"], float)
    assert isinstance(reading["timestamp"], float)


def test_collect_data_adds_reading():
    ws = WeatherStation()
    initial_len = len(ws.get_all_readings())
    ws.collect_data()
    assert len(ws.get_all_readings()) == initial_len + 1


def test_get_latest_reading():
    ws = WeatherStation()
    assert ws.get_latest_reading() is None  # No data yet

    ws.collect_data()
    latest = ws.get_latest_reading()
    assert latest is not None
    assert "temperature" in latest
    assert "humidity" in latest
    assert "pressure" in latest
    assert "timestamp" in latest
