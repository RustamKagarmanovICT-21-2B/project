from app.services.devices.base import BaseDeviceService


class AirConditionerService(BaseDeviceService):
    device_name = "air_conditioner"

    @classmethod
    def initialize(cls):
        cls.initialize_gpio(pin=27)

