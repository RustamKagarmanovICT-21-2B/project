from fastapi import APIRouter, Form, Depends
from typing import Annotated
from datetime import timedelta
from app.services.auth import AuthJWTService
from app.api.v1.dto.response import TokenResponse, DeviceResponse, TemperatureResponse
from app.api.v1.dto.request import TurnRequest
from app.services.devices import AirConditionerService, HeaterService, TemperatureSensorService


from fastapi.routing import APIRoute

router = APIRouter(route_class=APIRoute, tags=["v1"])


@router.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    expire_in = timedelta(hours=1)
    access_token = await AuthJWTService.create_access_token(username=username, password=password, expires_delta=expire_in)
    return TokenResponse(
        access_token=access_token,
        expire_in=expire_in.total_seconds(),
        token_type="Bearer",
        scope="partnerosago.gateway",
    )
@router.post("air-conditioner/turn", response_model=DeviceResponse, dependencies=[Depends(AuthJWTService.verify_token_dependency)])
async def turn_air_conditioner(request: TurnRequest):
    return AirConditionerService.set_state(request.state)


@router.get("air-conditioner/status", response_model=DeviceResponse, dependencies=[Depends(AuthJWTService.verify_token_dependency)])
async def get_air_conditioner_status():
    return AirConditionerService.get_status()


@router.post("heater/turn", response_model=DeviceResponse, dependencies=[Depends(AuthJWTService.verify_token_dependency)])
async def turn_heater(request: TurnRequest):
    return HeaterService.set_state(request.state)


@router.get("heater/status", response_model=DeviceResponse, dependencies=[Depends(AuthJWTService.verify_token_dependency)])
async def get_heater_status():
    return HeaterService.get_status()


@router.get("/read", response_model=TemperatureResponse, dependencies=[Depends(AuthJWTService.verify_token_dependency)])
async def get_temperature_and_humidity():
    return TemperatureSensorService.get_temperature_and_humidity()

