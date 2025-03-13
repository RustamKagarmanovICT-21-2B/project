from fastapi import FastAPI

from app.api.api import routers_map
from app.api.health import router as health


def register_routers(app: FastAPI) -> None:
    for api_version, routers in routers_map.items():
        for router in routers:
            app.include_router(router, prefix=f'/api/{api_version}')

    app.include_router(health)
