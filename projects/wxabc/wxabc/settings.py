from enum import IntEnum
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Stage(IntEnum):
    DEV = 1
    SIT = 2
    UAT = 3
    PROD = 4


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="WXABC_", env_file=".env")
    staging: Stage = Stage.DEV
    auth_key: str = Field(default="")
