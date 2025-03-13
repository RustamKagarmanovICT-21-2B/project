from app.services.devices.base import BaseDeviceService


class AirConditionerService(BaseDeviceService):
    """
    Сервис управления кондиционером.
    """

    def __init__(self):
        super().__init__(pin=27, device_name="air_conditioner")
