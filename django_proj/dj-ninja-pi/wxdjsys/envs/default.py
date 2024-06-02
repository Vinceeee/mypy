# 默认配置
import os
from enum import Enum
from pathlib import Path

DEBUG = True

_base_dir = Path("/tmp")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": _base_dir / "db.sqlite3",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}


class EnvEnum(Enum):
    UT = "ut"
    DEV = "dev"
    STAGE = "stage"
    PROD = "prod"


run_env = os.environ.get("RUN_ENV", "dev")

env = EnvEnum(run_env)

if env == EnvEnum.DEV:
    from .dev import *  # noqa
elif env == EnvEnum.UT:
    from .ut import *  # noqa
else:
    from .dev import *  # noqa
