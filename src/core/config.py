from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR: Path = Path(__file__).parent.parent.parent


class ImeiApiConfig(BaseModel):
    url: str = "https://api.imeicheck.net"
    token: str


class TgBotConfig(BaseModel):
    token: str
    allowed_users: list[int]


class ApiConfig(BaseModel):
    token: str
    host: str = "localhost"
    port: int = 8000
    protocol: Literal["http", "https"] = "http"


class Settings(BaseSettings):
    imei_api: ImeiApiConfig
    tg_bot: TgBotConfig
    api: ApiConfig

    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env",
        case_sensitive=False,
        env_nested_delimiter="__",
    )


settings = Settings()  # type: ignore
