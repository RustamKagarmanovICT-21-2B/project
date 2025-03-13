from fastapi import FastAPI
from app.core.routes import register_routers

app = FastAPI()


register_routers(app)
