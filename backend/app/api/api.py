from types import MappingProxyType

from fastapi import APIRouter
from app.api.v1 import router as router_v1

routers_map: MappingProxyType[str, tuple[APIRouter, ...]] = MappingProxyType(
    {
        "v1": (router_v1,),
    },
)
