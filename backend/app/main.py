from fastapi import FastAPI
from app.core.config import get_app_settings
from app.core.routes import register_routers

settings = get_app_settings()

app = FastAPI(**settings.fastapi_kwargs)

register_routers(app, settings)
