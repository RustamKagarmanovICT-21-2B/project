import sys
from app.api.v1.dto.response import TemperatureResponse

try:
    import board
    import adafruit_dht
except NotImplementedError:
    # Используем mock для эмуляции GPIO на неподдерживаемых платформах
    from unittest.mock import Mock
    board = Mock()
    adafruit_dht = Mock()


class TemperatureSensorService:
    """
    Сервис для работы с датчиком температуры (DHT22).
    """
    SENSOR = adafruit_dht.DHT22
    PIN = getattr(board, "D4", "D4")  # Используем эмуляцию для PIN

    @classmethod
    def get_temperature_and_humidity(cls) -> TemperatureResponse:
        """
        Возвращает текущую температуру и влажность через DTO.
        """
        try:
            sensor = cls.SENSOR(cls.PIN)
            temperature = sensor.temperature if hasattr(sensor, "temperature") else 22.5  # Эмуляция
            humidity = sensor.humidity if hasattr(sensor, "humidity") else 55.0  # Эмуляция
        except RuntimeError as e:
            raise ValueError(f"Failed to read from the temperature sensor: {e}")
        finally:
            if hasattr(sensor, "exit"):
                sensor.exit()

        if humidity is None or temperature is None:
            raise ValueError("Failed to retrieve temperature or humidity")

        return TemperatureResponse(
            temperature=temperature,
            humidity=humidity,
            message="Temperature and humidity retrieved successfully",
        )
