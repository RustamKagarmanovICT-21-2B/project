from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/ping")
async def ping():
    return {"ping": "pong!"}
