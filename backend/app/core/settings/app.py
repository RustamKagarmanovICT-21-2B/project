from pydantic_settings import BaseSettings

from pydantic import BaseModel, SecretStr


class Environments(BaseModel):
    secret_key: SecretStr


class AppSettings(BaseSettings, Environments):
    debug: bool = False
    api_prefix: str = "/api"
    jwt_token_prefix: str = "Token"
    title: str = "api-connector"
    version: str = "1.0.0"

    @property
    def fastapi_kwargs(self) -> dict[str, ...]:
        return {
            "debug": self.debug,
            "title": self.title,
            "version": self.version,
        }

    class Config:
        env_file = ".env"
        extra = "allow"
