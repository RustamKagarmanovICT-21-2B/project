from fastapi import APIRouter

from fastapi.routing import APIRoute

router = APIRouter(route_class=APIRoute, tags=["v1"])
