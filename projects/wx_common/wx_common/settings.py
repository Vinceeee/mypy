from pydantic_settings import BaseSettings
from loguru import logger


class Settings(BaseSettings):
    public_key: str = ""
    LOGURU_SETTINGS = [{}]

    def _setup(self):
        for _log_setting in self.LOGURU_SETTINGS:
            logger.add(**_log_setting)
