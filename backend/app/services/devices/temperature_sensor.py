import Adafruit_DHT
from app.api.v1.dto.response import TemperatureResponse


class TemperatureSensorService:
    SENSOR = Adafruit_DHT.DHT22
    PIN = 4  # GPIO пин, к которому подключен датчик

    @staticmethod
    def get_temperature_and_humidity()  -> TemperatureResponse:
        humidity, temperature = Adafruit_DHT.read_retry(TemperatureSensorService.SENSOR, TemperatureSensorService.PIN)
        if humidity is None or temperature is None:
            raise ValueError("Failed to read from the temperature sensor")
        return TemperatureResponse(
            temperature=temperature,
            humidity=humidity,
            message="Temperature and humidity retrieved successfully",
        )

