from pydantic import BaseModel


class TemperatureResponse(BaseModel):
    temperature: float
    humidity: float
    message: str

class DeviceResponse(BaseModel):
    """
    DTO для ответа устройства.
    """
    status: str
    device: str

class TokenResponse(BaseModel):
    access_token: str
    expire_in: int
    token_type: str
    scope: str
