from fastapi import APIRouter, Form
from typing import Annotated
from datetime import timedelta
from app.services.auth import AuthJWTService
from app.api.v1.dto.response import TokenResponse

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
