from datetime import datetime, timedelta, timezone
from app.core.config import get_app_settings
from fastapi import HTTPException
from jwt import encode

settings = get_app_settings()


class AuthJWTService:
    algorithm = "HS256"
    username = settings.username.get_secret_value()
    password = settings.password.get_secret_value()
    secret_key = settings.secret_key.get_secret_value()

    @classmethod
    async def create_access_token(cls, username: str, password: str, expires_delta: timedelta) -> str:
        if username != cls.username or password != cls.password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        jwt_payload = dict(sub=username)
        return cls._create_jwt(jwt_payload, expires_delta)

    @classmethod
    def _create_jwt(cls, data: dict, expires_delta: timedelta) -> str:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode = data.copy()
        to_encode.update({"exp": expire})
        return encode(to_encode, cls.secret_key, algorithm=cls.algorithm)
