from gpiozero import OutputDevice
from gpiozero import OutputDevice, Device
from gpiozero.pins.mock import MockFactory



class BaseDeviceService:
    relay: OutputDevice | None = None
    device_name: str = "base_device"


    @classmethod
    def initialize_gpio(cls, pin: int):
        try:
            cls.relay = OutputDevice(pin, active_high=True, initial_value=False)
        except Exception as e:
            print(f"GPIO Error: {e}")
            print("Switching to mock GPIO for development...")
            Device.pin_factory = MockFactory()  # Установить симуляцию GPIO
            cls.relay = OutputDevice(pin, active_high=True, initial_value=False)


    @classmethod
    def set_state(cls, state: bool):

        if state:
            cls.relay.on()
        else:
            cls.relay.off()
        return {"status": "on" if state else "off", "device": cls.device_name}



    @classmethod
    def get_status(cls):
        status = "on" if cls.relay.value else "off"
        return {"status": status, "device": cls.device_name}


