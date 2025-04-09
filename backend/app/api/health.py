from fastapi import APIRouter, Depends, HTTPException
from asyncpg import Pool, exceptions
from app.db.dependencies import get_db  

router = APIRouter(tags=["Health"])

@router.get("/ping")
async def ping():
    return {"ping": "pong!"}

@router.get("/health", summary="Проверка здоровья сервисов")
async def health_check(db: Pool = Depends(get_db)):
    service_status = {}
    try:
        # Проверка Postgre
        async with db.acquire() as connection:
            await connection.fetch("SELECT 1")
            service_status["postgres"] = "OK"
            
    except exceptions.PostgresError as e:
        service_status["postgres"] = f"Error: {str(e)}"
    except Exception as e:
        service_status["postgres"] = f"Unexpected error: {str(e)}"

    # Чтатус
    overall_status = "OK" if all(
        status == "OK" for status in service_status.values()
    ) else "Error"

    # Ответ
    response = {
        "status": overall_status,
        "services": service_status
    }

    # Возвращение статуса
    if overall_status == "OK":
        return response
    else:
        raise HTTPException(
            status_code=503,
            detail=response
        )