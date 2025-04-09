from asyncpg import create_pool, Pool

async def get_db() -> Pool:
    pool = await create_pool(
        dsn="postgresql://user:pass@db:5432/mydb",  # Для Docker: замените 'db' на 'localhost' если без контейнеров
        min_size=1,
        max_size=10
    )
    return pool