from app.services.devices.base import BaseDeviceService


class HeaterService(BaseDeviceService):
    """
    Сервис управления батареей.
    """

    def __init__(self):
        super().__init__(pin=17, device_name="heater")
