from gpiozero import OutputDevice


class BaseDeviceService:
    """
    Базовый класс для управления устройством через GPIO.
    """

    def __init__(self, pin: int, device_name: str):
        self.device_name = device_name
        self.relay = OutputDevice(pin, active_high=True, initial_value=False)

    def turn_on(self):
        """
        Включение устройства.
        """
        self.relay.on()
        return {"status": "on", "device": self.device_name}

    def turn_off(self):
        """
        Выключение устройства.
        """
        self.relay.off()
        return {"status": "off", "device": self.device_name}

    def get_status(self):
        """
        Получение текущего состояния устройства.
        """
        status = "on" if self.relay.value else "off"
        return {"status": status, "device": self.device_name}
