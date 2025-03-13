from pydantic import BaseModel


class TemperatureResponse(BaseResponse):
    temperature: float
    humidity: float
    message: str


class DeviceResponse(BaseResponse):
    """
    DTO для ответа устройства.
    """
    status: str
    device: str

class BaseResponse(BaseModel):
    pass


class TokenResponse(BaseResponse):
    access_token: str
    expire_in: int
    token_type: str
    scope: str
