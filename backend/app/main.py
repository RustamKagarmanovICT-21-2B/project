from fastapi import FastAPI

app = FastAPI()
from app.core.routes import register_routers

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"ping": "pong!"}
register_routers(app)
