from fastapi import FastAPI
from app.core.settings import AppSettings

from app.api.api import routers_map
from app.api.health import router as health


def register_routers(app: FastAPI, settings: AppSettings) -> None:
    for api_version, routers in routers_map.items():
        for router in routers:
            app.include_router(router, prefix=f'{settings.api_prefix}/{api_version}')

    app.include_router(health)

